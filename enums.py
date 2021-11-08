import utils

# This script contains MHRice rsz_enum!, rsz_newtype! and rsz_bitflags! macros, defined as Python functions
# They are used to cast data after they are read in

########################################
# These are listed in MHRice alchemy.rs
def enum_ColorTypes(type_id):
    type_list = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'White', 'Purple']
    return type_list[type_id]

def newtype_AlchemyPatturnTypes(type):
    return utils.u32_to_i32(type) + 1

def enum_GradeTypes(type_id):
    type_list = ['C', 'B', 'A', 'S']
    return type_list[type_id]

def enum_GradeTypesForSlotNumTable(type_id):
    type_list = ['C', 'B', 'A', 'S', None]
    return type_list[type_id]

########################################
# These are listed in MHRice armor.rs
def enum_PlArmorId(armor_id):
    armor_type_dict = {str(0x0C100000): 'Head',\
                        str(0x0C200000): 'Chest',\
                        str(0x0C300000): 'Arm',\
                        str(0x0C400000): 'Waist',\
                        str(0x0C500000): 'Leg'}
    if armor_id == 0:
        return 'TableNone'
    elif armor_id == 0x0C000000:
        return None
    elif armor_id == 0x00010001:
        return 'ChangedEx'
    else:
        true_id = armor_id & 0x0000FFFF
        armor_type = armor_id & 0xFFFF0000
        armor_type_str = armor_type_dict[str(armor_type)]
        return armor_type_str + '({})'.format(true_id)

def newtype_PlArmorSeriesTypes(type):
    return utils.u32_to_i32(type)

def enum_SexualEquipableFlag(type_id):
    type_list = ['MaleOnly', 'FemaleOnly', 'Both']
    return type_list[type_id]

def enum_EquipDifficultyGroup(type_id):
    type_list = ['Lower', 'Higher']
    return type_list[type_id]

def enum_PlOverwearId(overwear_id):
    overwear_type_dict = {str(0x0000): 'Head',\
                        str(0x1000): 'Chest',\
                        str(0x2000): 'Arm',\
                        str(0x3000): 'Waist',\
                        str(0x4000): 'Leg'}
    true_id = overwear_id & 0x0FFF
    overwear_type = overwear_id & 0xF000
    overwear_type_str = overwear_type_dict[str(overwear_type)]
    return overwear_type_str + '({})'.format(true_id)

########################################
# These are listed in MHRice collision.rs
def enum_CustomShapeType(type_id):
    type_list = [None, 'Cylinder', 'HoledCylinder', 'TrianglePole', 'Donuts', 'DonutsCylinder']
    return type_list[type_id]

def enum_LimitedHitAttr(type_id):
    type_list = [None, 'LimitedStan']
    return type_list[type_id]

def enum_HitSoundAttr(type_id):
    type_list = ['Default', 'Silence', 'Yarn', 'Em082BubbleBreakOnce', 'Em082OnibiBubbleBreakOnce',\
                'Em082BubbleBreakMultiple', 'Em082BubbleBreakMultipleLast', 'EnemyIndex036IceArm',\
                'EnemyIndex035FloatingRock', 'EnemyIndex038FloatingRock', 'EnemyIndex042CarryRock',\
                'EnemyIndex042CaryyPot', 'Max', 'Invalid']
    return type_list[type_id]

def bitflags_DamageAttr(key):
    flag_list = ['ALLOW_DISABLE', 'NO_BREAK_CONST_OBJECT', 'NO_BREAK_CONST_OBJECT_UNIQUE']
    return [flag_list[2-i] for i in reversed(range(3)) if '{0:3b}'.format(key)[i] == '1']

def enum_BaseHitMarkType(type_id):
    type_list = ['Normal', 'Moderate', 'Max', 'Invalid']
    return type_list[type_id]

########################################
# These are listed in MHRice common.rs
def bytes_Guid(text_bytes, bit_num):
    return [int(hex(text_bytes)[2*i+2:2*i+4], 16) for i in reversed(range(int(bit_num/8)))]

########################################
# These are listed in MHRice condition_damage_data.rs
def bitflags_StanceStatusFlags(key):
    flag_list = ['STAND', 'FLY', 'DIVING', 'WALL', 'CEILING']
    return [flag_list[4-i] for i in reversed(range(5)) if '{0:5b}'.format(key)[i] == '1']

def enum_UseDataType(type_id):
    type_list = ['Common', 'Unique']
    return type_list[type_id]

def enum_ConditionDamageDataUsed(type_id):
    type_list = ['Use', 'NotUse']
    return type_list[type_id]

########################################
# These are listed in MHRice data_tune.rs
def enum_ExtractiveType(type_id):
    type_list = ['Red', 'White', 'Orange', None]
    return type_list[type_id]

def enum_PartsBreakDataIgnoreCondition(type_id):
    type_list = [None, 'InTimes', 'Equal']
    return type_list[type_id]

def enum_PermitDamageAttrEnum(type_id):
    type_list = ['Slash', 'Strike', 'All']
    return type_list[type_id]

def bitflags_DamageCategoryFlag(key):
    flag_list = ['MARIONETTE_FRIENDLY_FIRE', 'MARIONETTE_START', 'DIVING', 'PARTS_LOSS', 'FALL_TRAP',\
                'SHOCK_TRAP', 'PARALYZE', 'SLEEP', 'STUN', 'MARIONETTE_L', 'FLASH', 'SOUND', 'GIMMICK_L',\
                'EM2_EM_L', 'GIMMICK_KNOCK_BACK', 'HIGH_PARTS', 'MARIONETTE_M', 'GIMMICK_M', 'EM2_EM_M',\
                'MULTI_PARTS', 'ELEMENT_WEAK', 'PARTS_BREAK', 'SLEEP_END', 'STAMINA', 'PARTS', 'MARIONETTE_S',\
                'GIMMICK_S', 'EM2_EM_S', 'STEEL_FANG']
    return [flag_list[27-i] for i in reversed(range(28)) if '{0:28b}'.format(key)[i] == '1']

def enum_HitWeight(type_id):
    type_list = ['PushedOnly', 'SSSS', 'SSS', 'SS', 'S', 'Normal', 'L', 'LL', 'LLL', 'LLLL', 'SpUse', 'NoMove']
    return type_list[type_id]

########################################
# These are listed in MHRice item.rs
def enum_CarriableFilter(type_id):
    type_list = ['All', 'Quest', 'Hyakuryu', 'Lobby']
    return type_list[type_id]

def enum_ItemTypes(type_id):
    type_list = ['Consume', 'Tool', 'Material', 'OffcutsMaterial', 'Bullet', 'Bottle',\
                'Present', 'PayOff', 'CarryPayoff', 'Carry', 'Judge', 'Antique']
    return type_list[type_id]

def enum_IconRank(type_id):
    type_list = [None, 'Great', 'Lv1', 'Lv2', 'Lv3']
    return type_list[type_id]

def enum_RankTypes(type_id):
    type_list = ['Low', 'Upper']
    return type_list[type_id]

def enum_ItemGroupTypes(type_id):
    type_list = ['Drink', 'Food', 'Others']
    return type_list[type_id]

def enum_ItemId(item_id):
    if item_id == 0:
        return 'Null'
    elif item_id == 0x04000000:
        return None
    elif item_id & 0xFFFF0000 == 0x04100000:
        return 'Normal({})'.format(item_id & 0x0000FFFF)
    else:
        return 'Ec({})'.format(item_id & 0x0000FFFF)

def newtype_RareTypes(type):
    return type + 1

def newtype_MaterialCategory(type):
    return utils.u32_to_i32(type)

########################################
# These are listed in MHRice lot.rs
def enum_QuestRank(type_id):
    type_list = ['Low', 'High']
    return type_list[type_id]

def enum_EnemyRewardPopTypes(type_id):
    type_list = [None, 'MainBody', 'PartsLoss1', 'PartsLoss2', 'DropItem1', 'DropItem2',\
                'DropItem3', 'DropItem4', 'DropItem5', 'DropItem6', 'Unique']
    return type_list[type_id]

def enum_BrokenPartsTypes(type_id):
    if type_id == 0:
        return None
    else:
        return type_id - 1

def enum_BreakLvTypes(type_id):
    type_list = [None, 'Lv1', 'Lv2', 'Lv3']
    return type_list[type_id]

def enum_EnemyPartsBreakRewardDataConditionType(type_id):
    type_list = ['All', 'Other']
    return type_list[type_id]

########################################
# These are listed in MHRice quest_data.rs
def bitflags_QuestType(key):
    flag_list = ['HUNTING', 'KILL', 'CAPTURE', 'BOSSRUSH', 'COLLECTS', 'TOUR', 'ARENA', 'SPECIAL', 'HYAKURYU', 'TRAINING']
    return [flag_list[9-i] for i in reversed(range(10)) if '{0:10b}'.format(key)[i] == '1']

def enum_QuestLevel(type_id):
    type_list = ['QL1', 'QL2', 'QL3', 'QL4', 'QL5', 'QL6', 'QL7', 'QL7Ex']
    return type_list[type_id]

def enum_EnemyLevel(type_id):
    type_list = ['Village', 'Low', 'High']
    return type_list[type_id]

def enum_QuestOrderType(type_id):
    type_list = [None, 'Under2', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H20', 'H30', 'H40', 'H50', 'H90', 'H100']
    return type_list[type_id]

def enum_QuestTargetType(type_id):
    type_list = [None, 'ItemGet', 'Hunting', 'Kill', 'Capture', 'AllMainEnemy', 'EmTotal', 'FinalBarrierDefense', 'FortLevelUp',\
                'PlayerDown', 'FinalBoss', 'HuntingMachine', 'DropItem', 'EmStun', 'EmElement', 'EmCondition', 'EmCntWeapon',\
                'EmCntHmBallista', 'EmCntHmCannon', 'EmCntHmGatling', 'EmCntHmTrap', 'EmCntHmFlameThrower', 'EmCntHmNpc',\
                'EmCntHmDragnator', 'ExtraEmRunaway']
    return type_list[type_id]

def enum_BossSetCondition(type_id):
    type_list = [None, 'Default', 'Free1', 'Free2', 'Free3', 'Timer1', 'Timer2', 'Em1Hp', 'Em2Hp', 'Em3Hp', 'Em4Hp', 'Em5Hp', 'HpEmx1',\
                'U13', 'U14', 'U15']
    # Comment in MHRice: TODO: this depends on version
    # U13: INIT_RANDOM (v6), HP_EMx2 (v7)
    # U14: SWAP_RANDOM (v6), INIT_RANDOM (v7)
    # U15: SWAP_RANDOM (v7)
    return type_list[type_id]

def enum_SwapSetCondition(type_id):
    type_list = [None, 'QuestTimer']
    return type_list[type_id]

def enum_SwapStopType(type_id):
    type_list = [None, 'LowerHp']
    if type_id > 1:
        print(type_id)
    return type_list[type_id]

def enum_SwapExecType(type_id):
    type_list = [None, 'FreeExtra']
    return type_list[type_id]

def enum_BattleBgmType(type_id):
    type_list = ['Default', 'SpBattle01']
    return type_list[type_id]

def enum_ClearBgmType(type_id):
    type_list = ['Default', 'SpClear01']
    return type_list[type_id]

def enum_EmTypes(enemy_id):
    enemy_type_dict = {str(0x0000): 'Em', str(0x1000): 'Ems'}
    true_id = enemy_id & 0x0FFF
    enemy_type = enemy_id & 0xF000
    enemy_type_str = enemy_type_dict[str(enemy_type)]
    return enemy_type_str + '({})'.format(true_id)

def enum_NandoYuragi(type_id):
    type_list = ['False', 'True1', 'True2']
    return type_list[type_id]

########################################
# These are listed in MHRice skill.rs
def enum_PlEquipSkillId(equip_skill_id):
    if equip_skill_id == 0:
        return None
    else:
        return equip_skill_id - 1 # MHRice does not explicitly -1

def enum_ApplyRules(type_id):
    type_list = [None, 'ElementNone', 'ElementFire', 'ElementWater', 'ElementThunder', 'ElementIce', 'ElementDragon',\
                'ElementPoison', 'ElementSleep', 'ElementParalyze', 'ElementBomb', 'ElementNotEqualMain', 'ElementFirstGroup',\
                'CanEquipTargetBottle', 'Series064', 'Series065']
    return type_list[type_id]

def enum_BulletType(type_id):
    type_list = [None, 'Normal1', 'Normal2', 'Normal3', 'Kantsu1', 'Kantsu2', 'Kantsu3', 'SanW1', 'SanW2', 'SanW3', 'SanO1',\
                'SanO2', 'SanO3', 'Tekko1', 'Tekko2', 'Tekko3', 'Kakusan1', 'Kakusan2', 'Kakusan3', 'Poison1', 'Poison2',\
                'Paralyze1', 'Paralyze2', 'Sleep1', 'Sleep2', 'Genki1', 'Genki2', 'Heal1', 'Heal2', 'Kijin', 'Kouka', 'Fire',\
                'FireKantsu', 'Water', 'WaterKantsu', 'Ice', 'IceKantsu', 'Thunder', 'ThunderKantsu', 'Dragon', 'DragonKantsu',\
                'Zanretsu', 'Ryugeki', 'Capture', 'Setti', 'Gatling', 'Snipe', 'GatlingHeal', 'SnipeHeal', 'WireBullet']
    return type_list[type_id]

def enum_BottlePowerUpTypes(type_id):
    type_list = [None, 'ShortRange', 'Poison', 'Paralyze', 'Sleep']
    return type_list[type_id]

def enum_ElementType(type_id):
    type_list = [None, 'Fire', 'Water', 'Thunder', 'Ice', 'Dragon', 'Poison', 'Sleep', 'Paralyze', 'Bomb']
    return type_list[type_id]

def enum_GunLanceFireType(type_id):
    type_list = ['Normal', 'Radial', 'Diffusion']
    return type_list[type_id]

def newtype_GunLanceFireLv(type):
    return utils.u32_to_i32(type) + 1

def enum_ChargeAxeBottleTypes(type_id):
    type_list = [None, 'StrongElement', 'Power']
    return type_list[type_id]

def enum_SlashAxeBottleTypes(type_id):
    type_list = [None, 'StrongElement', 'Power', 'Poison', 'Paralyze', None, None, 'DownStamina', 'Dragon']
    return type_list[type_id]

def enum_UniqueBulletType(type_id):
    type_list = ['Snipe', 'Gatling']
    return type_list[type_id]

def enum_BowChargeTypes(type_id):
    type_list = [None, 'BurstLv1', 'BurstLv2', 'BurstLv3', 'BurstLv4', 'BurstLv5', 'DiffusionLv1', 'DiffussionLv2', 'DiffusionLv3',\
                'DifussionLv4', 'DiffusionLv5', 'TransfixLv1', 'TransfixLv2', 'TransfixLv3', 'TransfixLv4', 'TransfixLv5']
    return type_list[type_id]

def enum_BowBottleTypes(type_id):
    type_list = ['ShortRange', 'Power', 'Poison', 'Paralyze', 'Sleep', 'Blast', 'DownStamina', 'Max', None]
    return type_list[type_id]

def enum_PlHyakuryuSkillId(hyakuryu_skill_id):
    if hyakuryu_skill_id == 0:
        return None
    else:
        return hyakuryu_skill_id - 1

def newtype_BowChargeStartLvTypes(type):
    return utils.u32_to_i32(type) + 1

def newtype_InsectLevelTypes(type):
    return utils.u32_to_i32(type) + 1

def enum_DecorationsId(decoration_id):
    if decoration_id == 0:
        return None
    else:
        return decoration_id - 1

########################################
# These are listed in MHRice weapon.rs
def enum_PlWeaponElementTypes(type_id):
    type_list = [None, 'Fire', 'Water', 'Thunder', 'Ice', 'Dragon', 'Poison', 'Sleep', 'Paralyze', 'Bomb']
    return type_list[type_id]

def enum_WeaponId(weapon_id):
    weapon_type_dict = {str(0x08100000): 'GreatSword',\
                        str(0x08200000): 'ShortSword',\
                        str(0x08300000): 'Hammer',\
                        str(0x08400000): 'Lance',\
                        str(0x08500000): 'LongSword',\
                        str(0x08600000): 'SlashAxe',\
                        str(0x08700000): 'GunLance',\
                        str(0x08800000): 'DualBlades',\
                        str(0x08900000): 'Horn',\
                        str(0x08A00000): 'InsectGlaive',\
                        str(0x08B00000): 'ChargeAxe',\
                        str(0x08C00000): 'LightBowgun',\
                        str(0x08D00000): 'HeavyBowgun',\
                        str(0x08E00000): 'Bow',\
                        str(0x08F00000): 'Insect'}
    if weapon_id == 0:
        return 'Null'
    elif weapon_id == 0x08000000:
        return None
    else:
        true_id = weapon_id & 0x0000FFFF
        weapon_type = weapon_id & 0xFFFF0000
        weapon_type_str = weapon_type_dict[str(weapon_type)]
        return weapon_type_str + '({})'.format(true_id)

def enum_Fluctuation(type_id):
    type_list = [None, 'LeftLittle', 'LeftMuch', 'RightLittle', 'RightMuch', 'RightAndLeftLittle', 'RightAndLeftMuch']
    return type_list[type_id]

def enum_KakusanType(type_id):
    type_list = ['CloseAttack', 'HorizontalAttack']
    return type_list[type_id]

def enum_ShootType(type_id):
    type_list = [None, 'MovingShot', 'MovingShotReload', 'MovingShotSingleAuto', 'MovingReload', 'MovingReloadSingleAuto',\
                'SingleAuto', 'MovingShotReloadSingleAuto']
    return type_list[type_id]

def enum_TreeType(type_id):
    if type_id == 0:
        return None
    else:
        return type_id - 2

def enum_VillageProgress(progress_id):
    if progress_id == 0:
        return None
    else:
        return progress_id - 1

def enum_HallProgress(progress_id):
    if progress_id == 0:
        return None
    else:
        return progress_id - 1
