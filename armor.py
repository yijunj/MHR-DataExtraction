import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice armor.rs
# Classes for armor data

class ArmorBaseUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.pl_armor_id = 'u32'
        self.is_valid = 'u8'
        self.series = 'u32'
        self.sort_id = 'u32'
        self.model_id = 'u32'
        self.rare = 'u8'
        self.value = 'u32'
        self.buy_value = 'u32'
        self.sexual_equipable = 'u32'
        self.symbol_color1 = 'u8'
        self.symbol_color2 = 'u8'
        self.def_val = 'u32'
        self.fire_reg_val = 'u32'
        self.water_reg_val = 'u32'
        self.ice_reg_val = 'u32'
        self.thunder_reg_val = 'u32'
        self.dragon_reg_val = 'u32'
        self.buildup_table = 'u32'
        self.buff_formula = 'u32'
        self.decorations_num_list = ['u32']
        self.skill_list = ['u8']
        self.skill_lv_list = ['u32']
        self.id_after_ex_change = 'u32'
    def human_readable(self):
        self.pl_armor_id = enum_PlArmorId(self.pl_armor_id)
        self.is_valid = bool(self.is_valid)
        self.series = newtype_PlArmorSeriesTypes(self.series)
        self.rare = newtype_RareTypes(self.rare)
        self.sexual_equipable = enum_SexualEquipableFlag(self.sexual_equipable)
        self.symbol_color1 = bool(self.symbol_color1)
        self.symbol_color2 = bool(self.symbol_color2)
        self.def_val = utils.u32_to_i32(self.def_val)
        self.fire_reg_val = utils.u32_to_i32(self.fire_reg_val)
        self.water_reg_val = utils.u32_to_i32(self.water_reg_val)
        self.ice_reg_val = utils.u32_to_i32(self.ice_reg_val)
        self.thunder_reg_val = utils.u32_to_i32(self.thunder_reg_val)
        self.dragon_reg_val = utils.u32_to_i32(self.dragon_reg_val)
        self.buildup_table = utils.u32_to_i32(self.buildup_table)
        self.buff_formula = utils.u32_to_i32(self.buff_formula)
        self.skill_list = [enum_PlEquipSkillId(i) for i in self.skill_list]
        self.skill_lv_list = [utils.u32_to_i32(i) for i in self.skill_lv_list]
        self.id_after_ex_change = enum_PlArmorId(self.id_after_ex_change)

class ArmorBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ArmorBaseUserDataParam']

class ArmorSeriesUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.armor_series = 'u32'
        self.difficulty_group = 'u32'
        self.is_collabo = 'u8'
        self.index = 'u32'
        self.overwear_sort_index = 'u32'
        self.sexual_enable = 'u32'
    def human_readable(self):
        self.armor_series = newtype_PlArmorSeriesTypes(self.armor_series)
        self.difficulty_group = enum_EquipDifficultyGroup(self.difficulty_group)
        self.is_collabo = bool(self.is_collabo)
        self.sexual_enable = enum_SexualEquipableFlag(self.sexual_enable)

class ArmorSeriesUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ArmorSeriesUserDataParam']

class ArmorProductUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.item_flag = 'u32'
        self.enemy_flag = 'u32'
        self.progress_flag = 'u32'
        self.item = ['u32']
        self.item_num = ['u32']
        self.material_category = 'u32'
        self.material_category_num = 'u32'
        self.output_item = ['u32']
        self.output_item_num = ['u32']
    def human_readable(self):
        self.id = enum_PlArmorId(self.id)
        self.item_flag = enum_ItemId(self.item_flag)
        self.enemy_flag = enum_EmTypes(self.enemy_flag)
        self.progress_flag = utils.u32_to_i32(self.progress_flag)
        self.item = [enum_ItemId(i) for i in self.item]
        self.material_category = newtype_MaterialCategory(self.material_category)
        self.output_item = [enum_ItemId(i) for i in self.output_item]

class ArmorProductUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ArmorProductUserDataParam']

class PlOverwearBaseUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.is_valid = 'u8'
        self.relative_id = 'u32'
        self.series = 'u32'
        self.sort_id = 'u32'
        self.model_id = 'u32'
        self.rare_type = 'u8'
        self.base_value = 'u32'
        self.sexual_equipable = 'u32'
        self.symbol_color_flag_list = ['u8', 'u16'] # Length of list is encodes in u16 (or u8?), not the usual u32
        self.is_one_set = 'u8'
    def human_readable(self):
        self.id = enum_PlOverwearId(self.id)
        self.is_valid = bool(self.is_valid)
        self.relative_id = enum_PlArmorId(self.relative_id)
        self.series = newtype_PlArmorSeriesTypes(self.series)
        self.rare_type = newtype_RareTypes(self.rare_type)
        self.sexual_equipable = enum_SexualEquipableFlag(self.sexual_equipable)
        self.symbol_color_flag_list = [bool(i) for i in self.symbol_color_flag_list]
        self.is_one_set = bool(self.is_one_set)

class PlOverwearBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['PlOverwearBaseUserDataParam']

class PlOverwearProductUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.item_flag = 'u32'
        self.enemy_flag = 'u32'
        self.progress_flag = 'u32'
        self.hr_limit_flag = 'u8'
        self.item = ['u32']
        self.item_num = ['u32']
        self.material_category = 'u32'
        self.material_category_num = 'u32'
        self.is_one_set = 'u8'
    def human_readable(self):
        self.id = enum_PlOverwearId(self.id)
        self.item_flag = enum_ItemId(self.item_flag)
        self.enemy_flag = enum_EmTypes(self.enemy_flag)
        self.progress_flag = utils.u32_to_i32(self.progress_flag)
        self.hr_limit_flag = bool(self.hr_limit_flag)
        self.item = [enum_ItemId(i) for i in self.item]
        self.material_category = newtype_MaterialCategory(self.material_category)
        self.is_one_set = bool(self.is_one_set)

class PlOverwearProductUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['PlOverwearProductUserDataParam']
