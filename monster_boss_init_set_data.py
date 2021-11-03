from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to MHRice boss_init_set_data.rs
# Classes for monster initialization data, which will become part of Monster class

class LotInfo(OrderedAttibuteClass):
    def __init__(self):
        self.lot = 'u32'
        self.block = 'u32'
        self.id = 'u32'
    def human_readable(self):
        if self.lot > 0x7FFFFFFF: self.lot -= (0xFFFFFFFF + 1)
        if self.block > 0x7FFFFFFF: self.block -= (0xFFFFFFFF + 1)
        if self.id > 0x7FFFFFFF: self.id -= (0xFFFFFFFF + 1)

class SetInfo(OrderedAttibuteClass):
    def __init__(self):
        self.set_name = 'string'
        self.info = ['LotInfo']

class StageInfo(OrderedAttibuteClass):
    def __init__(self):
        self.map_type = 'u32'
        self.set_info_list = ['SetInfo']
    def human_readable(self):
        if self.map_type > 0x7FFFFFFF: self.map_type -= (0xFFFFFFFF + 1)

class EnemyBossInitSetData(OrderedAttibuteClass):
    def __init__(self):
        self.enemy_type = 'u32'
        self.stage_info_list = ['StageInfo']
    def human_readable(self):
        if self.enemy_type > 0x7FFFFFFF: self.enemy_type -= (0xFFFFFFFF + 1)
