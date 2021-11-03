from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to MHRice condition_damage_data.rs
# Classes for monster condition data, which will become part of Monster class

class StockData(OrderedAttibuteClass):
    def __init__(self):
        self.default_limit = 'u32'
        self.add_limit = 'u32'
        self.max_limit = 'u32'
        self.sub_value = 'u32'
        self.sub_interval = 'u32'
    def human_readable(self):
        self.default_limit = utils.hex_to_f32(hex(self.default_limit)[2:])
        self.add_limit = utils.hex_to_f32(hex(self.add_limit)[2:])
        self.max_limit = utils.hex_to_f32(hex(self.max_limit)[2:])
        self.sub_value = utils.hex_to_f32(hex(self.sub_value)[2:])
        self.sub_interval = utils.hex_to_f32(hex(self.sub_interval)[2:])

class ConditionDamageDataBase(OrderedAttibuteClass):
    def __init__(self):
        self.default_stock = 'StockData'
        self.ride_stock = 'StockData'
        self.max_stock = 'u32'
        self.active_time = 'u32'
        self.sub_active_time = 'u32'
        self.min_active_time = 'u32'
        self.add_tired_time = 'u32'
        self.damage_interval = 'u32'
        self.damage = 'u32'
    def human_readable(self):
        self.max_stock = utils.hex_to_f32(hex(self.max_stock)[2:])
        self.active_time = utils.hex_to_f32(hex(self.active_time)[2:])
        self.sub_active_time = utils.hex_to_f32(hex(self.sub_active_time)[2:])
        self.min_active_time = utils.hex_to_f32(hex(self.min_active_time)[2:])
        self.add_tired_time = utils.hex_to_f32(hex(self.add_tired_time)[2:])
        self.damage_interval = utils.hex_to_f32(hex(self.damage_interval)[2:])
        self.damage = utils.hex_to_f32(hex(self.damage)[2:])

class ParalyzeDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class SleepDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class StunDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class StaminaDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.sub_stamina = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.sub_stamina = utils.hex_to_f32(hex(self.sub_stamina)[2:])

class FlashDamageLvData(OrderedAttibuteClass):
    def __init__(self):
        self.active_count = 'u32'
        self.active_time = 'u32'
    def human_readable(self):
        if self.active_count > 0x7FFFFFFF: self.active_count -= (0xFFFFFFFF + 1)
        self.active_time = utils.hex_to_f32(hex(self.active_time)[2:])

class FlashDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.damage_lvs = ['FlashDamageLvData']
        self.ignore_refresh_stance = 'u32'
        self.max_distance = 'u32'
        self.min_distance = 'u32'
        self.angle = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.ignore_refresh_stance = enum_StanceStatusFlags(self.ignore_refresh_stance)
        self.max_distance = utils.hex_to_f32(hex(self.max_distance)[2:])
        self.min_distance = utils.hex_to_f32(hex(self.min_distance)[2:])
        self.angle = utils.hex_to_f32(hex(self.angle)[2:])

class PoisonDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class BlastDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.blast_damage = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.blast_damage = utils.hex_to_f32(hex(self.blast_damage)[2:])

class MarionetteStartDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.use_data = 'u32'
        self.nora_first_limit = 'u32'
    def human_readable(self):
        super().human_readable()
        self.use_data = enum_UseDataType(self.use_data)
        self.nora_first_limit = utils.hex_to_f32(hex(self.nora_first_limit)[2:])

class AdjustMeatDownData(OrderedAttibuteClass):
    def __init__(self):
        self.hard_meat_adjust_value = 'u32'
        self.soft_meat_adjust_value = 'u32'
        self.judge_meat_value = 'u32'
    def human_readable(self):
        self.hard_meat_adjust_value = utils.hex_to_f32(hex(self.hard_meat_adjust_value)[2:])
        self.soft_meat_adjust_value = utils.hex_to_f32(hex(self.soft_meat_adjust_value)[2:])
        self.judge_meat_value = utils.hex_to_f32(hex(self.judge_meat_value)[2:])

class WaterDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.slash_strike_adjust = 'AdjustMeatDownData'
        self.shell_adjust = 'AdjustMeatDownData'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class FireDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.hit_damage_rate = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.hit_damage_rate = utils.hex_to_f32(hex(self.hit_damage_rate)[2:])

class IceDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.motion_speed_rate = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.motion_speed_rate = utils.hex_to_f32(hex(self.motion_speed_rate)[2:])

class ThunderAdjustParamData(OrderedAttibuteClass):
    def __init__(self):
        self.hit_damage_to_stun_rate = 'u32'
        self.hit_damage_to_stun_max = 'u32'
        self.hit_damage_to_stun_min = 'u32'
        self.default_stun_damage_rate = 'u32'
    def human_readable(self):
        self.hit_damage_to_stun_rate = utils.hex_to_f32(hex(self.hit_damage_to_stun_rate)[2:])
        self.hit_damage_to_stun_max = utils.hex_to_f32(hex(self.hit_damage_to_stun_max)[2:])
        self.hit_damage_to_stun_min = utils.hex_to_f32(hex(self.hit_damage_to_stun_min)[2:])
        self.default_stun_damage_rate = utils.hex_to_f32(hex(self.default_stun_damage_rate)[2:])

class ThunderDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.stun_meat_adjust = 'ThunderAdjustParamData'
        self.normal_meat_adjust = 'ThunderAdjustParamData'
        self.stun_active_limit = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        if self.stun_active_limit > 0x7FFFFFFF: self.stun_active_limit -= (0xFFFFFFFF + 1)

class FallTrapDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.render_offset_y = 'u32'
        self.render_offset_speed = 'u32'
        self.render_offset_reset_time = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.render_offset_y = utils.hex_to_f32(hex(self.render_offset_y)[2:])
        self.render_offset_speed = utils.hex_to_f32(hex(self.render_offset_speed)[2:])
        self.render_offset_reset_time = utils.hex_to_f32(hex(self.render_offset_reset_time)[2:])

class FallQuickSandDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.render_offset_y = 'u32'
        self.render_offset_speed = 'u32'
        self.render_offset_reset_time = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.render_offset_y = utils.hex_to_f32(hex(self.render_offset_y)[2:])
        self.render_offset_speed = utils.hex_to_f32(hex(self.render_offset_speed)[2:])
        self.render_offset_reset_time = utils.hex_to_f32(hex(self.render_offset_reset_time)[2:])

class FallOtomoTrapDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.already_poison_stock_value = 'u32'
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()
        self.already_poison_stock_value = utils.hex_to_f32(hex(self.already_poison_stock_value)[2:])

class ShockTrapDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class CaptureDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class KoyashiDamageData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.preset_type = 'u32'
    def human_readable(self):
        super().human_readable()

class SteelFangData(ConditionDamageDataBase):
    def __init__(self):
        super().__init__()
        self.active_limit_count = 'u32'
        self.preset_type = 'u32'
        self.is_unique_target_param = 'u32'
        self.max_distance = 'u32'
        self.min_distance = 'u32'
        self.angle = 'u32'
    def human_readable(self):
        super().human_readable()
        if self.active_limit_count > 0x7FFFFFFF: self.active_limit_count -= (0xFFFFFFFF + 1)
        self.max_distance = utils.hex_to_f32(hex(self.max_distance)[2:])
        self.min_distance = utils.hex_to_f32(hex(self.min_distance)[2:])
        self.angle = utils.hex_to_f32(hex(self.angle)[2:])

class EnemyConditionDamageData(OrderedAttibuteClass):
    def __init__(self):
        self.paralyze_data = 'ParalyzeDamageData'
        self.sleep_data = 'SleepDamageData'
        self.stun_data = 'StunDamageData'
        self.stamina_data = 'StaminaDamageData'
        self.flash_data = 'FlashDamageData'
        self.poison_data = 'PoisonDamageData'
        self.blast_data = 'BlastDamageData'
        self.marionette_data = 'MarionetteStartDamageData'
        self.water_data = 'WaterDamageData'
        self.fire_data = 'FireDamageData'
        self.ice_data = 'IceDamageData'
        self.thunder_data = 'ThunderDamageData'
        self.fall_trap_data = 'FallTrapDamageData'
        self.fall_quick_sand_data = 'FallQuickSandDamageData'
        self.fall_otomo_trap_data = 'FallOtomoTrapDamageData'
        self.shock_trap_data = 'ShockTrapDamageData'
        self.shock_otomo_trap_data = 'ShockTrapDamageData'
        self.capture_data = 'CaptureDamageData'
        self.koyashi_data = 'KoyashiDamageData'
        self.steel_fang_data = 'SteelFangData'
        self.use_paralyze = 'u8'
        self.use_sleep = 'u8'
        self.use_stun = 'u8'
        self.use_stamina = 'u8'
        self.use_flash = 'u8'
        self.use_poison = 'u8'
        self.use_blast = 'u8'
        self.use_ride = 'u8'
        self.use_water = 'u8'
        self.use_fire = 'u8'
        self.use_ice = 'u8'
        self.use_thunder = 'u8'
        self.use_fall_trap = 'u8'
        self.use_fall_quick_sand = 'u8'
        self.use_fall_otomo_trap = 'u8'
        self.use_shock_trap = 'u8'
        self.use_shock_otomo_trap = 'u8'
        self.use_capture = 'u8'
        self.use_dung = 'u8'
        self.use_steel_fang = 'u8'
    def human_readable(self):
        self.use_paralyze = enum_ConditionDamageDataUsed(self.use_paralyze)
        self.use_sleep = enum_ConditionDamageDataUsed(self.use_sleep)
        self.use_stun = enum_ConditionDamageDataUsed(self.use_stun)
        self.use_stamina = enum_ConditionDamageDataUsed(self.use_stamina)
        self.use_flash = enum_ConditionDamageDataUsed(self.use_flash)
        self.use_poison = enum_ConditionDamageDataUsed(self.use_poison)
        self.use_blast = enum_ConditionDamageDataUsed(self.use_blast)
        self.use_ride = enum_ConditionDamageDataUsed(self.use_ride)
        self.use_water = enum_ConditionDamageDataUsed(self.use_water)
        self.use_fire = enum_ConditionDamageDataUsed(self.use_fire)
        self.use_ice = enum_ConditionDamageDataUsed(self.use_ice)
        self.use_thunder = enum_ConditionDamageDataUsed(self.use_thunder)
        self.use_fall_trap = enum_ConditionDamageDataUsed(self.use_fall_trap)
        self.use_fall_quick_sand = enum_ConditionDamageDataUsed(self.use_fall_quick_sand)
        self.use_fall_otomo_trap = enum_ConditionDamageDataUsed(self.use_fall_otomo_trap)
        self.use_shock_trap = enum_ConditionDamageDataUsed(self.use_shock_trap)
        self.use_shock_otomo_trap = enum_ConditionDamageDataUsed(self.use_shock_otomo_trap)
        self.use_capture = enum_ConditionDamageDataUsed(self.use_capture)
        self.use_dung = enum_ConditionDamageDataUsed(self.use_dung)
        self.use_steel_fang = enum_ConditionDamageDataUsed(self.use_steel_fang)
