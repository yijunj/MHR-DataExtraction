from collections import OrderedDict
import struct
import json

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

    def items(self):
        return self.__odict__.items()

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
        for item in self.items():
            if item[1] == 'p128' or item[1] == 'p64' or item[1] == 'p32' or item[1] == 'p16':
                dummy_key_list.append(item[0])
        for key in dummy_key_list:
            delattr(self, key)

    # human_readable() method is called after the object has all its data populated
    # This method casts the data into the correct types
    # and is defined differently in each class
    def human_readable(self):
        pass

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

# Casts unsigned 8-bit int to signed int
def u8_to_i8(u8):
    if u8 > 0x7F:
        return u8 - (0xFF + 1)
    else:
        return u8

# Loads hash map from file: a dictionary from u32 keys to data type strings
# These strings are exactly names of the classes defined in each Python module
def hash_map():
    with open('hash/data_type_dict.json', 'r') as f:
        data_type_dict = json.load(f)
    return data_type_dict

RSZ_TYPE_MAP = hash_map()
VERSION = 12
