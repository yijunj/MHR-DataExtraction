import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice boss_init_set_data.rs
# Classes for monster initialization data, which will become part of Monster class

class LotInfo(OrderedAttibuteClass):
    def __init__(self):
        self.lot = 'u32'
        self.block = 'u32'
        self.id = 'u32'
    def human_readable(self):
        self.lot = utils.u32_to_i32(self.lot)
        self.block = utils.u32_to_i32(self.block)
        self.id = utils.u32_to_i32(self.id)

class SetInfo(OrderedAttibuteClass):
    def __init__(self):
        self.set_name = 'string'
        self.info = ['LotInfo']

class StageInfo(OrderedAttibuteClass):
    def __init__(self):
        self.map_type = 'u32'
        self.set_info_list = ['SetInfo']
    def human_readable(self):
        self.map_type = utils.u32_to_i32(self.map_type)

class EnemyBossInitSetData(OrderedAttibuteClass):
    def __init__(self):
        self.enemy_type = 'u32'
        self.stage_info_list = ['StageInfo']
    def human_readable(self):
        self.enemy_type = utils.u32_to_i32(self.enemy_type)
