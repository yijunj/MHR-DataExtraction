import sys
sys.path.append('..')

import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualMonsterData(OrderedAttibuteClass):
    def __init__(self, enemy_index):
        self.name = {'zh':None, 'en':None, 'ja':None}

        self.enemy_index = enemy_index
        self.id = None
        self.sub_id = None
        self.enemy_type_id = None
        self.is_large_monster = None

        self.family_type = None
        self.habitat_area = []
        self.meat_msg_id_list = [] # Dropped eventually
        self.meat_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.meat_list_by_phase = {0:[], 1:[], 2:[], 3:[], 4:[]}

        self.part_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.part_ig_light_list = []
        self.part_breakable_list = []
        self.part_severable_list = []

        self.lr_target_reward_item_id_list = []
        self.lr_target_reward_num_list = []
        self.lr_target_reward_prob_list = []

        self.lr_carve_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.lr_carve_item_id_list_by_part = {0:[], 1:[], 2:[]}
        self.lr_carve_num_list_by_part = {0:[], 1:[], 2:[]}
        self.lr_carve_prob_list_by_part = {0:[], 1:[], 2:[]}

        self.lr_capture_reward_item_id_list = []
        self.lr_capture_reward_num_list = []
        self.lr_capture_reward_prob_list = []

        self.lr_break_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.lr_break_part_lv_list = []
        self.lr_break_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.lr_break_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.lr_break_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

        self.lr_drop_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.lr_drop_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.lr_drop_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.lr_drop_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

        self.lr_palico_reward_item_id_list = []
        self.lr_palico_reward_num_list = []
        self.lr_palico_reward_prob_list = []

        self.hr_target_reward_item_id_list = []
        self.hr_target_reward_num_list = []
        self.hr_target_reward_prob_list = []

        self.hr_carve_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.hr_carve_item_id_list_by_part = {0:[], 1:[], 2:[]}
        self.hr_carve_num_list_by_part = {0:[], 1:[], 2:[]}
        self.hr_carve_prob_list_by_part = {0:[], 1:[], 2:[]}

        self.hr_capture_reward_item_id_list = []
        self.hr_capture_reward_num_list = []
        self.hr_capture_reward_prob_list = []

        self.hr_break_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.hr_break_part_lv_list = []
        self.hr_break_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.hr_break_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.hr_break_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

        self.hr_drop_name_list = {'zh':[], 'en':[], 'ja':[]}
        self.hr_drop_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.hr_drop_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
        self.hr_drop_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

        self.hr_palico_reward_item_id_list = []
        self.hr_palico_reward_num_list = []
        self.hr_palico_reward_prob_list = []

    def clean_up(self):
        delattr(self, 'meat_msg_id_list')

def parse_monster_data(pedia):
    max_length = 1000
    monster_list = [None] * max_length
    monster_list_from_pedia = [None] * max_length

    # Generate part dictionary
    max_length_part_dict = 100
    part_dict_key_list = [None] * max_length_part_dict
    part_dict_value_list = [None] * max_length_part_dict
    for msg in pedia.hunter_note_msg.entries:
        if 'Parts' in msg.name:
            part_id = int(msg.name[-2:])
            part_dict_key_list[part_id] = str(msg.guid)
            part_dict_value_list[part_id] = msg
    for i in reversed(range(max_length_part_dict)):
        if not part_dict_key_list[i] is None:
            break
    part_dict_key_list = part_dict_key_list[:i+1]
    for i in reversed(range(max_length_part_dict)):
        if not part_dict_value_list[i] is None:
            break
    part_dict_value_list = part_dict_value_list[:i+1]
    part_dict = OrderedDict(zip(part_dict_key_list, part_dict_value_list))

    # Get monster names and ids
    # Data originally stored in pedia.monster_names
    for name in pedia.monster_names.entries:
        if parse_data_utils.verify_msg_name(name, 'EnemyIndex'):
            enemy_index = int(name.name.split('Index')[1])
            monster_list[enemy_index] = IndividualMonsterData(enemy_index)
            monster_list[enemy_index].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            monster_list[enemy_index].name['en'] = name.content[1].replace('\r\n', ' ')
            monster_list[enemy_index].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    # The order in pedia.large_monsters matches with that in pedia.monster_names.entries
    # But the ids don't match up! (enemy_type matches most of the time, but exceptions exist)
    # Similarly, only the order matches for small monsters
    # So it's important to visit pedia.large_monsters and pedia.small_monsters in order
    # and assign them to (the non-empty entries of) monster_list sequentially
    enemy_index = 0
    for monster in pedia.large_monsters:
        if not monster_list[enemy_index] is None:
            monster_list_from_pedia[enemy_index] = monster
            monster_list[enemy_index].id = monster.id
            monster_list[enemy_index].sub_id = monster.sub_id
            monster_list[enemy_index].enemy_type_id = monster.sub_id * 256 + monster.id
            monster_list[enemy_index].is_large_monster = True
        enemy_index += 1
    for monster in pedia.small_monsters:
        if not monster_list[enemy_index] is None and monster.sub_id == 0:
            monster_list_from_pedia[enemy_index] = monster
            monster_list[enemy_index].id = monster.id
            monster_list[enemy_index].sub_id = monster.sub_id
            monster_list[enemy_index].enemy_type_id = monster.sub_id * 256 + monster.id
            monster_list[enemy_index].is_large_monster = False
        enemy_index += 1

    # Get the part id list so that the part names can be looked up from hunter's note msg
    # Data originally stored in pedia.monster_list
    for enemy in pedia.monster_list.data_list:
        # Seems like this data set only contains large monsters
        if enemy.em_type.startswith('Em('):
            enemy_type_id = int(enemy.em_type.split('(')[1].split(')')[0])
            for monster in monster_list:
                if monster is None:
                    continue
                if monster.enemy_type_id != enemy_type_id:
                    continue
                if not monster.is_large_monster:
                    continue

                monster.family_type = enemy.family_type
                monster.habitat_area = enemy.habitat_area.flag
                # Not needed for new extraction code
                if len(monster.habitat_area) == 1 and type(monster.habitat_area[0]) == type(0):
                    monster.habitat_area = bin(monster.habitat_area[0])[2:]
                    monster.habitat_area = [int(p)+1 for p, c in enumerate(monster.habitat_area) if c == '1']
                meat_msg_id_list = [i.part for i in enemy.part_table_data]
                part_order_list = [i.em_meat for i in enemy.part_table_data]
                monster.meat_msg_id_list = [i for _, i in sorted(zip(part_order_list, meat_msg_id_list))]
                break

    # Get the part names from hunter's note msg
    # Data originally stored in pedia.hunter_note_msg
    for monster in monster_list:
        if not monster is None:
            for part_id in monster.meat_msg_id_list:
                monster.meat_name_list['zh'].append(list(part_dict.values())[part_id].content[13])
                monster.meat_name_list['en'].append(list(part_dict.values())[part_id].content[1])
                monster.meat_name_list['ja'].append(list(part_dict.values())[part_id].content[0])

    # Meat and part data
    # Meat data originally stored in pedia.large_monsters[i].meat_data and pedia.small_monsters[i].meat_data
    # Part data originally stored in pedia.large_monsters[i].data_tune and pedia.small_monsters[i].data_tune
    for enemy_index in range(len(monster_list_from_pedia)):
        monster_from_pedia = monster_list_from_pedia[enemy_index]
        if not monster_from_pedia is None:
            monster = monster_list[enemy_index]

            # Meat
            for i in range(len(monster.meat_msg_id_list)):
                meat_group_info = monster_from_pedia.meat_data.meat_container[i].meat_group_info
                for phase in range(5):
                    meat_list = monster.meat_list_by_phase[phase]
                    if len(meat_group_info) > phase:
                        meat_list.append(meat_group_info[phase].__odict__)
                if len(meat_group_info) > 5:
                    raise Exception('{} has more than 5 phases!'.format(monster.name['en']))

            # Small monsters do not have meat_msg_id_list, so treat them separately
            if not monster.is_large_monster:
                for i in monster_from_pedia.meat_data.meat_container:
                    meat_group_info = i.meat_group_info
                    for phase in range(5):
                        meat_list = monster.meat_list_by_phase[phase]
                        if len(meat_group_info) > phase:
                            if meat_group_info[phase].slash == 0:
                                break
                            meat_list.append(meat_group_info[phase].__odict__)
                    if len(meat_group_info) > 5:
                        raise Exception('{} has more than 5 phases!'.format(monster.name['en']))
                part_num = len(monster.meat_list_by_phase[0])
                if part_num == 1:
                    monster.meat_name_list['zh'] = ['躯干']
                    monster.meat_name_list['en'] = ['Torso']
                    monster.meat_name_list['ja'] = ['胴']
                elif part_num == 2:
                    monster.meat_name_list['zh'] = ['头部', '躯干']
                    monster.meat_name_list['en'] = ['Head', 'Torso']
                    monster.meat_name_list['ja'] = ['頭', '胴']
                elif part_num == 3:
                    monster.meat_name_list['zh'] = ['头部', '躯干', '尾巴']
                    monster.meat_name_list['en'] = ['Head', 'Torso', 'Tail']
                    monster.meat_name_list['ja'] = ['頭', '胴', '尻尾']
                if monster.name['en'] == 'Remobra': # Outlier
                    monster.meat_name_list['zh'] = ['头部', '尾巴', '翼']
                    monster.meat_name_list['en'] = ['Head', 'Tail', 'Wing']
                    monster.meat_name_list['ja'] = ['頭', '尻尾', '翼']

            # Part and IG light
            part_name_list_ja = monster_from_pedia.parts_map
            # monster = clean_monster_part_name(monster)
            for i in monster_from_pedia.data_tune.enemy_parts_data:
                if not i.extractive_type is None:
                    monster.part_ig_light_list.append(i.extractive_type)

            # Some outliers
            if len(part_name_list_ja) != len(monster.part_ig_light_list):
                if monster.name['en'] == 'Goss Harag' or monster.name['en'] == 'Bnahabra':
                    monster.part_ig_light_list = monster.part_ig_light_list[:-1]
                else:
                    raise Exception('Part number does not match for {}'.format(monster.name['en']))
            if monster.name['en'] == 'Felyne' or monster.name['en'] == 'Kulu-Ya-Ku':
                part_name_list_ja = part_name_list_ja[:-1]
                monster.part_ig_light_list = monster.part_ig_light_list[:-1]

            monster.part_breakable_list = [False] * len(part_name_list_ja)
            monster.part_severable_list = [False] * len(part_name_list_ja)
            for i in monster_from_pedia.data_tune.enemy_parts_break_data_list:
                if i.parts_group < len(monster.part_breakable_list):
                    monster.part_breakable_list[i.parts_group] = True
            for i in monster_from_pedia.data_tune.enemy_parts_loss_data_list:
                if i.parts_group < len(monster.part_severable_list):
                    monster.part_severable_list[i.parts_group] = True

            monster.part_name_list['zh'] = [None] * len(part_name_list_ja)
            monster.part_name_list['en'] = [None] * len(part_name_list_ja)
            monster.part_name_list['ja'] = [None] * len(part_name_list_ja)
            for i in range(len(part_name_list_ja)):
                name_translated = parse_data_utils.translate_part_name(part_name_list_ja[i])
                monster.part_name_list['zh'][i] = name_translated.name_zh
                monster.part_name_list['en'][i] = name_translated.name_en
                monster.part_name_list['ja'][i] = name_translated.name_ja

    # Reward data
    # Data originally stored in pedia.monster_lot
    for enemy in pedia.monster_lot.param:
        if enemy.em_types.startswith('Em'):
            enemy_type_id = int(enemy.em_types.split('(')[1].split(')')[0])
            is_large_monster = enemy.em_types.startswith('Em(')
            for monster in monster_list:
                if monster is None:
                    continue
                if monster.enemy_type_id != enemy_type_id:
                    continue
                if monster.is_large_monster != is_large_monster:
                    continue

                # Target reward
                temp_target_reward_item_id_list =\
                    [int(i.split('(')[1].split(')')[0]) for i in enemy.target_reward_item_id_list if not i is None]
                temp_target_reward_num_list = [i for i in enemy.target_reward_num_list if i != 0]
                temp_target_reward_prob_list = [i for i in enemy.target_reward_probability_list if i != 0]

                # Carve reward
                temp_carve_name_list = {'zh':[], 'en':[], 'ja':[]}
                temp_carve_item_id_list_by_part = {0:[], 1:[], 2:[]}
                temp_carve_num_list_by_part = {0:[], 1:[], 2:[]}
                temp_carve_prob_list_by_part = {0:[], 1:[], 2:[]}
                temp_carve_name_list['en'] = [i for i in enemy.enemy_reward_type_list if not i is None]
                for i in range(30):
                    carve_list_id = int(i/10)
                    if not enemy.hagitory_reward_item_id_list[i] is None:
                        temp_carve_item_id_list_by_part[carve_list_id]\
                            .append(int(enemy.hagitory_reward_item_id_list[i].split('(')[1].split(')')[0]))
                    if enemy.hagitory_reward_num_list[i] != 0:
                        temp_carve_num_list_by_part[carve_list_id].append(enemy.hagitory_reward_num_list[i])
                    if enemy.hagitory_reward_probability_list[i] != 0:
                        temp_carve_prob_list_by_part[carve_list_id].append(enemy.hagitory_reward_probability_list[i])
                if len(temp_carve_name_list['en']) == 1:
                    temp_carve_name_list['zh'] = ['本体']
                    temp_carve_name_list['en'] = ['Body']
                    temp_carve_name_list['ja'] = ['体']
                elif len(temp_carve_name_list['en']) == 2:
                    temp_carve_name_list['zh'] = ['本体', '尾巴']
                    temp_carve_name_list['en'] = ['Body', 'Tail']
                    temp_carve_name_list['ja'] = ['体', '尻尾']
                elif len(temp_carve_name_list['en']) == 3:
                    if monster.name['en'] == 'Barroth':
                        temp_carve_name_list['zh'] = ['本体', '尾巴', '头壳']
                        temp_carve_name_list['en'] = ['Body', 'Tail', '头壳']
                        temp_carve_name_list['ja'] = ['体', '尻尾', '頭殻']
                    if monster.name['en'] == 'Basarios':
                        temp_carve_name_list['zh'] = ['本体', '尾巴', '拟岩态或倒地时用铁镐在背后挖掘']
                        temp_carve_name_list['zh'] = ['Body', 'Tail', 'Special']
                        temp_carve_name_list['zh'] = ['体', '尻尾', '特殊']
                    elif monster.name['en'].endswith('Zinogre'):
                        temp_carve_name_list['zh'] = ['本体', '尾巴', '倒地时用网在背后捕捉']
                        temp_carve_name_list['zh'] = ['Body', 'Tail', 'Special']
                        temp_carve_name_list['zh'] = ['体', '尻尾', '特殊']

                # Capture reward
                temp_capture_reward_item_id_list =\
                    [int(i.split('(')[1].split(')')[0]) for i in enemy.capture_reward_item_id_list if not i is None]
                temp_capture_reward_num_list = [i for i in enemy.capture_reward_num_list if i != 0]
                temp_capture_reward_prob_list = [i for i in enemy.capture_reward_probability_list if i != 0]

                # Part break reward
                temp_break_name_list = {'zh':[], 'en':[], 'ja':[]}
                temp_break_part_lv_list = []
                temp_break_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                temp_break_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                temp_break_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                for part in enemy.parts_break_list:
                    if not part is None:
                        parts_break_list_entry = pedia.parts_type.params[part]
                        for info in parts_break_list_entry.text_infos:
                            if 'Em({})'.format(enemy_type_id) in info.enemy_type_list:
                                temp_break_name_list['zh'].append(part_dict[str(info.text_bytes_for_monster_list)].content[13])
                                temp_break_name_list['en'].append(part_dict[str(info.text_bytes_for_monster_list)].content[1])
                                temp_break_name_list['ja'].append(part_dict[str(info.text_bytes_for_monster_list)].content[0])
                for part_lv in enemy.parts_break_lv_list:
                    if not part_lv is None:
                        temp_break_part_lv_list.append(int(part_lv[-1]))
                for i in range(60):
                    break_list_id = int(i/10)
                    if not enemy.parts_break_reward_item_id_list[i] is None:
                        temp_break_item_id_list_by_part[break_list_id]\
                            .append(int(enemy.parts_break_reward_item_id_list[i].split('(')[1].split(')')[0]))
                    if enemy.parts_break_reward_num_list[i] != 0:
                        temp_break_num_list_by_part[break_list_id].append(enemy.parts_break_reward_num_list[i])
                    if enemy.parts_break_reward_probability_list[i] != 0:
                        temp_break_prob_list_by_part[break_list_id].append(enemy.parts_break_reward_probability_list[i])

                # Drop reward
                temp_drop_name_list = {'zh':[], 'en':[], 'ja':[]}
                temp_drop_item_id_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                temp_drop_num_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                temp_drop_prob_list_by_part = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}
                temp_drop_name_list['en'] = [i for i in enemy.drop_reward_type_list if not i is None]
                for i in range(60):
                    drop_list_id = int(i/10)
                    if not enemy.drop_reward_item_id_list[i] is None:
                        temp_drop_item_id_list_by_part[drop_list_id]\
                            .append(int(enemy.drop_reward_item_id_list[i].split('(')[1].split(')')[0]))
                    if enemy.drop_reward_num_list[i] != 0:
                        temp_drop_num_list_by_part[drop_list_id].append(enemy.drop_reward_num_list[i])
                    if enemy.drop_reward_probability_list[i] != 0:
                        temp_drop_prob_list_by_part[drop_list_id].append(enemy.drop_reward_probability_list[i])
                if len(temp_drop_name_list['en']) == 1:
                    temp_drop_name_list['zh'] = ['普通掉落']
                    temp_drop_name_list['en'] = ['Normal']
                    temp_drop_name_list['ja'] = ['平常']
                elif len(temp_drop_name_list['en']) == 2:
                    temp_drop_name_list['zh'] = ['普通掉落', '骑乘掉落']
                    temp_drop_name_list['en'] = ['Normal', 'Riding']
                    temp_drop_name_list['ja'] = ['平常', '乗る']

                # Palico reward
                temp_palico_reward_item_id_list =\
                    [int(i.split('(')[1].split(')')[0]) for i in enemy.otomo_reward_item_id_list if not i is None]
                temp_palico_reward_num_list = [i for i in enemy.otomo_reward_num_list if i != 0]
                temp_palico_reward_prob_list = [i for i in enemy.otomo_reward_probability_list if i != 0]

                # Choose rank
                if enemy.quest_rank == 'Low':
                    monster.lr_target_reward_item_id_list = temp_target_reward_item_id_list
                    monster.lr_target_reward_num_list = temp_target_reward_num_list
                    monster.lr_target_reward_prob_list = temp_target_reward_prob_list
                    monster.lr_carve_name_list = temp_carve_name_list
                    monster.lr_carve_item_id_list_by_part = temp_carve_item_id_list_by_part
                    monster.lr_carve_num_list_by_part = temp_carve_num_list_by_part
                    monster.lr_carve_prob_list_by_part = temp_carve_prob_list_by_part
                    monster.lr_capture_reward_item_id_list = temp_capture_reward_item_id_list
                    monster.lr_capture_reward_num_list = temp_capture_reward_num_list
                    monster.lr_capture_reward_prob_list = temp_capture_reward_prob_list
                    monster.lr_break_name_list = temp_break_name_list
                    monster.lr_break_part_lv_list = temp_break_part_lv_list
                    monster.lr_break_item_id_list_by_part = temp_break_item_id_list_by_part
                    monster.lr_break_num_list_by_part = temp_break_num_list_by_part
                    monster.lr_break_prob_list_by_part = temp_break_prob_list_by_part
                    monster.lr_drop_name_list = temp_drop_name_list
                    monster.lr_drop_item_id_list_by_part = temp_drop_item_id_list_by_part
                    monster.lr_drop_num_list_by_part = temp_drop_num_list_by_part
                    monster.lr_drop_prob_list_by_part = temp_drop_prob_list_by_part
                    monster.lr_palico_reward_item_id_list = temp_palico_reward_item_id_list
                    monster.lr_palico_reward_num_list = temp_palico_reward_num_list
                    monster.lr_palico_reward_prob_list = temp_palico_reward_prob_list
                elif enemy.quest_rank == 'High':
                    monster.hr_target_reward_item_id_list = temp_target_reward_item_id_list
                    monster.hr_target_reward_num_list = temp_target_reward_num_list
                    monster.hr_target_reward_prob_list = temp_target_reward_prob_list
                    monster.hr_carve_name_list = temp_carve_name_list
                    monster.hr_carve_item_id_list_by_part = temp_carve_item_id_list_by_part
                    monster.hr_carve_num_list_by_part = temp_carve_num_list_by_part
                    monster.hr_carve_prob_list_by_part = temp_carve_prob_list_by_part
                    monster.hr_capture_reward_item_id_list = temp_capture_reward_item_id_list
                    monster.hr_capture_reward_num_list = temp_capture_reward_num_list
                    monster.hr_capture_reward_prob_list = temp_capture_reward_prob_list
                    monster.hr_break_name_list = temp_break_name_list
                    monster.hr_break_part_lv_list = temp_break_part_lv_list
                    monster.hr_break_item_id_list_by_part = temp_break_item_id_list_by_part
                    monster.hr_break_num_list_by_part = temp_break_num_list_by_part
                    monster.hr_break_prob_list_by_part = temp_break_prob_list_by_part
                    monster.hr_drop_name_list = temp_drop_name_list
                    monster.hr_drop_item_id_list_by_part = temp_drop_item_id_list_by_part
                    monster.hr_drop_num_list_by_part = temp_drop_num_list_by_part
                    monster.hr_drop_prob_list_by_part = temp_drop_prob_list_by_part
                    monster.hr_palico_reward_item_id_list = temp_palico_reward_item_id_list
                    monster.hr_palico_reward_num_list = temp_palico_reward_num_list
                    monster.hr_palico_reward_prob_list = temp_palico_reward_prob_list

                break

    for i in reversed(range(max_length)):
        if not monster_list[i] is None:
            break
    monster_list = monster_list[:i+1]

    for monster in monster_list:
        if not monster is None:
            monster.clean_up()
    return monster_list

def monster_list_to_json(pedia):
    monster_list = parse_monster_data(pedia)
    large_monster_list = [i for i in monster_list if not i is None and i.is_large_monster]
    small_monster_list = [i for i in monster_list if not i is None and not i.is_large_monster]
    with open('monster/Monster.json', 'w', encoding='utf8') as f:
        monster_list_json = [i if i is None else i.__odict__ for i in monster_list]
        json.dump(monster_list_json, f, ensure_ascii=False, indent=2)
    with open('monster/LargeMonster.json', 'w', encoding='utf8') as f:
        large_monster_list_json = [i if i is None else i.__odict__ for i in large_monster_list]
        json.dump(large_monster_list_json, f, ensure_ascii=False, indent=2)
    with open('monster/SmallMonster.json', 'w', encoding='utf8') as f:
        small_monster_list_json = [i if i is None else i.__odict__ for i in small_monster_list]
        json.dump(small_monster_list_json, f, ensure_ascii=False, indent=2)

def monster_to_json(pedia):
    monster_list = parse_monster_data(pedia)
    for monster in monster_list:
        if monster is None:
            continue
        with open('monster/Monster{:03}.json'.format(monster.enemy_index), 'w', encoding='utf8') as f:
            monster_json = monster.__odict__
            json.dump(monster_json, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    # monster_to_json(pedia)
    monster_list_to_json(pedia)
