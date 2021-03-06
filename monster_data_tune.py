import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice data_tune.rs
# Classes for monster data, which will become part of Monster class

class EnemyPartsData(OrderedAttibuteClass):
    def __init__(self):
        self.vital = 'u32'
        self.extractive_type = 'u32'
    def human_readable(self):
        self.vital = utils.u32_to_i32(self.vital)
        self.extractive_type = enum_ExtractiveType(self.extractive_type)

class DataTunePartsBreakData(OrderedAttibuteClass):
    def __init__(self):
        self.break_level = 'u32'
        self.vital = 'u32'
        self.ignore_condition = 'u32'
        self.ignore_check_count = 'u32'
        self.reward_data = 'u32'
    def human_readable(self):
        self.break_level = utils.u32_to_i32(self.break_level)
        self.vital = utils.u32_to_i32(self.vital)
        self.ignore_condition = enum_PartsBreakDataIgnoreCondition(self.ignore_condition)
        self.ignore_check_count = utils.u32_to_i32(self.ignore_check_count)
        self.reward_data = utils.u32_to_i32(self.reward_data)

class DataTuneEnemyPartsBreakData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_group = 'u16'
        self.parts_break_data_list = ['DataTunePartsBreakData']

class DataTunePartsLossData(OrderedAttibuteClass):
    def __init__(self):
        self.vital = 'u32'
        self.permit_damage_attr = 'u32'
    def human_readable(self):
        self.vital = utils.u32_to_i32(self.vital)
        self.permit_damage_attr = enum_PermitDamageAttrEnum(self.permit_damage_attr)

class DataTuneEnemyPartsLossData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_group = 'u16'
        self.parts_loss_data = 'DataTunePartsLossData'

class EnablePartsGroup(OrderedAttibuteClass):
    def __init__(self):
        self.enable_parts = ['u8']
    def human_readable(self):
        self.enable_parts = [bool(i) for i in self.enable_parts]

class MultiPartsVital(OrderedAttibuteClass):
    def __init__(self):
        self.vital = 'u32'
    def human_readable(self):
        self.vital = utils.u32_to_i32(self.vital)

class EnemyMultiPartsSystemVitalData(OrderedAttibuteClass):
    def __init__(self):
        self.use_type = 'u32'
        self.priority = 'u32'
        self.enable_parts_data = ['EnablePartsGroup']
        self.enable_last_attack_parts = ['string']
        self.is_enable_hyakuryu = 'u8'
        self.is_enable_overwrite_down = 'u8'
        self.is_prio_damage_customize = 'u8'
        self.prio_damage_catagory_flag = 'u32'
        self.is_multi_rate_ex = 'u8'
        self.multi_parts_vital_data = ['MultiPartsVital']
        self.enable_parts_names = ['string']
        self.enable_parts_values = ['u32']
    def human_readable(self):
        self.use_type = enum_UseDataType(self.use_type)
        self.is_enable_hyakuryu = bool(self.is_enable_hyakuryu)
        self.is_enable_overwrite_down = bool(self.is_enable_overwrite_down)
        self.is_prio_damage_customize = bool(self.is_prio_damage_customize)
        self.prio_damage_catagory_flag = bitflags_DamageCategoryFlag(self.prio_damage_catagory_flag)
        self.is_multi_rate_ex = bool(self.is_multi_rate_ex)
        self.enable_parts_values = [utils.u32_to_i32(i) for i in self.enable_parts_values]

class EnemyMultiPartsVitalData(OrderedAttibuteClass):
    def __init__(self):
        self.use_type = 'u32'
        self.priority = 'u32'
        self.enable_parts_data = ['EnablePartsGroup']
        self.enable_last_attack_parts = ['string']
        self.is_enable_hyakuryu = 'u8'
        self.is_enable_overwrite_down = 'u8'
        self.is_prio_damage_customize = 'u8'
        self.prio_damage_catagory_flag = 'u32'
        self.is_multi_rate_ex = 'u8'
        self.multi_parts_vital_data = ['MultiPartsVital']
        self.enable_parts_names = ['string']
        self.enable_parts_values = ['u32']
    def human_readable(self):
        self.use_type = enum_UseDataType(self.use_type)
        self.is_enable_hyakuryu = bool(self.is_enable_hyakuryu)
        self.is_enable_overwrite_down = bool(self.is_enable_overwrite_down)
        self.is_prio_damage_customize = bool(self.is_prio_damage_customize)
        self.prio_damage_catagory_flag = bitflags_DamageCategoryFlag(self.prio_damage_catagory_flag)
        self.is_multi_rate_ex = bool(self.is_multi_rate_ex)
        self.enable_parts_values = [utils.u32_to_i32(i) for i in self.enable_parts_values]

class EnemyGimmickVitalData(OrderedAttibuteClass):
    def __init__(self):
        self.vital_s = 'u32'
        self.vital_m = 'u32'
        self.vital_l = 'u32'
        self.vital_knock_back = 'u32'
    def human_readable(self):
        self.vital_s = utils.u32_to_i32(self.vital_s)
        self.vital_m = utils.u32_to_i32(self.vital_m)
        self.vital_l = utils.u32_to_i32(self.vital_l)
        self.vital_knock_back = utils.u32_to_i32(self.vital_knock_back)

class EnemyMarionetteVitalData(OrderedAttibuteClass):
    def __init__(self):
        self.vital_s = 'u32'
        self.vital_m = 'u32'
        self.vital_l = 'u32'
    def human_readable(self):
        self.vital_s = utils.u32_to_i32(self.vital_s)
        self.vital_m = utils.u32_to_i32(self.vital_m)
        self.vital_l = utils.u32_to_i32(self.vital_l)

class CharacterContollerTune(OrderedAttibuteClass):
    def __init__(self):
        self.radius = 'u32'
        self.offset_y = 'u32'
    def human_readable(self):
        self.radius = utils.u32_to_f32(self.radius)
        self.offset_y = utils.u32_to_f32(self.offset_y)

class EnemyDataTune(OrderedAttibuteClass):
    def __init__(self):
        self.base_hp_vital = 'u32'
        self.enemy_parts_data = ['EnemyPartsData']
        self.enemy_parts_break_data_list = ['DataTuneEnemyPartsBreakData']
        self.enemy_parts_loss_data_list = ['DataTuneEnemyPartsLossData']
        self.enemy_multi_parts_vital_system_data = ['EnemyMultiPartsSystemVitalData']
        self.enemy_multi_parts_vital_data_list = ['EnemyMultiPartsVitalData']
        self.gimmick_vital_data = 'EnemyGimmickVitalData'
        self.marionette_vital_data = 'EnemyMarionetteVitalData'
        self.terrain_action_check_dist = 'u32'
        self.adjust_wall_point_offset = 'u32'
        self.character_controller_tune_data = ['CharacterContollerTune']
        self.weight = 'u8'
        self.dying_village_hp_vital_rate = 'u32'
        self.dying_low_level_hp_vital_rate = 'u32'
        self.dying_high_level_hp_vital_rate = 'u32'
        self.capture_village_hp_vital_rate = 'u32'
        self.capture_low_level_hp_vital_rate = 'u32'
        self.capture_high_level_hp_vital_rate = 'u32'
        self.self_sleep_recover_hp_vital_rate = 'u32'
        self.self_sleep_time = 'u32'
        self.in_combat_self_sleep_flag = 'u8'
        self.dummy_shadow_scale = 'u32'
        self.max_num_for_normal_quest = 'u32'
        self.max_num_for_hyakuryu_quest = 'u32'
        self.max_sound_damage_count = 'u32'
    def human_readable(self):
        self.base_hp_vital = utils.u32_to_i32(self.base_hp_vital)
        self.terrain_action_check_dist = utils.u32_to_f32(self.terrain_action_check_dist)
        self.adjust_wall_point_offset = utils.u32_to_f32(self.adjust_wall_point_offset)
        self.weight = enum_HitWeight(self.weight)
        self.dying_village_hp_vital_rate = utils.u32_to_f32(self.dying_village_hp_vital_rate)
        self.dying_low_level_hp_vital_rate = utils.u32_to_f32(self.dying_low_level_hp_vital_rate)
        self.dying_high_level_hp_vital_rate = utils.u32_to_f32(self.dying_high_level_hp_vital_rate)
        self.capture_village_hp_vital_rate = utils.u32_to_f32(self.capture_village_hp_vital_rate)
        self.capture_low_level_hp_vital_rate = utils.u32_to_f32(self.capture_low_level_hp_vital_rate)
        self.capture_high_level_hp_vital_rate = utils.u32_to_f32(self.capture_high_level_hp_vital_rate)
        self.self_sleep_recover_hp_vital_rate = utils.u32_to_f32(self.self_sleep_recover_hp_vital_rate)
        self.self_sleep_time = utils.u32_to_f32(self.self_sleep_time)
        self.in_combat_self_sleep_flag = bool(self.in_combat_self_sleep_flag)
        self.dummy_shadow_scale = utils.u32_to_f32(self.dummy_shadow_scale)
        self.max_num_for_normal_quest = utils.u32_to_i32(self.max_num_for_normal_quest)
        self.max_num_for_hyakuryu_quest = utils.u32_to_i32(self.max_num_for_hyakuryu_quest)
        self.max_sound_damage_count = utils.u32_to_i32(self.max_sound_damage_count)
