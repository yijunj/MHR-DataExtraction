from monster import *
from weapon import *
import user
import pickle

# Gather user file data into one class
class PediaUser(OrderedAttibuteClass):
    def __init__(self): # This initialization is just to remind you of the data types
        self.large_monsters = ['monster.Monster']
        self.small_monsters = ['monster.Monster']
        self.condition_preset = 'condition_damage_preset.EnemyConditionPresetData'
        self.monster_list = 'boss.MonsterListBossData'
        self.monster_lot = 'lot.MonsterLotTableUserData'
        self.parts_type = 'lot.PartsTypeTextUserData'
        self.normal_quest_data = 'quest.NormalQuestData'
        self.normal_quest_data_for_enemy = 'quest.NormalQuestDataForEnemy'
        self.difficulty_rate = 'quest.SystemDifficultyRateData'
        self.random_scale = 'quest.RandomScaleTableData'
        self.size_list = 'quest.EnemySizeListData'
        self.discover_em_set_data = 'quest.DiscoverEmSetData'
        self.armor = 'armor.ArmorBaseUserData'
        self.armor_series = 'armor.ArmorSeriesUserData'
        self.armor_product = 'armor.ArmorProductUserData'
        self.overwear = 'armor.PlOverwearBaseUserData'
        self.overwear_product = 'armor.PlOverwearProductUserData'
        self.equip_skill = 'skill.PlEquipSkillBaseUserData'
        self.hyakuryu_skill = 'skill.PlHyakuryuSkillBaseUserData'
        self.hyakuryu_skill_recipe = 'skill.PlHyakuryuSkillRecipeUserData'
        self.decorations = 'skill.DecorationsBaseUserData'
        self.decorations_product = 'skill.DecorationsProductUserData'
        self.alchemy_pattern = 'alchemy.AlchemyPatturnUserData'
        self.alchemy_pl_skill = 'alchemy.AlchemyPlSkillTableUserData'
        self.alchemy_grade_worth = 'alchemy.GradeWorthTableUserData'
        self.alchemy_rare_type = 'alchemy.RareTypeTableUserData'
        self.alchemy_second_skill_lot = 'alchemy.SecondSkillLotRateTableUserData'
        self.alchemy_skill_grade_lot = 'alchemy.SkillGradeLotRateTableUserData'
        self.alchemy_slot_num = 'alchemy.SlotNumTableUserData'
        self.alchemy_slot_worth = 'alchemy.SlotWorthTableUserData'
        self.item_list = 'item.ItemUserData'
        self.great_sword = 'weapon.WeaponList'
        self.short_sword = 'weapon.WeaponList'
        self.hammer = 'weapon.WeaponList'
        self.lance = 'weapon.WeaponList'
        self.long_sword = 'weapon.WeaponList'
        self.slash_axe = 'weapon.WeaponList'
        self.gun_lance = 'weapon.WeaponList'
        self.dual_blades = 'weapon.WeaponList'
        self.horn = 'weapon.WeaponList'
        self.insect_glaive = 'weapon.WeaponList'
        self.charge_axe = 'weapon.WeaponList'
        self.light_bowgun = 'weapon.WeaponList'
        self.heavy_bowgun = 'weapon.WeaponList'
        self.bow = 'weapon.WeaponList'

    def collect_user_data(self):
        _, self.large_monsters = read_large_monster_data()
        _, self.small_monsters = read_small_monster_data()
        self.condition_preset = user.read_user_file('user\\condition_damage_preset\\system_condition_damage_preset_data.user.2')
        self.monster_list = user.read_user_file('user\\boss\\MonsterListBossData.user.2')
        self.monster_lot = user.read_user_file('user\\lot\\MonsterLotTableData.user.2')
        self.parts_type = user.read_user_file('user\\lot\\PartsTypeTextData.user.2')
        self.normal_quest_data = user.read_user_file('user\\quest\\NormalQuestData.user.2')
        self.normal_quest_data_for_enemy = user.read_user_file('user\\quest\\NormalQuestDataForEnemy.user.2')
        self.difficulty_rate = user.read_user_file('user\\quest\\system_difficulty_rate_data.user.2')
        self.random_scale = user.read_user_file('user\\quest\\system_boss_random_scale_data.user.2')
        self.size_list = user.read_user_file('user\\quest\\system_enemy_sizelist_data.user.2')
        self.discover_em_set_data = user.read_user_file('user\\quest\\DiscoverEmSetData.user.2')
        self.armor = user.read_user_file('user\\armor\\ArmorBaseData.user.2')
        self.armor_series = user.read_user_file('user\\armor\\ArmorSeriesData.user.2')
        self.armor_product = user.read_user_file('user\\armor\\ArmorProductData.user.2')
        self.overwear = user.read_user_file('user\\armor\\PlOverwearBaseData.user.2')
        self.overwear_product = user.read_user_file('user\\armor\\PlOverwearProductUserData.user.2')
        self.equip_skill = user.read_user_file('user\\skill\\PlEquipSkillBaseData.user.2')
        self.hyakuryu_skill = user.read_user_file('user\\skill\\PlHyakuryuSkillBaseData.user.2')
        self.hyakuryu_skill_recipe = user.read_user_file('user\\skill\\HyakuryuSkillRecipeData.user.2')
        self.decorations = user.read_user_file('user\\skill\\DecorationsBaseData.user.2')
        self.decorations_product = user.read_user_file('user\\skill\\DecorationsProductData.user.2')
        self.alchemy_pattern = user.read_user_file('user\\alchemy\\AlchemyPatturnData.user.2')
        self.alchemy_pl_skill = user.read_user_file('user\\alchemy\\AlchemyPlSkillTable.user.2')
        self.alchemy_grade_worth = user.read_user_file('user\\alchemy\\GradeWorthTable.user.2')
        self.alchemy_rare_type = user.read_user_file('user\\alchemy\\RareTypeTable.user.2')
        self.alchemy_second_skill_lot = user.read_user_file('user\\alchemy\\SecondSkillLotRateTable.user.2')
        self.alchemy_skill_grade_lot = user.read_user_file('user\\alchemy\\SkillGradeLotRateTable.user.2')
        self.alchemy_slot_num = user.read_user_file('user\\alchemy\\SlotNumTable.user.2')
        self.alchemy_slot_worth = user.read_user_file('user\\alchemy\\SlotWorthTable.user.2')
        self.item_list = user.read_user_file('user\\item\\ItemData.user.2')
        self.great_sword = WeaponList('GreatSword')
        self.short_sword = WeaponList('ShortSword')
        self.hammer = WeaponList('Hammer')
        self.lance = WeaponList('Lance')
        self.long_sword = WeaponList('LongSword')
        self.slash_axe = WeaponList('SlashAxe')
        self.gun_lance = WeaponList('GunLance')
        self.dual_blades = WeaponList('DualBlades')
        self.horn = WeaponList('Horn')
        self.insect_glaive = WeaponList('InsectGlaive')
        self.charge_axe = WeaponList('ChargeAxe')
        self.light_bowgun = WeaponList('LightBowgun')
        self.heavy_bowgun = WeaponList('HeavyBowgun')
        self.bow = WeaponList('Bow')

if __name__ == '__main__':
    pedia_user = PediaUser()
    pedia_user.collect_user_data()
    # with open('pedia_user.pickle', 'wb') as f:
    #     pickle.dump(pedia_user, f)
    # print('Pedia saved as pickle file')
    # user.print_hierarchical_object(pedia_user)
