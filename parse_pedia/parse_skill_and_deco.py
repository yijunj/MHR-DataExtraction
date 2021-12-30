import sys
sys.path.append('..')

import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualSkillData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}
        self.detail = {'zh':[], 'en':[], 'ja':[]}

        self.id = id
        self.max_level = None
        self.icon_color = None

class IndividualSkillHyakuryuData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = id
        self.icon_color = None
        self.cost = None
        self.forge_item = []
        self.forge_item_num = []

class IndividualDecorationData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}

        self.id = id
        self.sort_id = None
        self.rare_type = None
        self.icon_color = None
        self.decoration_lv = None
        self.skill_id_list = []
        self.skill_lv_list = []
        self.forge_val = None
        self.sell_val = None

        self.forge_item_flag = None
        self.forge_enemy_is_large = None
        self.forge_enemy_flag = None
        self.forge_progress_flag = None
        self.forge_item = []
        self.forge_item_num = []

def parse_skill_data(pedia):
    max_length = 1000
    skill_list = [None] * max_length

    name_list = pedia.player_skill_name_msg.entries
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'PlayerSkill'):
            id = int(name.name.split('_')[1])
            skill_list[id] = IndividualSkillData(id)
            skill_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            skill_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            skill_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    explain_list = pedia.player_skill_explain_msg.entries
    for explain in explain_list:
        if parse_data_utils.verify_msg_name(explain, 'PlayerSkill'):
            id = int(explain.name.split('_')[1])
            if not skill_list[id] is None:
                skill_list[id].explain['zh'] = parse_data_utils.beautify_string(explain.content[13].replace('\r\n', ''))
                skill_list[id].explain['en'] = explain.content[1].replace('\r\n', ' ')
                skill_list[id].explain['ja'] = parse_data_utils.beautify_string(explain.content[0].replace('\r\n', ''))

    detail_list = pedia.player_skill_detail_msg.entries
    for detail in detail_list:
        if parse_data_utils.verify_msg_name(detail, 'PlayerSkill'):
            id = int(detail.name.split('_')[1])
            # level = int(detail.name.split('_')[2])
            if not skill_list[id] is None:
                skill_list[id].detail['zh'].append(parse_data_utils.beautify_string(detail.content[13].replace('\r\n', '')))
                skill_list[id].detail['en'].append(detail.content[1].replace('\r\n', ' '))
                skill_list[id].detail['ja'].append(parse_data_utils.beautify_string(detail.content[0].replace('\r\n', '')))

    data_list = pedia.equip_skill.param
    for data in data_list:
        if not data.id is None:
            id = data.id
            if not skill_list[id] is None:
                skill_list[id].max_level = data.max_level
                skill_list[id].icon_color = data.icon_color

    for i in reversed(range(max_length)):
        if not skill_list[i] is None:
            break
    skill_list = skill_list[:i+1]
    return skill_list

def parse_skill_hyakuryu_data(pedia):
    max_length = 1000
    skill_hyakuryu_list = [None] * max_length

    name_list = pedia.hyakuryu_skill_name_msg.entries
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'HyakuryuSkill'):
            id = int(name.name.split('_')[1])
            skill_hyakuryu_list[id] = IndividualSkillHyakuryuData(id)
            skill_hyakuryu_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            skill_hyakuryu_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            skill_hyakuryu_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    explain_list = pedia.hyakuryu_skill_explain_msg.entries
    for explain in explain_list:
        if parse_data_utils.verify_msg_name(explain, 'HyakuryuSkill'):
            if not skill_hyakuryu_list[id] is None:
                skill_hyakuryu_list[id].explain['zh'] = parse_data_utils.beautify_string(explain.content[13].replace('\r\n', ''))
                skill_hyakuryu_list[id].explain['en'] = explain.content[1].replace('\r\n', ' ')
                skill_hyakuryu_list[id].explain['ja'] = parse_data_utils.beautify_string(explain.content[0].replace('\r\n', ''))

    data_list = pedia.hyakuryu_skill.param
    for data in data_list:
        if not data.id is None:
            id = data.id
            if not skill_hyakuryu_list[id] is None:
                skill_hyakuryu_list[id].icon_color = data.item_color

    product_list = pedia.hyakuryu_skill_recipe.param
    for product in product_list:
        if not product.skill_id is None:
            id = product.skill_id
            if not skill_hyakuryu_list[id] is None:
                skill_hyakuryu_list[id].cost = product.cost
                skill_hyakuryu_list[id].forge_item = [int(i.split('(')[1].split(')')[0]) for i in product.recipe_item_id_list if not i is None]
                skill_hyakuryu_list[id].forge_item_num = [i for i in product.recipe_item_num_list if i != 0]

    for i in reversed(range(max_length)):
        if not skill_hyakuryu_list[i] is None:
            break
    skill_hyakuryu_list = skill_hyakuryu_list[:i+1]
    return skill_hyakuryu_list

def parse_decoration_data(pedia):
    max_length = 1000
    decoration_list = [None] * max_length

    name_list = pedia.decorations_name_msg.entries
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'Decorations'):
            id = int(name.name.split('_')[1])
            decoration_list[id] = IndividualDecorationData(id)
            decoration_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            decoration_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            decoration_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    data_list = pedia.decorations.param
    for data in data_list:
        if not data.id is None:
            id = data.id
            if not decoration_list[id] is None:
                decoration_list[id].sort_id = data.sort_id
                decoration_list[id].rare_type = data.rare
                decoration_list[id].icon_color = data.icon_color
                decoration_list[id].decoration_lv = data.decoration_lv
                decoration_list[id].skill_id_list = [i for i in data.skill_id_list if not i is None]
                decoration_list[id].skill_lv_list = [i for i in data.skill_lv_list if not i is None]
                decoration_list[id].forge_val = data.base_price * 2
                decoration_list[id].sell_val = data.base_price

    product_list = pedia.decorations_product.param
    for product in product_list:
        if not product.id is None:
            id = product.id
            if not decoration_list[id] is None:
                if not product.item_flag is None:
                    decoration_list[id].forge_item_flag = int(product.item_flag.split('(')[1].split(')')[0])
                if not product.enemy_flag is None:
                    decoration_list[id].forge_enemy_is_large = product.enemy_flag.startswith('Em(')
                    decoration_list[id].forge_enemy_flag = int(product.enemy_flag.split('(')[1].split(')')[0])
                decoration_list[id].forge_progress_flag = product.progress_flag
                decoration_list[id].forge_item = [int(i.split('(')[1].split(')')[0]) for i in product.item_id_list if not i is None]
                decoration_list[id].forge_item_num = [i for i in product.item_num_list if i != 0]

    for i in reversed(range(max_length)):
        if not decoration_list[i] is None:
            break
    decoration_list = decoration_list[:i+1]
    return decoration_list

def skill_list_to_json(pedia):
    skill_list = parse_skill_data(pedia)
    with open('skill_and_deco/Skill.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in skill_list], f, ensure_ascii=False, indent=2)

def skill_hyakuryu_list_to_json(pedia):
    skill_hyakuryu_list = parse_skill_hyakuryu_data(pedia)
    with open('skill_and_deco/SkillHyakuryu.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in skill_hyakuryu_list], f, ensure_ascii=False, indent=2)

def deco_list_to_data(pedia):
    decoration_list = parse_decoration_data(pedia)
    with open('skill_and_deco/Decoration.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in decoration_list], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    skill_list_to_json(pedia)
    skill_hyakuryu_list_to_json(pedia)
    deco_list_to_data(pedia)
