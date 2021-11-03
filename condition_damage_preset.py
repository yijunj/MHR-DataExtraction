from utils import OrderedAttibuteClass
from enums import *
from monster_condition_damage_data import *
import utils

# This correspondes to MHRice condition_damage_preset.rs
# Classes for monster condition preset data

class PresetParalyzeData(ParalyzeDamageData):
    def __init__(self):
        super().__init__()

class PresetSleepData(SleepDamageData):
    def __init__(self):
        super().__init__()

class PresetStunData(StunDamageData):
    def __init__(self):
        super().__init__()

class PresetStaminaData(StaminaDamageData):
    def __init__(self):
        super().__init__()

class PresetFlashData(FlashDamageData):
    def __init__(self):
        super().__init__()

class PresetPoison(PoisonDamageData):
    def __init__(self):
        super().__init__()

class PresetBlastData(BlastDamageData):
    def __init__(self):
        super().__init__()

class PresetWater(WaterDamageData):
    def __init__(self):
        super().__init__()

class PresetFireData(FireDamageData):
    def __init__(self):
        super().__init__()

class PresetIceData(IceDamageData):
    def __init__(self):
        super().__init__()

class PresetThunderData(ThunderDamageData):
    def __init__(self):
        super().__init__()

class PresetFallTrapData(FallTrapDamageData):
    def __init__(self):
        super().__init__()

class PresetFallQuickSandData(FallQuickSandDamageData):
    def __init__(self):
        super().__init__()

class PresetFallOtomoTrapData(FallOtomoTrapDamageData):
    def __init__(self):
        super().__init__()

class PresetShockTrapData(ShockTrapDamageData):
    def __init__(self):
        super().__init__()

class PresetShockOtomoTrapData(ShockTrapDamageData):
    def __init__(self):
        super().__init__()

class PresetCaptureData(CaptureDamageData):
    def __init__(self):
        super().__init__()

class PresetKoyashiData(KoyashiDamageData):
    def __init__(self):
        super().__init__()

class PresetSteelFangData(SteelFangData):
    def __init__(self):
        super().__init__()

class EnemyConditionPresetData(OrderedAttibuteClass):
    def __init__(self):
        self.paralyze_data = ['PresetParalyzeData']
        self.sleep_data = ['PresetSleepData']
        self.stun_data = ['PresetStunData']
        self.flash_data = ['PresetFlashData']
        self.blast_data = ['PresetBlastData']
        self.stamina_data = ['PresetStaminaData']
        self.poison_data = ['PresetPoison']
        self.fire_data = ['PresetFireData']
        self.water_data = ['PresetWater']
        self.ice_data = ['PresetIceData']
        self.thunder_data = ['PresetThunderData']
        self.fall_trap_data = ['PresetFallTrapData']
        self.fall_quick_sand_data = ['PresetFallQuickSandData']
        self.fall_otomo_trap_data = ['PresetFallOtomoTrapData']
        self.shock_trap_data = ['PresetShockTrapData']
        self.shock_otomo_trap_data = ['PresetShockOtomoTrapData']
        self.capture_data = ['PresetCaptureData']
        self.koyashi_data = ['PresetKoyashiData']
        self.steel_fang_data = ['PresetSteelFangData']
