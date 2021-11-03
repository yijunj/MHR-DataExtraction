from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to part of MHRice lot.rs
# Classes for monster lot and part data etc.

class MonsterLotTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.em_types = 'u32'
        self.quest_rank = 'u32'
        self.target_reward_item_id_list = ['u32']
        self.target_reward_num_list = ['u32']
        self.target_reward_probability_list = ['u32']
        self.enemy_reward_type_list = ['u32']
        self.hagitory_reward_item_id_list = ['u32']
        self.hagitory_reward_num_list = ['u32']
        self.hagitory_reward_probability_list = ['u32']
        self.capture_reward_item_id_list = ['u32']
        self.capture_reward_num_list = ['u32']
        self.capture_reward_probability_list = ['u32']
        self.parts_break_list = ['u32']
        self.parts_break_lv_list = ['u32']
        self.parts_break_reward_item_id_list = ['u32']
        self.parts_break_reward_num_list = ['u32']
        self.parts_break_reward_probability_list = ['u32']
        self.parts_break_reward_type_list = ['u32']
        self.drop_reward_type_list = ['u32']
        self.drop_reward_item_id_list = ['u32']
        self.drop_reward_num_list = ['u32']
        self.drop_reward_probability_list = ['u32']
        self.otomo_reward_item_id_list = ['u32']
        self.otomo_reward_num_list = ['u32']
        self.otomo_reward_probability_list = ['u32']
    def human_readable(self):
        self.em_types = enum_EmTypes(self.em_types)
        self.quest_rank = enum_QuestRank(self.quest_rank)
        self.target_reward_item_id_list = [enum_ItemId(i) for i in self.target_reward_item_id_list]
        self.enemy_reward_type_list = [enum_EnemyRewardPopTypes(i) for i in self.enemy_reward_type_list]
        self.hagitory_reward_item_id_list = [enum_ItemId(i) for i in self.hagitory_reward_item_id_list]
        self.capture_reward_item_id_list = [enum_ItemId(i) for i in self.capture_reward_item_id_list]
        self.parts_break_list = [enum_BrokenPartsTypes(i) for i in self.parts_break_list]
        self.parts_break_lv_list = [enum_BreakLvTypes(i) for i in self.parts_break_lv_list]
        self.parts_break_reward_item_id_list = [enum_ItemId(i) for i in self.parts_break_reward_item_id_list]
        self.parts_break_reward_type_list = [enum_EnemyRewardPopTypes(i) for i in self.parts_break_reward_type_list]
        self.drop_reward_type_list = [enum_EnemyRewardPopTypes(i) for i in self.drop_reward_type_list]
        self.drop_reward_item_id_list = [enum_ItemId(i) for i in self.drop_reward_item_id_list]
        self.otomo_reward_item_id_list = [enum_ItemId(i) for i in self.otomo_reward_item_id_list]

class MonsterLotTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['MonsterLotTableUserDataParam']

class PartsBreakGroupConditionInfo(OrderedAttibuteClass):
    def __init__(self):
        self.parts_group = 'u16'
        self.parts_break_level = 'u16'

class EnemyPartsBreakRewardInfo(OrderedAttibuteClass):
    def __init__(self):
        self.parts_break_condition_list = ['PartsBreakGroupConditionInfo']
        self.condition_type = 'u32'
        self.broken_parts_type = 'u32'
    def human_readable(self):
        self.condition_type = enum_EnemyPartsBreakRewardDataConditionType(self.condition_type)
        self.broken_parts_type = enum_BrokenPartsTypes(self.broken_parts_type)

class EnemyPartsBreakRewardData(OrderedAttibuteClass):
    def __init__(self):
        self.enemy_parts_break_reward_infos = ['EnemyPartsBreakRewardInfo']

class PartsTypeTextUserDataTextInfo(OrderedAttibuteClass):
    def __init__(self):
        self.enemy_type_list = ['u32']
        self.aligner = 'p64'
        self.text_bytes = 'u128'
        self.text_bytes_for_monster_list = 'u128'
    def human_readable(self):
        self.enemy_type_list = [enum_EmTypes(i) for i in self.enemy_type_list]
        self.text_bytes = [int(hex(self.text_bytes)[2*i+2:2*i+4], 16) for i in reversed(range(16))]
        self.text_bytes_for_monster_list =\
            [int(hex(self.text_bytes_for_monster_list)[2*i+2:2*i+4], 16) for i in reversed(range(16))]

class PartsTypeInfo(OrderedAttibuteClass):
    def __init__(self):
        self.broken_parts_type = 'u32'
        self.text_infos = ['PartsTypeTextUserDataTextInfo']
    def human_readable(self):
        self.broken_parts_type = enum_BrokenPartsTypes(self.broken_parts_type)

class PartsTypeTextUserData(OrderedAttibuteClass):
    def __init__(self):
        self.params = ['PartsTypeInfo']
