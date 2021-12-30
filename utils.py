from collections import OrderedDict
import struct
import json
import os

cwd = 'M:\\MHR game data extraction\\Extract data with Python'

# Loads hash map from file: a dictionary from u32 keys to data type strings
# These strings are exactly names of the classes defined in each Python module
def hash_map():
    with open(os.path.join(cwd, 'hash\\data_type_dict.json'), 'r') as f:
        data_type_dict = json.load(f)
    return data_type_dict

RSZ_TYPE_MAP = hash_map()
VERSION = 12

# Class template that is inherited by many classes
# Features in ordered attributes
# Also padding marks to let the user file reader know when game file pads
class OrderedAttibuteClass(object):
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        instance.__odict__ = OrderedDict()
        return instance

    def __setattr__(self, key, value):
        if key != '__odict__':
            self.__odict__[key] = value
        object.__setattr__(self, key, value)

    def __delattr__(self, key):
        if key in self.keys():
            self.__odict__.pop(key)

    def keys(self):
        return self.__odict__.keys()

    def values(self):
        return self.__odict__.values()

    def items(self):
        return self.__odict__.items()

    def to_json(self):
        return json.dumps(self.__odict__, ensure_ascii=False)

    def versioned(self, attribute, vmin, vmax):
        if VERSION >= vmin and VERSION <= vmax:
            return attribute
        else:
            return None

    # The initialization of class attributes says how many bits the data piece takes
    # I do not distinguish signed vs unsigned, int vs float vs bool -- type casting happens later
    # When reading the data, all numeric attributes are marked one of the following:
    # 'string', 'u8', 'u16', 'u32'
    # and all-list attributes with numeric entries are marked as one of the following:
    # ['string'], ['u8'], ['u16'], ['u32']
    # and for those attributes that takes class objects, they are initialized with the corresponding class name
    # such as 'DataTunePartsLossData', or ['ArmorBaseUserDataParam'] (which is a list)
    # An n-bit data needs to start as data.pos being an integer multiple of n, otherwise needs padding in front

    # For numeric lists, game data always starts with a piece that says how many entries the list has
    # which is usually stored it 32 bits, but could also be less than that
    # In this case, the list is initialized as, say, ['u8, 'u16'], meaning 'list of u8 data, beginning with u16 entry count'
    # There are also cases where the game file skips until the next multiple of, say, 128 bits
    # In this case, I create a dummy attribute initialized to, say 'p128'
    # The user file reader moves the cursor to the appropriate location when it sees this
    # But since this attribute does not carry data, I delete it once the object has all data populated
    # which is the clean_up() method

    def clean_up(self):
        dummy_key_list = []
        for key, value in self.items():
            if value == 'p128' or value == 'p64' or value == 'p32' or value == 'p16':
                dummy_key_list.append(key)
        for key in dummy_key_list:
            delattr(self, key) # Delete attributes used for padding
        for value in self.values():
            if type(value) == list and len(value) == 1 and value[0] in RSZ_TYPE_MAP.values():
                value.pop() # Get rid of the initialization string

    # human_readable() method is called after the object has all its data populated
    # This method casts the data into the correct types
    # and is defined differently in each class
    def human_readable(self):
        pass

########################################
# General casting methods
# Casts hex (represented as string) into float
def hex_to_f32(hex):
    if hex == '0':
        return 0.0
    else:
        return round(struct.unpack('!f', bytes.fromhex(hex))[0], 3)

# Casts dec version of float-representing hex into float
def u32_to_f32(u32):
    return hex_to_f32(hex(u32)[2:])

# Casts unsigned int to signed int
def u32_to_i32(u32):
    if u32 > 0x7FFFFFFF:
        return u32 - (0xFFFFFFFF + 1)
    else:
        return u32

# Casts signed int to unsigned int
def i32_to_u32(i32):
    if i32 < 0:
        return i32 + (0xFFFFFFFF + 1)
    else:
        return i32

# Casts unsigned 8-bit int to signed int
def u8_to_i8(u8):
    if u8 > 0x7F:
        return u8 - (0xFF + 1)
    else:
        return u8

########################################
# General char/string manipulating methods
def u8_list_to_u16_str(u8_list):
    s = [chr(u8_list[i] + (u8_list[i+1] << 8)) for i in range(len(u8_list)) if i % 2 == 0]
    return ''.join(s)

def read_str_until_x00(string):
    s = []
    for char in string:
        if ord(char) == 0:
            break
        s.append(char)
    return ''.join(s)

def str_to_u16_hashable(string):
    hash_s = []
    for char in string:
        hash_s.append(char)
        if ord(char) <= 0xFF:
            hash_s.append('\x00')
    return ''.join(hash_s)

########################################
# General BitStream manipulating methods
# Move cursor (pad) to the next multiple of given number of bits
def pad_to_multiple_of(bit_num, data):
    while data.pos % bit_num != 0:
        data.pos += 1
    return data

########################################
# General printing methods
def print_hex(data):
    print('{:0>4X}'.format(data))

def print_object(ordered_attribute_object, deliminator='\n'):
    print(list(ordered_attribute_object.items()), end=deliminator)

def print_first_few_params(object, n, deliminator='\n'):
    if len(object.keys()) == 1:
        print('Print the first few params', end=deliminator)
        sub_object_list = list(object.items())[0][1]
        for i in range(min(n, len(sub_object_list))):
            print_object(sub_object_list[i], deliminator)
    else:
        raise Exception('Object has more than one attributes') # Should use print_hierarchical_object instead

def print_last_few_params(object, n, deliminator='\n'):
    if len(object.keys()) == 1:
        print('Print the last few params', end=deliminator)
        sub_object_list = list(object.items())[0][1]
        for i in reversed(range(min(n, len(sub_object_list)))):
            print_object(sub_object_list[-i-1], deliminator)
    else:
        raise Exception('Object has more than one attributes') # Should use print_hierarchical_object instead

# This prints a nested object (object has one ore more attributes that is/are other object(s)), unpacked
def print_hierarchical_object(object, deliminator='\n'):
    for key in object.keys():
        attribute = getattr(object, key)
        if type(attribute) == list:
            if len(attribute) == 0 or type(attribute[0]) == int or type(attribute[0]) == float or\
            type(attribute[0]) == str or type(attribute[0]) == bool or attribute[0] is None:
                print((key, attribute), end=', ')
            else:
                print(key, end=': ')
                for sub_object in attribute:
                    print('{', end='')
                    print_hierarchical_object(sub_object, deliminator)
        else:
            if type(attribute) == int or type(attribute) == float or\
            type(attribute) == str or type(attribute) == bool or attribute is None:
                print((key, attribute), end=', ')
            else:
                print(key, end=': {')
                print_hierarchical_object(attribute, deliminator)
    print('},', end=deliminator)
