from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice skill.rs
# Classes for skill and decoration data

class PlEquipSkillBaseUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.max_level = 'u32'
        self.icon_color = 'u32'
        self.worth_point_list = 'u32'
    def human_readable(self):
        self.id = enum_PlEquipSkillId(self.id)
        if self.max_level > 0x7FFFFFFF: self.max_level -= (0xFFFFFFFF + 1)
        if self.icon_color > 0x7FFFFFFF: self.icon_color -= (0xFFFFFFFF + 1)

class PlEquipSkillBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['PlEquipSkillBaseUserDataParam']

class PlHyakuryuSkillBaseUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.item_color = 'u32'
        self.apply_rule = 'u32'
        self.add_atk = 'u8'
        self.add_def_list = ['u8']
        self.add_critical_rate_list = ['u8'] # No padding after this list
        self.add_main_element_val = 'u8'
        self.add_sub_element_val = 'u8'
        self.add_bottle_element_val = 'u8'
        self.add_insect_lv = 'u8'
        self.add_recoil = 'u8'
        self.add_reload = 'u8'
        self.add_fluctuation = 'u8'
        self.add_bullet_type_list = ['u32']
        self.add_lb_bullet_num_list = ['u8']
        self.add_hb_bullet_num_list = ['u8']
        self.add_rapid_shot_list = ['u32']
        self.add_build_up_bottle_type = 'u32'
        self.overwrite_flag_list = ['u8']
        self.overwrite_main_element_type = 'u32'
        self.overwrite_main_element_val = 'u8'
        self.overwrite_sub_element_type = 'u32'
        self.overwrite_sub_element_val = 'u8'
        self.overwrite_sharpness_val_list = ['u32']
        self.overwrite_takumi_val_list = ['u32']
        self.overwrite_gl_fire_type = 'u32'
        self.overwrite_gl_fire_lv = 'u32'
        self.overwrite_concert_id_list = ['u32']
        self.overwrite_caxe_bottle_type = 'u32'
        self.overwrite_saxe_bottle_type = 'u32'
        self.overwrite_insect_lv = 'u32'
        self.overwrite_hb_unique_bullet = 'u32'
        self.overwrite_charge_type_list = ['u32']
        self.overwrite_charge_start_lv = 'u32'
        self.overwrite_curve_types = 'u32'
        self.overwrite_bottle_equip_flag = 'u32'
    def human_readable(self):
        self.id = enum_PlHyakuryuSkillId(self.id)
        if self.item_color > 0x7FFFFFFF: self.item_color -= (0xFFFFFFFF + 1)
        self.apply_rule = enum_ApplyRules(self.apply_rule)
        if self.add_atk > 0x7F: self.add_atk -= (0xFF + 1)
        self.add_def_list = [i-(0xFF + 1) if i > 0x7F else i for i in self.add_def_list]
        self.add_critical_rate_list = [i-(0xFF + 1) if i > 0x7F else i for i in self.add_critical_rate_list]
        if self.add_main_element_val > 0x7F: self.add_main_element_val -= (0xFF + 1)
        if self.add_sub_element_val > 0x7F: self.add_sub_element_val -= (0xFF + 1)
        if self.add_bottle_element_val > 0x7F: self.add_bottle_element_val -= (0xFF + 1)
        if self.add_insect_lv > 0x7F: self.add_insect_lv -= (0xFF + 1)
        if self.add_recoil > 0x7F: self.add_recoil -= (0xFF + 1)
        if self.add_reload > 0x7F: self.add_reload -= (0xFF + 1)
        if self.add_fluctuation > 0x7F: self.add_fluctuation -= (0xFF + 1)
        self.add_bullet_type_list = [enum_BulletType(i) for i in self.add_bullet_type_list]
        self.add_lb_bullet_num_list = [i-(0xFF + 1) if i > 0x7F else i for i in self.add_lb_bullet_num_list]
        self.add_hb_bullet_num_list = [i-(0xFF + 1) if i > 0x7F else i for i in self.add_hb_bullet_num_list]
        self.add_rapid_shot_list = [enum_BulletType(i) for i in self.add_rapid_shot_list]
        self.add_build_up_bottle_type = enum_BottlePowerUpTypes(self.add_build_up_bottle_type)
        self.overwrite_flag_list = [bool(i) for i in self.overwrite_flag_list]
        self.overwrite_main_element_type = enum_ElementType(self.overwrite_main_element_type)
        self.overwrite_sub_element_type = enum_ElementType(self.overwrite_sub_element_type)
        self.overwrite_sharpness_val_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.overwrite_sharpness_val_list]
        self.overwrite_takumi_val_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.overwrite_takumi_val_list]
        self.overwrite_gl_fire_type = enum_GunLanceFireType(self.overwrite_gl_fire_type)
        if self.overwrite_gl_fire_lv > 0x7FFFFFFF: self.overwrite_gl_fire_lv -= (0xFFFFFFFF + 1)
        self.overwrite_concert_id_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.overwrite_concert_id_list]
        self.overwrite_caxe_bottle_type = enum_ChargeAxeBottleTypes(self.overwrite_caxe_bottle_type)
        self.overwrite_saxe_bottle_type = enum_SlashAxeBottleTypes(self.overwrite_saxe_bottle_type)
        if self.overwrite_insect_lv > 0x7FFFFFFF: self.overwrite_insect_lv -= (0xFFFFFFFF + 1)
        self.overwrite_hb_unique_bullet = enum_UniqueBulletType(self.overwrite_hb_unique_bullet)
        self.overwrite_charge_type_list = [enum_BowChargeTypes(i) for i in self.overwrite_charge_type_list]
        if self.overwrite_charge_start_lv > 0x7FFFFFFF: self.overwrite_charge_start_lv -= (0xFFFFFFFF + 1)
        if self.overwrite_curve_types > 0x7FFFFFFF: self.overwrite_curve_types -= (0xFFFFFFFF + 1)
        self.overwrite_bottle_equip_flag = enum_BowBottleTypes(self.overwrite_bottle_equip_flag)

class PlHyakuryuSkillBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['PlHyakuryuSkillBaseUserDataParam']

class PlHyakuryuSkillRecipeUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.recipe_no = 'u32'
        self.skill_id = 'u32'
        self.cost = 'u32'
        self.recipe_item_id_list = ['u32']
        self.recipe_item_num_list = ['u32']
    def human_readable(self):
        self.skill_id = enum_PlHyakuryuSkillId(self.skill_id)
        self.recipe_item_id_list = [enum_ItemId(i) for i in self.recipe_item_id_list]

class PlHyakuryuSkillRecipeUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['PlHyakuryuSkillRecipeUserDataParam']

class DecorationsBaseUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.sort_id = 'u32'
        self.rare = 'u8'
        self.icon_color = 'u32'
        self.decoration_lv = 'u32'
        self.skill_id_list = ['u32']
        self.skill_lv_list = ['u32']
        self.base_price = 'u32'
    def human_readable(self):
        self.id = enum_DecorationsId(self.id)
        self.rare += 1
        if self.icon_color > 0x7FFFFFFF: self.icon_color -= (0xFFFFFFFF + 1)
        if self.decoration_lv > 0x7FFFFFFF: self.decoration_lv -= (0xFFFFFFFF + 1)
        self.skill_id_list = [enum_PlEquipSkillId(i) for i in self.skill_id_list]
        self.skill_lv_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.skill_lv_list]

class DecorationsBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['DecorationsBaseUserDataParam']

class DecorationsProductUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.item_flag = 'u32'
        self.enemy_flag = 'u32'
        self.progress_flag = 'u32'
        self.item_id_list = ['u32']
        self.item_num_list = ['u32']
    def human_readable(self):
        self.id = enum_DecorationsId(self.id)
        self.item_flag = enum_ItemId(self.item_flag)
        self.enemy_flag = enum_EmTypes(self.enemy_flag)
        if self.progress_flag > 0x7FFFFFFF: self.progress_flag -= (0xFFFFFFFF + 1)
        self.item_id_list = [enum_ItemId(i) for i in self.item_id_list]

class DecorationsProductUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['DecorationsProductUserDataParam']
