from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to part of MHRice lot.rs
# Classes for monster drop item data, which will become part of Monster class

class EnemyDropItemInfo(OrderedAttibuteClass):
    def __init__(self):
        self.percentage = 'u32'
        self.enemy_reward_pop_type = 'u32'
        self.drop_item_model_type = 'u32'
    def human_readable(self):
        self.enemy_reward_pop_type = enum_EnemyRewardPopTypes(self.enemy_reward_pop_type)
        if self.drop_item_model_type > 0x7FFFFFFF: self.drop_item_model_type -= (0xFFFFFFFF + 1)

class EnemyDropItemTableData(OrderedAttibuteClass):
    def __init__(self):
        self.percentage = 'u32'
        self.enemy_drop_item_info_list = ['EnemyDropItemInfo']
        self.max_num = 'u32'
    def human_readable(self):
        if self.max_num > 0x7FFFFFFF: self.max_num -= (0xFFFFFFFF + 1)

class EnemyDropItemInfoData(OrderedAttibuteClass):
    def __init__(self):
        self.enemy_drop_item_table_data_tbl = ['EnemyDropItemTableData']
        self.marionette_reward_pop_type = 'u32'
    def human_readable(self):
        self.marionette_reward_pop_type = enum_EnemyRewardPopTypes(self.marionette_reward_pop_type)
