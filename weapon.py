from bitstring import BitStream
from utils import OrderedAttibuteClass
from enums import *
import user
import msg
import utils

# This correspondes to MHRice weapon.rs
# Classes for weapon data

class WeaponBaseData(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.sort_id = 'u32'
        self.rare_type = 'u8' # Starts from 0
        self.model_id = 'u32'
        self.base_val = 'u32'
        self.buy_val = 'u32'
    def human_readable(self):
        self.id = enum_WeaponId(self.id)
        self.rare_type = newtype_RareTypes(self.rare_type) # Now starts from 1

class MainWeaponBaseData(WeaponBaseData):
    def __init__(self):
        super().__init__()
        self.atk = 'u32'
        self.critical_rate = 'u32'
        self.def_bonus = 'u32'
        self.hyakuryu_skill_id_list = ['u32'] # Starts from 1
        self.slot_num_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.atk = utils.u32_to_i32(self.atk)
        self.critical_rate = utils.u32_to_i32(self.critical_rate)
        self.def_bonus = utils.u32_to_i32(self.def_bonus)
        self.hyakuryu_skill_id_list = [enum_PlHyakuryuSkillId(i) for i in self.hyakuryu_skill_id_list] # Now starts from 0

class ElementWeaponBaseData(MainWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.main_element_type = 'u32'
        self.main_element_val = 'u32'
    def human_readable(self):
        super().human_readable()
        self.main_element_type = enum_PlWeaponElementTypes(self.main_element_type)
        self.main_element_val = utils.u32_to_i32(self.main_element_val)

class CloseRangeWeaponBaseData(ElementWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.sharpness_val_list = ['u32']
        self.takumi_val_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.sharpness_val_list = [utils.u32_to_i32(i) for i in self.sharpness_val_list]
        self.takumi_val_list = [utils.u32_to_i32(i) for i in self.takumi_val_list]

class GreatSwordBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class GreatSwordBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['GreatSwordBaseUserDataParam']

class ShortSwordBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class ShortSwordBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ShortSwordBaseUserDataParam']

class HammerBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class HammerBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['HammerBaseUserDataParam']

class LanceBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class LanceBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['LanceBaseUserDataParam']

class LongSwordBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class LongSwordBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['LongSwordBaseUserDataParam']

class SlashAxeBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.slash_axe_bottle_type = 'u32'
        self.slash_axe_bottle_element_val = 'u32'
    def human_readable(self):
        super().human_readable()
        self.slash_axe_bottle_type = enum_SlashAxeBottleTypes(self.slash_axe_bottle_type)
        self.slash_axe_bottle_element_val = utils.u32_to_i32(self.slash_axe_bottle_element_val)

class SlashAxeBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['SlashAxeBaseUserDataParam']

class GunLanceBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.gun_lance_fire_type = 'u32'
        self.gun_lance_fire_lv = 'u32'
    def human_readable(self):
        super().human_readable()
        self.gun_lance_fire_type = enum_GunLanceFireType(self.gun_lance_fire_type)
        self.gun_lance_fire_lv = newtype_GunLanceFireLv(self.gun_lance_fire_lv)

class GunLanceBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['GunLanceBaseUserDataParam']

class DualBladesBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.sub_element_type = 'u32'
        self.sub_element_val = 'u32'
    def human_readable(self):
        super().human_readable()
        self.sub_element_type = enum_PlWeaponElementTypes(self.sub_element_type)
        self.sub_element_val = utils.u32_to_i32(self.sub_element_val)

class DualBladesBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['DualBladesBaseUserDataParam']

class HornBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.horn_melody_type_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.horn_melody_type_list = [utils.u32_to_i32(i) for i in self.horn_melody_type_list]

class HornBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['HornBaseUserDataParam']

class InsectGlaiveBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.insect_glaive_insect_lv = 'u32'
    def human_readable(self):
        super().human_readable()
        self.insect_glaive_insect_lv = newtype_InsectLevelTypes(self.insect_glaive_insect_lv)

class InsectGlaiveBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['InsectGlaiveBaseUserDataParam']

class ChargeAxeBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.charge_axe_bottle_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.charge_axe_bottle_type = enum_ChargeAxeBottleTypes(self.charge_axe_bottle_type)

class ChargeAxeBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ChargeAxeBaseUserDataParam']

class BulletWeaponBaseUserDataParam(MainWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.fluctuation = 'u32'
        self.reload = 'u32'
        self.recoil = 'u32'
        self.kakusan_type = 'u32'
        self.bullet_equip_flag_list = ['u8']
        self.bullet_num_list = ['u32']
        self.bullet_type_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.fluctuation = enum_Fluctuation(self.fluctuation)
        self.reload = utils.u32_to_i32(self.reload)
        self.recoil = utils.u32_to_i32(self.recoil)
        self.kakusan_type = enum_KakusanType(self.kakusan_type)
        self.bullet_equip_flag_list = [bool(i) for i in self.bullet_equip_flag_list]
        self.bullet_type_list = [enum_ShootType(i) for i in self.bullet_type_list]

class LightBowgunBaseUserDataParam(BulletWeaponBaseUserDataParam):
    def __init__(self):
        super().__init__()
        self.rapid_shot_list = ['u32']
        self.unique_bullet = 'u32'
    def human_readable(self):
        super().human_readable()
        self.rapid_shot_list = [enum_BulletType(i) for i in self.rapid_shot_list]
        self.unique_bullet = enum_BulletType(self.unique_bullet)

class LightBowgunBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['LightBowgunBaseUserDataParam']

class HeavyBowgunBaseUserDataParam(BulletWeaponBaseUserDataParam):
    def __init__(self):
        super().__init__()
        self.heavy_bowgun_unique_bullet_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.heavy_bowgun_unique_bullet_type = enum_UniqueBulletType(self.heavy_bowgun_unique_bullet_type)

class HeavyBowgunBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['HeavyBowgunBaseUserDataParam']

class BowBaseUserDataParam(ElementWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.bow_bottle_power_up_type_list = ['u32']
        self.bow_bottle_equip_flag_list = ['u8']
        self.bow_default_charge_lv_limit = 'u32'
        self.bow_charge_type_list = ['u32']
        self.bow_curve_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.bow_bottle_power_up_type_list = [enum_BottlePowerUpTypes(i) for i in self.bow_bottle_power_up_type_list]
        self.bow_bottle_equip_flag_list = [bool(i) for i in self.bow_bottle_equip_flag_list]
        self.bow_default_charge_lv_limit = newtype_BowChargeStartLvTypes(self.bow_default_charge_lv_limit)
        self.bow_charge_type_list = [enum_BowChargeTypes(i) for i in self.bow_charge_type_list]
        self.bow_curve_type = utils.u32_to_i32(self.bow_curve_type)

class BowBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['BowBaseUserDataParam']

class WeaponCraftingData(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.item_flag = 'u32'
        self.enemy_flag = 'u32'
        self.progress_flag = 'u32'
        self.item = ['u32']
        self.item_num = ['u32']
        self.material_category = 'u32'
        self.material_category_num = 'u32'
    def human_readable(self):
        self.id = enum_WeaponId(self.id)
        self.item_flag = enum_ItemId(self.item_flag)
        self.enemy_flag = enum_EmTypes(self.enemy_flag)
        self.progress_flag = utils.u32_to_i32(self.progress_flag)
        self.item = [enum_ItemId(i) for i in self.item]
        self.material_category = newtype_MaterialCategory(self.material_category)

class WeaponProcessUserDataParam(WeaponCraftingData):
    def __init__(self):
        super().__init__()
        self.output_item = ['u32']
        self.output_item_num = ['u32']
    def human_readable(self):
        super().human_readable()
        self.output_item = [enum_ItemId(i) for i in self.output_item]

class WeaponProcessUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['WeaponProcessUserDataParam']

class WeaponProductUserDataParam(WeaponCraftingData):
    def __init__(self):
        super().__init__()
        self.output_item = ['u32']
        self.output_item_num = ['u32']
    def human_readable(self):
        super().human_readable()
        self.output_item = [enum_ItemId(i) for i in self.output_item]

class WeaponProductUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['WeaponProductUserDataParam']

class WeaponChangeUserDataParam(WeaponCraftingData):
    def __init__(self):
        super().__init__()
    def human_readable(self):
        super().human_readable()

class WeaponChangeUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['WeaponChangeUserDataParam']

class WeaponUpdateTreeUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.tree_type = 'u32'
        self.index = 'u32'
        self.village_progress = 'u32'
        self.hall_progress = 'u32'
        self.weapon_id = 'u32'
        self.next_weapon_type_list = ['u32']
        self.next_weapon_index_list = ['u32']
        self.prev_weapon_type = 'u32'
        self.prev_weapon_index = 'u32'
    def human_readable(self):
        self.tree_type = enum_TreeType(self.tree_type)
        self.index = utils.u32_to_i32(self.index)
        self.village_progress = enum_VillageProgress(self.village_progress)
        self.hall_progress = enum_HallProgress(self.hall_progress)
        self.weapon_id = enum_WeaponId(self.weapon_id)
        self.next_weapon_type_list = [enum_TreeType(i) for i in self.next_weapon_type_list]
        self.next_weapon_index_list = [utils.u32_to_i32(i) for i in self.next_weapon_index_list]
        self.prev_weapon_type = enum_TreeType(self.prev_weapon_type)
        self.prev_weapon_index = utils.u32_to_i32(self.prev_weapon_index)

class WeaponUpdateTreeUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['WeaponUpdateTreeUserDataParam']

class WeaponList(OrderedAttibuteClass):
    def __init__(self, weapon_type): # e.g. weapon_type = 'GreatSword'
        self.weapon_type = weapon_type
        self.get_base_data()
        self.get_product()
        self.get_change()
        self.get_process()
        self.get_tree()
        self.get_name()
        self.get_explain()

    def get_base_data(self):
        filename = 'user\\weapon\\{}\\{}BaseData.user.2'.format(self.weapon_type, self.weapon_type)
        self.base_data = user.read_user_file(filename)

    def get_product(self):
        filename = 'user\\weapon\\{}\\{}ProductData.user.2'.format(self.weapon_type, self.weapon_type)
        self.product = user.read_user_file(filename)

    def get_change(self):
        filename = 'user\\weapon\\{}\\{}ChangeData.user.2'.format(self.weapon_type, self.weapon_type)
        self.change = user.read_user_file(filename)

    def get_process(self):
        filename = 'user\\weapon\\{}\\{}ProcessData.user.2'.format(self.weapon_type, self.weapon_type)
        self.process = user.read_user_file(filename)

    def get_tree(self):
        filename = 'user\\weapon\\{}\\{}UpdateTreeData.user.2'.format(self.weapon_type, self.weapon_type)
        self.tree = user.read_user_file(filename)

    def get_name(self):
        filename = 'msg\\{}_Name.msg.17'.format(self.weapon_type)
        self.name = msg.read_msg_file(filename)

    def get_explain(self):
        filename = 'msg\\{}_Explain.msg.17'.format(self.weapon_type)
        self.explain = msg.read_msg_file(filename)

if __name__ == '__main__':
    weapon_type_list = ['GreatSword', 'ShortSword', 'Hammer', 'Lance', 'LongSword', 'SlashAxe', 'GunLance',\
                        'DualBlades', 'Horn', 'InsectGlaive', 'ChargeAxe', 'LightBowgun', 'HeavyBowgun', 'Bow']
    weapon_type = weapon_type_list[0]
    weapon = WeaponList(weapon_type)
    utils.print_hierarchical_object(weapon)
