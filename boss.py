from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to MHRice monster_list.rs
# Classes for monster habitat data etc.

class PartData(OrderedAttibuteClass):
    def __init__(self):
        self.part = 'u32'
        self.circle_size = 'u32'
        self.begin_align = 'p128' # Pad until multiple of 128-bit
        self.circle_pos_x = 'u32' # ViaVec2.x in MHRice
        self.circle_pos_y = 'u32' # ViaVec2.y in MHRice
        self.end_align = 'p128' # Pad until multiple of 128-bit
        self.em_meat = 'u32'
        self.em_meat_group_index = 'u32'
    def human_readable(self):
        if self.part > 0x7FFFFFFF: self.part -= (0xFFFFFFFF + 1)
        if self.circle_size > 0x7FFFFFFF: self.circle_size -= (0xFFFFFFFF + 1)
        self.circle_pos_x = utils.hex_to_f32(hex(self.circle_pos_x)[2:])
        self.circle_pos_y = utils.hex_to_f32(hex(self.circle_pos_y)[2:])
        if self.em_meat > 0x7FFFFFFF: self.em_meat -= (0xFFFFFFFF + 1)
        if self.em_meat_group_index > 0x7FFFFFFF: self.em_meat_group_index -= (0xFFFFFFFF + 1)

class BitSetFlagHabitatType(OrderedAttibuteClass):
    def __init__(self):
        self.flag = ['u32']

class BossMonsterData(OrderedAttibuteClass):
    def __init__(self):
        self.em_type = 'u32'
        self.family_type = 'u32'
        self.habitat_area = 'BitSetFlagHabitatType'
        self.is_limit_open_lv = 'u8'
        self.part_Table_data = ['PartData']
    def human_readable(self):
        self.em_type = enum_EmTypes(self.em_type)
        if self.family_type > 0x7FFFFFFF: self.family_type -= (0xFFFFFFFF + 1)
        self.is_limit_open_lv = bool(self.is_limit_open_lv)

class MonsterListBossData(OrderedAttibuteClass):
    def __init__(self):
        self.data_list = ['BossMonsterData']
