from bitstring import BitStream
from utils import OrderedAttibuteClass
from enums import *
import user

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
        self.rare_type += 1 # Now starts from 1

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
        if self.atk > 0x7FFFFFFF: self.atk -= (0xFFFFFFFF + 1)
        if self.critical_rate > 0x7FFFFFFF: self.critical_rate -= (0xFFFFFFFF + 1)
        if self.def_bonus > 0x7FFFFFFF: self.def_bonus -= (0xFFFFFFFF + 1)
        self.hyakuryu_skill_id_list = [enum_PlHyakuryuSkillId(i) for i in self.hyakuryu_skill_id_list] # Now starts from 0

class ElementWeaponBaseData(MainWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.main_element_type = 'u32'
        self.main_element_val = 'u32'
    def human_readable(self):
        super().human_readable()
        self.main_element_type = enum_PlWeaponElementTypes(self.main_element_type)
        if self.main_element_val > 0x7FFFFFFF: self.main_element_val -= (0xFFFFFFFF + 1)

class CloseRangeWeaponBaseData(ElementWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.sharpness_val_list = ['u32']
        self.takumi_val_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.sharpness_val_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.sharpness_val_list]
        self.takumi_val_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.takumi_val_list]

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
        if self.slash_axe_bottle_element_val > 0x7FFFFFFF: self.slash_axe_bottle_element_val -= (0xFFFFFFFF + 1)

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
        if self.gun_lance_fire_lv > 0x7FFFFFFF: self.gun_lance_fire_lv -= (0xFFFFFFFF + 1)
        self.gun_lance_fire_lv += 1

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
        if self.sub_element_val > 0x7FFFFFFF: self.sub_element_val -= (0xFFFFFFFF + 1)

class DualBladesBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['DualBladesBaseUserDataParam']

class HornBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.horn_melody_type_list = ['u32']
    def human_readable(self):
        super().human_readable()
        self.horn_melody_type_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.horn_melody_type_list]

class HornBaseUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['HornBaseUserDataParam']

class InsectGlaiveBaseUserDataParam(CloseRangeWeaponBaseData):
    def __init__(self):
        super().__init__()
        self.insect_glaive_insect_lv = 'u32'
    def human_readable(self):
        super().human_readable()
        if self.insect_glaive_insect_lv > 0x7FFFFFFF: self.insect_glaive_insect_lv -= (0xFFFFFFFF + 1)
        self.insect_glaive_insect_lv += 1

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
        if self.reload > 0x7FFFFFFF: self.reload -= (0xFFFFFFFF + 1)
        if self.recoil > 0x7FFFFFFF: self.recoil -= (0xFFFFFFFF + 1)
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
        if self.bow_default_charge_lv_limit > 0x7FFFFFFF: self.bow_default_charge_lv_limit -= (0xFFFFFFFF + 1)
        self.bow_default_charge_lv_limit += 1
        self.bow_charge_type_list = [enum_BowChargeTypes(i) for i in self.bow_charge_type_list]
        if self.bow_curve_type > 0x7FFFFFFF: self.bow_curve_type -= (0xFFFFFFFF + 1)

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
        if self.progress_flag > 0x7FFFFFFF: self.progress_flag -= (0xFFFFFFFF + 1)
        self.item = [enum_ItemId(i) for i in self.item]
        self.material_category = enum_MaterialCategory(self.material_category)

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
        if self.index > 0x7FFFFFFF: self.index -= (0xFFFFFFFF + 1)
        self.village_progress = enum_VillageProgress(self.village_progress)
        self.hall_progress = enum_HallProgress(self.hall_progress)
        self.weapon_id = enum_WeaponId(self.weapon_id)
        self.next_weapon_type_list = [enum_TreeType(i) for i in self.next_weapon_type_list]
        self.next_weapon_index_list = [i-(0xFFFFFFFF + 1) if i > 0x7FFFFFFF else i for i in self.next_weapon_index_list]
        self.prev_weapon_type = enum_TreeType(self.prev_weapon_type)
        if self.prev_weapon_index > 0x7FFFFFFF: self.prev_weapon_index -= (0xFFFFFFFF + 1)

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

    def get_base_data(self):
        data = BitStream(filename = 'user\\weapon\\{}\\{}BaseData.user.2'.format(self.weapon_type, self.weapon_type))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.base_data, _ = user.read_rsz(data_type_list, data)

    def get_product(self):
        data = BitStream(filename = 'user\\weapon\\{}\\{}ProductData.user.2'.format(self.weapon_type, self.weapon_type))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.product, _ = user.read_rsz(data_type_list, data)

    def get_change(self):
        data = BitStream(filename = 'user\\weapon\\{}\\{}ChangeData.user.2'.format(self.weapon_type, self.weapon_type))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.change, _ = user.read_rsz(data_type_list, data)

    def get_process(self):
        data = BitStream(filename = 'user\\weapon\\{}\\{}ProcessData.user.2'.format(self.weapon_type, self.weapon_type))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.process, _ = user.read_rsz(data_type_list, data)

    def get_tree(self):
        data = BitStream(filename = 'user\\weapon\\{}\\{}UpdateTreeData.user.2'.format(self.weapon_type, self.weapon_type))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.tree, _ = user.read_rsz(data_type_list, data)

if __name__ == '__main__':
    weapon_type_list = ['GreatSword', 'ShortSword', 'Hammer', 'Lance', 'LongSword', 'SlashAxe', 'GunLance',\
                        'DualBlades', 'Horn', 'InsectGlaive', 'ChargeAxe', 'LightBowgun', 'HeavyBowgun', 'Bow']
    weapon_type = weapon_type_list[0]
    weapon = WeaponList(weapon_type)
    user.print_hierarchical_object(weapon)
