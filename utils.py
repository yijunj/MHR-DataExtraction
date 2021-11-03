from collections import OrderedDict
import struct
import json

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

    def add_padding(self):
        for i in range(len(self.keys())):
            key_list = list(self.keys())
            dtype = getattr(self, key_list[i])
            if type(dtype) == list:
                if dtype[0].startswith('u') and dtype[0] != 'u32' and i+1 < len(key_list):
                    dtype_next = getattr(self, key_list[i+1])
                    if dtype[0] == dtype_next:
                        dtype[0] += ',np'
            else:
                if dtype.startswith('u') and dtype != 'u32' and i+1 < len(key_list):
                    dtype_next = getattr(self, key_list[i+1])
                    if (dtype=='u16' and dtype_next=='u16') or dtype_next=='u8':
                        setattr(self, key_list[i], dtype+',np')

    def clean_up(self):
        dummy_key_list = []
        for item in self.items():
            if item[1] == 'p128' or item[1] == 'p64' or item[1] == 'p32':
                dummy_key_list.append(item[0])
        for key in dummy_key_list:
            delattr(self, key)

    def human_readable(self):
        pass

def hex_to_f32(hex):
    if hex == '0':
        return 0.0
    else:
        return round(struct.unpack('!f', bytes.fromhex(hex))[0], 3)

def hash_map():
    with open('hash/data_type_dict.json', 'r') as f:
        data_type_dict = json.load(f)
    return data_type_dict

RSZ_TYPE_MAP = hash_map()
