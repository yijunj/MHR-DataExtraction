import sys
sys.path.append('..')

import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualQuestData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.quest_giver = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}
        self.detail = {'zh':None, 'en':None, 'ja':None}
        self.fail_condition = {'zh':None, 'en':None, 'ja':None}

        self.id = id
        self.sort_id = None
        self.quest_type = None
        self.quest_level = None
        self.enemy_level = None
        self.map_no = None
        self.time_limit = None
        self.quest_life = None
        self.target_is_large_monster_list = []
        self.target_enemy_type_id_list = []
        self.all_enemy_type_id_list = []
        self.scale_table_id_list = [] # Dropped eventually
        self.scale_base_list = [] # Dropped eventually
        self.small_crown_rate_list = []
        self.large_crown_rate_list = []
        self.target_item_id_list = []
        self.target_num_list = []
        self.reward_item_id_list = []
        self.reward_num_list = []
        self.reward_prob_list = []
        self.reward_money = None
        self.reward_village_point = None
        self.reward_rank_point = None

    def clean_up(self):
        delattr(self, 'scale_table_id_list')
        delattr(self, 'scale_base_list')

def get_scale_table(pedia):
    max_length = 100
    scale_table_list = [None] * max_length

    for table in pedia.random_scale.random_scale_table_data_list:
        scale_table_list[table.type] = {'scale':[], 'rate':[]}
        for scale_data in table.scale_and_rate_data:
            scale_table_list[table.type]['scale'].append(scale_data.scale)
            scale_table_list[table.type]['rate'].append(scale_data.rate)

    for i in reversed(range(max_length)):
        if not scale_table_list[i] is None:
            break
    scale_table_list = scale_table_list[:i+1]
    return scale_table_list

def get_size_boarder(pedia):
    size_boarder_dict = {}
    for data in pedia.size_list.size_info_param:
        size_boarder_dict[data.em_type] = data
    return size_boarder_dict

def get_reward_table(pedia):
    reward_table_dict = {}
    for data in pedia.quest_reward_table.param:
        reward_table_dict[data.reward_tbl] = data
    return reward_table_dict

def parse_quest_data(pedia, quest_type):
    max_length = 1000
    quest_list = [None] * max_length

    id = -1
    name_list = eval('pedia.quest_{}_msg.entries'.format(quest_type))
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'QN'):
            if name.name.endswith('_01'):
                id += 1
                quest_id = int(name.name.split('_')[0][2:])
                quest_list[id] = IndividualQuestData(id)
                quest_list[id].sort_id = quest_id
                quest_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                quest_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
                quest_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            elif name.name.endswith('_02'):
                if quest_id == int(name.name.split('_')[0][2:]):
                    quest_list[id].quest_giver['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                    quest_list[id].quest_giver['en'] = name.content[1].replace('\r\n', ' ')
                    quest_list[id].quest_giver['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            elif name.name.endswith('_03'):
                if quest_id == int(name.name.split('_')[0][2:]):
                    quest_list[id].explain['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                    quest_list[id].explain['en'] = name.content[1].replace('\r\n', ' ')
                    quest_list[id].explain['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            elif name.name.endswith('_04'):
                if quest_id == int(name.name.split('_')[0][2:]):
                    quest_list[id].detail['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                    quest_list[id].detail['en'] = name.content[1].replace('\r\n', ' ')
                    quest_list[id].detail['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            elif name.name.endswith('_05'):
                if quest_id == int(name.name.split('_')[0][2:]):
                    quest_list[id].fail_condition['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                    quest_list[id].fail_condition['en'] = name.content[1].replace('\r\n', ' ')
                    quest_list[id].fail_condition['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    for i in reversed(range(max_length)):
        if not quest_list[i] is None:
            break
    quest_list = quest_list[:i+1]

    for quest_from_pedia in pedia.normal_quest_data.param:
        for quest in quest_list:
            if quest.sort_id == quest_from_pedia.quest_no:
                quest.quest_type = quest_from_pedia.quest_type[0]
                quest.quest_level = quest_from_pedia.quest_level
                quest.enemy_level = quest_from_pedia.enemy_level
                quest.map_no = quest_from_pedia.map_no
                quest.time_limit = quest_from_pedia.time_limit
                quest.quest_life = quest_from_pedia.quest_life

                quest.target_is_large_monster_list = [i.startswith('Em(') for i in quest_from_pedia.tgt_em_type if i != 'Em(0)']
                quest.target_enemy_type_id_list = [int(i.split('(')[1].split(')')[0]) for i in quest_from_pedia.tgt_em_type]
                quest.target_enemy_type_id_list = [i for i in quest.target_enemy_type_id_list if i != 0]
                quest.all_enemy_type_id_list = [int(i.split('(')[1].split(')')[0]) for i in quest_from_pedia.boss_em_type]
                quest.all_enemy_type_id_list = [i for i in quest.all_enemy_type_id_list if i != 0]
                quest.target_num_list = [i for i in quest_from_pedia.tgt_num if i != 0]
                if quest.target_enemy_type_id_list == []:
                    quest.target_item_id_list = quest_from_pedia.tgt_item_id[:len(quest.target_num_list)]

                quest.reward_money = quest_from_pedia.rem_money
                quest.reward_village_point = quest_from_pedia.rem_village_point
                quest.reward_rank_point = quest_from_pedia.rem_rank_point
                break

    for quest_from_pedia in pedia.normal_quest_data_for_enemy.param:
        for quest in quest_list:
            if quest.sort_id == quest_from_pedia.quest_no:
                quest.scale_table_id_list = quest_from_pedia.scale_tbl[:len(quest.all_enemy_type_id_list)]
                quest.scale_base_list = quest_from_pedia.scale[:len(quest.all_enemy_type_id_list)]
                break

    scale_table_list = get_scale_table(pedia)
    size_boarder_dict = get_size_boarder(pedia)
    for quest in quest_list:
        if len(quest.scale_table_id_list) != len(quest.all_enemy_type_id_list):
            raise Exception('Length of scale table does not match length of monster list')
        quest.small_crown_rate_list = [0] * len(quest.all_enemy_type_id_list)
        quest.large_crown_rate_list = [0] * len(quest.all_enemy_type_id_list)
        for i in range(len(quest.all_enemy_type_id_list)):
            enemy_type_id = quest.all_enemy_type_id_list[i]
            scale_table = scale_table_list[quest.scale_table_id_list[i]]
            if not scale_table is None:
                small_boarder = size_boarder_dict['Em({})'.format(enemy_type_id)].small_boarder
                small_boarder /= (quest.scale_base_list[i]/100.0)
                king_boarder = size_boarder_dict['Em({})'.format(enemy_type_id)].king_boarder
                king_boarder /= (quest.scale_base_list[i]/100.0)
                for j in range(len(scale_table['scale'])):
                    if scale_table['scale'][j] <= small_boarder:
                        quest.small_crown_rate_list[i] += scale_table['rate'][j]
                    if scale_table['scale'][j] >= king_boarder:
                        quest.large_crown_rate_list[i] += scale_table['rate'][j]

    reward_table_dict = get_reward_table(pedia)
    for quest in quest_list:
        for reward in pedia.quest_reward.param:
            if reward.quest_id == quest.sort_id:
                if reward.reward_tbl != 0:
                    reward_table = reward_table_dict[reward.reward_tbl]
                    quest.reward_item_id_list = [int(i.split('(')[1].split(')')[0]) for i in reward_table.reward_item_id_list if not i is None]
                    quest.reward_num_list = [i for i in reward_table.reward_num_list if i != 0]
                    quest.reward_prob_list = [i for i in reward_table.reward_prob_list if i != 0]
                break

    for quest in quest_list:
        if not quest is None:
            quest.clean_up()
    return quest_list

def quest_list_to_json(pedia, quest_type):
    quest_list = parse_quest_data(pedia, quest_type.lower())
    with open('quest/Quest{}.json'.format(quest_type), 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in quest_list], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    quest_list_to_json(pedia, 'Hall')
    quest_list_to_json(pedia, 'Village')
    quest_list_to_json(pedia, 'Arena')
    quest_list_to_json(pedia, 'Tutorial')

    # utils.print_hierarchical_object(pedia.quest_reward.param[10])
    # utils.print_hierarchical_object(pedia.quest_reward_table.param[10])
