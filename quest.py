import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice quest_data.rs
# Classes for quest data

class NormalQuestDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.quest_no = 'u32'
        self.quest_type = 'u32'
        self.quest_level = 'u32'
        self.enemy_level = 'u32'
        self.map_no = 'u32'
        self.base_time = 'u32'
        self.time_variation = 'u32'
        self.time_limit = 'u32'
        self.quest_life = 'u32'
        self.order_type = ['u32']
        self.target_type = ['u8']
        self.tgt_em_type = ['u32']
        self.tgt_item_id = ['u32']
        self.tgt_num = ['u32']
        self.boss_em_type = ['u32']
        self.init_extra_em_num = 'u32'
        self.swap_em_rate = ['u8']
        self.boss_set_condition = ['u32']
        self.boss_set_param = ['u32']
        self.swap_set_condition = ['u32']
        self.swap_set_param = ['u8']
        self.swap_exit_time = self.versioned(['u8', 'u16'], 5, 0xFFFFFFFF)
        self.is_swap_exit_marionette = self.versioned('u8', 5, 0xFFFFFFFF)
        self.swap_stop_type = 'u32'
        self.swap_stop_param = 'u32'
        self.swap_exec_type = 'u32'
        self.rem_money = 'u32'
        self.rem_village_point = 'u32'
        self.rem_rank_point = 'u32'
        self.supply_tbl = 'u32'
        self.icon = ['u32']
        self.is_from_npc = self.versioned('u8,np', 0, 4)
        self.is_tutorial = 'u8,np'
        self.fence_default_active = 'u8,np'
        self.aligner = 'p16'
        self.fence_active_sec = 'u16'
        self.fence_default_wait_sec = 'u16'
        self.fence_reload_sec = 'u16'
        self.is_use_pillar = ['u8']
        self.auto_match_hr = 'u32'
        self.battle_bgm_type = 'u32'
        self.clear_bgm_type = 'u32'
    def human_readable(self):
        self.quest_no = utils.u32_to_i32(self.quest_no)
        self.quest_type = bitflags_QuestType(self.quest_type)
        self.quest_level = enum_QuestLevel(self.quest_level)
        self.enemy_level = enum_EnemyLevel(self.enemy_level)
        self.map_no = utils.u32_to_i32(self.map_no)
        self.order_type = [enum_QuestOrderType(i) for i in self.order_type]
        self.target_type = [enum_QuestTargetType(i) for i in self.target_type]
        self.tgt_em_type = [enum_EmTypes(i) for i in self.tgt_em_type]
        self.boss_em_type = [enum_EmTypes(i) for i in self.boss_em_type]
        self.boss_set_condition = [enum_BossSetCondition(i) for i in self.boss_set_condition]
        self.swap_set_condition = [enum_SwapSetCondition(i) for i in self.swap_set_condition]
        if not self.is_swap_exit_marionette is None:
            self.is_swap_exit_marionette = bool(self.is_swap_exit_marionette)
        self.swap_stop_type = enum_SwapStopType(self.swap_stop_type)
        self.swap_exec_type = enum_SwapExecType(self.swap_exec_type)
        self.icon = [utils.u32_to_i32(i) for i in self.icon]
        if not self.is_from_npc is None:
            self.is_from_npc = bool(self.is_from_npc)
        self.is_tutorial = bool(self.is_tutorial)
        self.fence_default_active = bool(self.fence_default_active)
        self.is_use_pillar = [bool(i) for i in self.is_use_pillar]
        self.battle_bgm_type = enum_BattleBgmType(self.battle_bgm_type)
        self.clear_bgm_type = enum_ClearBgmType(self.clear_bgm_type)

class NormalQuestData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['NormalQuestDataParam']

class SharedEnemyParam(OrderedAttibuteClass):
    def __init__(self):
        self.route_no = ['u8']
        self.init_set_name = ['string']
        self.sub_type = ['u8']
        self.vital_tbl = ['u8']
        self.attack_tbl = ['u8']
        self.parts_tbl = ['u8']
        self.other_tbl = ['u8']
        self.stamina_tbl = ['u8']
        self.scale = ['u8']
        self.scale_tbl = ['u32']
        self.difficulty = ['u32']
        self.boss_multi = ['u8']
    def human_readable(self):
        self.scale_tbl = [utils.u32_to_i32(i) for i in self.scale_tbl]
        self.difficulty = [enum_NandoYuragi(i) for i in self.difficulty]

class NormalQuestDataForEnemyParam(SharedEnemyParam):
    def __init__(self):
        super().__init__()
        super_key_list = list(super().keys())
        self.quest_no = 'u32'
        self.ems_set_no = 'u32'
        self.zako_vital = 'u8'
        self.zako_attack = 'u8'
        self.zako_parts = 'u8'
        self.zako_other = 'u8'
        self.zako_multi = 'u8'
        for key in super_key_list: # Need to move keys of parent class to the end
            self.__odict__.move_to_end(key)
    def human_readable(self):
        super().human_readable()
        self.quest_no = utils.u32_to_i32(self.quest_no)
        self.ems_set_no = utils.u32_to_i32(self.ems_set_no)

class NormalQuestDataForEnemy(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['NormalQuestDataForEnemyParam']

class VitalRateTableData(OrderedAttibuteClass):
    def __init__(self):
        self.vital_rate = 'u32'
    def human_readable(self):
        self.vital_rate = utils.u32_to_f32(self.vital_rate)

class AttackRateTableData(OrderedAttibuteClass):
    def __init__(self):
        self.attack_rate = 'u32'
    def human_readable(self):
        self.attack_rate = utils.u32_to_f32(self.attack_rate)

class PartsRateTableData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_vital_rate = 'u32'
    def human_readable(self):
        self.parts_vital_rate = utils.u32_to_f32(self.parts_vital_rate)

class OtherRateTableData(OrderedAttibuteClass):
    def __init__(self):
        self.defense_rate = 'u32'
        self.damage_element_rate_a = 'u32'
        self.damage_element_rate_b = 'u32'
        self.stun_rate = 'u32'
        self.tired_rate = 'u32'
        self.marionette_rate = 'u32'
    def human_readable(self):
        self.defense_rate = utils.u32_to_f32(self.defense_rate)
        self.damage_element_rate_a = utils.u32_to_f32(self.damage_element_rate_a)
        self.damage_element_rate_b = utils.u32_to_f32(self.damage_element_rate_b)
        self.stun_rate = utils.u32_to_f32(self.stun_rate)
        self.tired_rate = utils.u32_to_f32(self.tired_rate)
        self.marionette_rate = utils.u32_to_f32(self.marionette_rate)

class MultiData(OrderedAttibuteClass):
    def __init__(self):
        self.two = 'u32'
        self.three = 'u32'
        self.four = 'u32'
    def human_readable(self):
        self.two = utils.u32_to_f32(self.two)
        self.three = utils.u32_to_f32(self.three)
        self.four = utils.u32_to_f32(self.four)

class MultiRateTableData(OrderedAttibuteClass):
    def __init__(self):
        self.multi_data_list = ['MultiData']

class SystemDifficultyRateData(OrderedAttibuteClass):
    def __init__(self):
        self.vital_rate_table_list = ['VitalRateTableData']
        self.attack_rate_table_list = ['AttackRateTableData']
        self.parts_rate_table_list = ['PartsRateTableData']
        self.other_rate_table_list = ['OtherRateTableData']
        self.multi_rate_table_list = ['MultiRateTableData']

class ScaleAndRateData(OrderedAttibuteClass):
    def __init__(self):
        self.scale = 'u32'
        self.rate = 'u32'
    def human_readable(self):
        self.scale = utils.u32_to_f32(self.scale)

class RandomScaleTableData(OrderedAttibuteClass):
    def __init__(self):
        self.type = 'u32'
        self.scale_and_rate_data = ['ScaleAndRateData']
    def human_readable(self):
        self.type = utils.u32_to_i32(self.type)

class EnemyBossRandomScaleData(OrderedAttibuteClass):
    def __init__(self):
        self.random_scale_table_data_list = ['RandomScaleTableData']

class SizeInfo(OrderedAttibuteClass):
    def __init__(self):
        self.em_type = 'u32'
        self.base_size = 'u32'
        self.small_boarder = 'u32'
        self.big_boarder = 'u32'
        self.king_boarder = 'u32'
        self.no_size_scale = 'u8'
    def human_readable(self):
        self.em_type = enum_EmTypes(self.em_type)
        self.base_size = utils.u32_to_f32(self.base_size)
        self.small_boarder = utils.u32_to_f32(self.small_boarder)
        self.big_boarder = utils.u32_to_f32(self.big_boarder)
        self.king_boarder = utils.u32_to_f32(self.king_boarder)
        self.no_size_scale = bool(self.no_size_scale)

class EnemySizeListData(OrderedAttibuteClass):
    def __init__(self):
        self.size_info_param = ['SizeInfo']

class DiscoverEmSetDataParam(SharedEnemyParam):
    def __init__(self):
        super().__init__()
        super_key_list = list(super().keys())
        self.em_type = 'u32'
        self.cond_village = 'u32'
        self.cond_low = 'u32'
        self.cond_high = 'u32'
        self.map_flag = ['u8']
        for key in super_key_list: # Need to move keys of parent class to the end
            self.__odict__.move_to_end(key)
    def human_readable(self):
        super().human_readable()
        self.em_type = enum_EmTypes(self.em_type)
        self.cond_village = enum_VillageProgress(self.cond_village)
        self.cond_low = utils.u32_to_i32(self.cond_low)
        self.cond_high = utils.u32_to_i32(self.cond_high)
        self.map_flag = [bool(i) for i in self.map_flag]

class DiscoverEmSetData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['DiscoverEmSetDataParam']
