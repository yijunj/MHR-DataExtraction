import monster
import weapon
import user
import msg
import utils
from utils import OrderedAttibuteClass
import pickle

# Gather user and msg file data into one class
class Pedia(OrderedAttibuteClass):
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
        self.quest_reward = 'quest.QuestDataForRewardUserData'
        self.quest_reward_table = 'quest.RewardIdLotTableUserData'
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

        self.hunter_note_msg = 'msg.Msg'
        self.monster_names = 'msg.Msg'
        self.monster_aliases = 'msg.Msg'
        self.quest_hall_msg = 'msg.Msg'
        self.quest_village_msg = 'msg.Msg'
        self.quest_tutorial_msg = 'msg.Msg'
        self.quest_arena_msg = 'msg.Msg'
        self.armor_head_name_msg = 'msg.Msg'
        self.armor_chest_name_msg = 'msg.Msg'
        self.armor_arm_name_msg = 'msg.Msg'
        self.armor_waist_name_msg = 'msg.Msg'
        self.armor_leg_name_msg = 'msg.Msg'
        self.armor_series_name_msg = 'msg.Msg'
        self.player_skill_name_msg = 'msg.Msg'
        self.player_skill_explain_msg = 'msg.Msg'
        self.player_skill_detail_msg = 'msg.Msg'
        self.hyakuryu_skill_name_msg = 'msg.Msg'
        self.hyakuryu_skill_explain_msg = 'msg.Msg'
        self.decorations_name_msg = 'msg.Msg'
        self.items_name_msg = 'msg.Msg'
        self.items_explain_msg = 'msg.Msg'
        self.material_category_msg = 'msg.Msg'
        self.horn_melody = 'msg.Msg'

    def collect_data(self):
        _, self.large_monsters = monster.read_large_monster_data()
        _, self.small_monsters = monster.read_small_monster_data()
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
        self.quest_reward = user.read_user_file('user\\quest\\QuestDataForRewardData.user.2')
        self.quest_reward_table = user.read_user_file('user\\quest\\RewardIdLotTableData.user.2')
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
        self.great_sword = weapon.WeaponList('GreatSword')
        self.short_sword = weapon.WeaponList('ShortSword')
        self.hammer = weapon.WeaponList('Hammer')
        self.lance = weapon.WeaponList('Lance')
        self.long_sword = weapon.WeaponList('LongSword')
        self.slash_axe = weapon.WeaponList('SlashAxe')
        self.gun_lance = weapon.WeaponList('GunLance')
        self.dual_blades = weapon.WeaponList('DualBlades')
        self.horn = weapon.WeaponList('Horn')
        self.insect_glaive = weapon.WeaponList('InsectGlaive')
        self.charge_axe = weapon.WeaponList('ChargeAxe')
        self.light_bowgun = weapon.WeaponList('LightBowgun')
        self.heavy_bowgun = weapon.WeaponList('HeavyBowgun')
        self.bow = weapon.WeaponList('Bow')

        self.hunter_note_msg = msg.read_msg_file('msg\\HN_Hunternote_Menu.msg.17')
        self.monster_names = msg.read_msg_file('msg\\Tag_EM_Name.msg.17')
        self.monster_aliases = msg.read_msg_file('msg\\Tag_EM_Name_Alias.msg.17')
        self.quest_hall_msg = msg.read_msg_file('msg\\QuestData_Hall.msg.17')
        self.quest_village_msg = msg.read_msg_file('msg\\QuestData_Village.msg.17')
        self.quest_tutorial_msg = msg.read_msg_file('msg\\QuestData_Tutorial.msg.17')
        self.quest_arena_msg = msg.read_msg_file('msg\\QuestData_Arena.msg.17')
        self.armor_head_name_msg = msg.read_msg_file('msg\\A_Head_Name.msg.17')
        self.armor_chest_name_msg = msg.read_msg_file('msg\\A_Chest_Name.msg.17')
        self.armor_arm_name_msg = msg.read_msg_file('msg\\A_Arm_Name.msg.17')
        self.armor_waist_name_msg = msg.read_msg_file('msg\\A_Waist_Name.msg.17')
        self.armor_leg_name_msg = msg.read_msg_file('msg\\A_Leg_Name.msg.17')
        self.armor_series_name_msg = msg.read_msg_file('msg\\ArmorSeries_Hunter_Name.msg.17')
        self.player_skill_name_msg = msg.read_msg_file('msg\\PlayerSkill_Name.msg.17')
        self.player_skill_explain_msg = msg.read_msg_file('msg\\PlayerSkill_Explain.msg.17')
        self.player_skill_detail_msg = msg.read_msg_file('msg\\PlayerSkill_Detail.msg.17')
        self.hyakuryu_skill_name_msg = msg.read_msg_file('msg\\HyakuryuSkill_Name.msg.17')
        self.hyakuryu_skill_explain_msg = msg.read_msg_file('msg\\HyakuryuSkill_Explain.msg.17')
        self.decorations_name_msg = msg.read_msg_file('msg\\Decorations_Name.msg.17')
        self.items_name_msg = msg.read_msg_file('msg\\ItemName.msg.17')
        self.items_explain_msg = msg.read_msg_file('msg\\ItemExplain.msg.17')
        self.material_category_msg = msg.read_msg_file('msg\\ItemCategoryType_Name.msg.17')
        self.horn_melody = msg.read_msg_file('msg\\Horn_UniqueParam.msg.17')

if __name__ == '__main__':
    pedia = Pedia()
    pedia.collect_data()
    with open('pedia.pickle', 'wb') as f:
        pickle.dump(pedia, f)
    print('Pedia saved as pickle file')
    # utils.print_hierarchical_object(pedia)
