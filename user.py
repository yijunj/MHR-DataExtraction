from bitstring import BitStream
import json
from utils import RSZ_TYPE_MAP

from alchemy import *
from armor import *
from boss import *
from condition_damage_preset import *
from item import *
from lot import *
from monster_data_base import *
from monster_data_tune import *
from monster_meat_data import *
from monster_condition_damage_data import *
from monster_anger_data import *
from monster_parts_break_data import *
from monster_boss_init_set_data import *
from monster_drop_item import *
from quest import *
from skill import *
from weapon import *

# This script is about reading user data files
# Basically, it reads a certain number of bits, assigns it to the current class attribute, then repeat

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

# Reads meta data of a user data file
def read_usr_head(data):
    magic = data.read('uintle:32')
    if magic != 0x00525355: # little-endian version of USR\0
        raise Exception('User magic should be "USR"')
    resource_count = data.read('uintle:32')
    child_count = data.read('uintle:32')
    padding = data.read('uintle:32')
    if padding != 0:
        raise Exception('padding should be zero')
    resource_list_offset = data.read('uintle:64')
    child_list_offset = data.read('uintle:64')
    rsz_offset = data.read('uintle:64')

    # What to do about resource_list_offset and child_list_offset?
    # Now read RSZ
    data.pos = rsz_offset * 8
    return data

# Reads meta data of a RSZ data file
def read_rsz_head(data):
    base = data.pos
    magic = data.read('uintle:32')
    if magic != 0x005A5352: # little-endian version of RSZ\0
        raise Exception('RSZ magic should be "RSZ"')
    version = data.read('uintle:32')
    if version != 0x10: # little-endian version of RSZ\0
        raise Exception('Version should be 0x10')
    root_count = data.read('uintle:32')
    type_descriptor_count = data.read('uintle:32')
    string_count = data.read('uintle:32')
    padding = data.read('uintle:32')
    if padding != 0:
        raise Exception('padding should be zero')
    type_descriptor_offset = data.read('uintle:64')
    data_offset = data.read('uintle:64')
    string_table_offset = data.read('uintle:64')

    # Do something to root: what is this?
    roots = []
    for i in range(root_count):
        roots.append(data.read('uintle:32'))

    # Now read type descriptor hashes
    data.pos = base + type_descriptor_offset * 8
    type_descriptor_list = []
    for i in range(type_descriptor_count):
        type_descriptor_list.append(data.read('uintle:64'))
    if type_descriptor_list[0] != 0:
        raise Exception('First type descriptor should be zero')

    data_type_list = []
    for type_descriptor in type_descriptor_list[1:]:
        data_type_list.append(RSZ_TYPE_MAP[str(type_descriptor & 0xFFFFFFFF)])

    data.pos = base + data_offset * 8
    return data_type_list, data

# Reads a chunk in the RSZ file corresponding to the given object
# The data part of RSZ is sequential according to a data type hash in the beginning of the file
# Here I send in a certain data type, create an object, an read the file to fill in its attributes
def read_rsz_chunk(data_type, data):
    object = eval(data_type)()
    object.add_padding()
    keys = list(object.keys())
    # print_object(object)

    for key in keys:
        attribute = getattr(object, key)
        if attribute is None:
            continue
        if type(attribute) == list: # This attribute takes in a list
            # The first list entry is the number of bits to encode each piece of data, but how many pieces?
            # i.e. how long will this list be? Well, normally, length of list is encoded in the next 32 bits
            # But occasionally, the length is encoded in less than that
            # In this case, the initialization of this attibute has the number of bits as the second list entry
            # This number is represented here as length_bit_num
            if attribute[0] == 'string': # List of strings
                length = data.read('uintle:32')
                temp_list = []
                for i in range(length):
                    char_num = data.read('uintle:32')
                    string = ''
                    for j in range(char_num):
                        string += chr(data.read('uintle:16'))
                    if string.endswith('\0'): # Excluding \0
                        string = string[:-1]
                    temp_list.append(string)
                    while data.pos % 32 != 0: # If not read in a full block of 4 bytes, move the cursor to the next block
                        data.pos += 1
                setattr(object, key, temp_list)
            elif attribute[0].startswith('u'): # List of integers
                if len(attribute) == 1:
                    length_bit_num = 32
                else:
                    length_bit_num = int(attribute[1][1:])
                length = data.read('uintle:' + str(length_bit_num)) # This is the length of the list
                format = attribute[0][1:].split(',')
                bit_num = int(format[0]) # This is the length of each entry in bits
                temp_list = []
                for i in range(length):
                    temp_list.append(data.read('uintle:' + str(bit_num)))
                setattr(object, key, temp_list)
                if len(format) == 1: # Needs padding
                    while data.pos % 32 != 0: # If not read in a full block of 4 bytes, move the cursor to the next block
                        data.pos += 1
            else:
                # This attribute 'eats' (absorbes other objects as its value)
                # Need to move the cursor to the correct position
                # Because after the parent node takes its children, the game file performs a count
                # Jump over the data number counts and move the cursor to the next data chunk
                while data.pos % 32 != 0:
                    data.pos += 1
                length = data.read('uintle:32')
                data.pos += length * 32
        else:
            if attribute == 'string': # String data
                char_num = data.read('uintle:32')
                string = ''
                for j in range(char_num):
                    string += chr(data.read('uintle:16'))
                if string.endswith('\0'): # Excluding \0
                    string = string[:-1]
                setattr(object, key, string)
                while data.pos % 32 != 0: # If not read in a full block of 4 bytes, move the cursor to the next block
                    data.pos += 1
            elif attribute.startswith('u'): # Integer data
                format = attribute[1:].split(',')
                bit_num = int(format[0])
                setattr(object, key, data.read('uintle:' + str(bit_num)))
                if len(format) == 1: # Needs padding
                    while data.pos % 32 != 0: # If not read in a full block of 4 bytes, move the cursor to the next block
                        data.pos += 1
            elif attribute.startswith('p'): # Pad until multiple of n-bit
                bit_num = int(attribute[1:])
                while data.pos % bit_num != 0:
                    data.pos += 1
            else:
                # This attribute eats
                # Need to move the cursor to the correct position
                # Because after the parent node takes its children, the game file performs a count
                # Jump over the data number counts and move the cursor to the next data chunk
                data.pos += 32

    object.human_readable()
    # print(data.pos)
    # print_object(object)
    return object, data

# Analyze the data type list, figure out the hierarchy between data types
# Some data types contain other data types
# i.e. object x of a certain data type X has object y of a certain data type Y as its attribute
# This shows in the data type list as [...Y,X...]
# So I need to see if a data type can absorb other data types in front of it in the list
# I call this 'eating' (object x eats object y)
# Sometimes x can eat multiple y's in front of it
# Here I create a stack and push the objects in if they don't have anything to eat
# However, if a data type x does eat, according to the structure it should eat the top of stack y
# So the code pops the top y, absorbs it into x, then repeat until the top is no longer edible by x
# Then x is pushed into the stack
# In the end the stack should only have a root left
def read_rsz(data_type_list, data):
    data_stack = []
    for data_type in data_type_list:
        # print(data_type)
        object = eval(data_type)()
        object.add_padding()
        keys = list(object.keys())

        # Data that eats: loop through key in reverse order because of the stack nature
        key_can_eat_list = []
        for key in reversed(keys):
            attribute = getattr(object, key)
            if type(attribute) == list:
                first_attribute = attribute[0]
            else:
                first_attribute = attribute

            eat_data_flag = False
            while len(data_stack) > 0:
                top_of_stack = data_stack[-1]
                if first_attribute == top_of_stack.__class__.__name__: # object can take top_of_stack as its list entry
                    key_can_eat_list.append(key)
                    eat_data_flag = True
                    data_stack.pop()
                    if type(attribute) == list:
                        attribute.append(top_of_stack)
                    else:
                        setattr(object, key, top_of_stack)
                        break # Only eat once if not a list
                else:
                    break
            if eat_data_flag and type(attribute) == list:
                attribute.reverse()
                attribute.pop() # Get rid of the initialization string

        # Data that don't eat: use read_rsz_chunk() to fill in values
        temp_object, data = read_rsz_chunk(data_type, data)
        for key in keys:
            attribute = getattr(object, key)
            if key not in key_can_eat_list: # This key does not eat data, then assign value
                setattr(object, key, getattr(temp_object, key))
        object.clean_up()
        # print_hierarchical_object(object)
        data_stack.append(object)
    if len(data_stack) != 1:
        raise Exception('Stack should only have the root left in the end')
    return data_stack[0], data

# Combines everything together
def read_user_file(filename):
    data = BitStream(filename = filename)
    data = read_usr_head(data)
    data_type_list, data = read_rsz_head(data)
    object, _ = read_rsz(data_type_list, data)
    return object

if __name__ == '__main__':
    # weapon_type = 'GreatSword'
    # filename = 'user\\weapon\\{}\\{}BaseData.user.2'.format(weapon_type, weapon_type)
    filename = 'user\\quest\\NormalQuestData.user.2'
    # filename = 'user\\skill\\PlHyakuryuSkillBaseData.user.2'
    object = read_user_file(filename)
    # print_first_few_params(object, 1000, deliminator='\n\n')
    # print_last_few_params(object, 3, deliminator='\n\n')
    print_hierarchical_object(object)
