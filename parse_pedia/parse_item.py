import sys
sys.path.append('..')

import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualItemData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = id
        self.sort_id = None
        self.rare_type = None
        self.type = None
        self.cariable_filter = None
        self.pl_max_count = None
        self.ot_max_count = None
        self.supply = None
        self.infinite = None
        self.default = None
        self.icon_can_eat = None
        self.effect_rare = None
        self.sell_val = None
        self.buy_val = None
        self.item_action_type = None
        self.rank_type = None
        self.item_group = None
        self.category_worth = None
        self.material_category = []
        self.evaluation_value = None

class IndividualEnvironmentCreatureData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = id

class IndividualMaterialCategoryData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.id = id

def parse_item_data(pedia):
    max_length = 10000
    max_length_ec = 100
    item_list = [None] * max_length
    ec_list = [None] * max_length_ec

    name_list = pedia.items_name_msg.entries
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'I'):
            if name.name.startswith('I_EC'):
                id = int(name.name.split('_')[2])
                ec_list[id] = IndividualEnvironmentCreatureData(id)
                ec_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                ec_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
                ec_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            else:
                id = int(name.name.split('_')[1])
                item_list[id] = IndividualItemData(id)
                item_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                item_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
                item_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    explain_list = pedia.items_explain_msg.entries
    for explain in explain_list:
        if parse_data_utils.verify_msg_name(explain, 'I'):
            if explain.name.startswith('I_EC'):
                id = int(explain.name.split('_')[2])
                if not ec_list[id] is None:
                    ec_list[id].explain['zh'] = parse_data_utils.beautify_string(explain.content[13].replace('\r\n', ''))
                    ec_list[id].explain['en'] = explain.content[1].replace('\r\n', ' ')
                    ec_list[id].explain['ja'] = parse_data_utils.beautify_string(explain.content[0].replace('\r\n', ''))
            else:
                id = int(explain.name.split('_')[1])
                if not item_list[id] is None:
                    item_list[id].explain['zh'] = parse_data_utils.beautify_string(explain.content[13].replace('\r\n', ''))
                    item_list[id].explain['en'] = explain.content[1].replace('\r\n', ' ')
                    item_list[id].explain['ja'] = parse_data_utils.beautify_string(explain.content[0].replace('\r\n', ''))

    data_list = pedia.item_list.param
    for data in data_list:
        if not data.id is None and data.id.startswith('Normal'):
            id = int(data.id.split('(')[1].split(')')[0])
            if not item_list[id] is None:
                item_list[id].sort_id = data.sort_id
                item_list[id].rare_type = data.rare
                item_list[id].type = data.type
                item_list[id].cariable_filter = data.cariable_filter
                item_list[id].pl_max_count = data.pl_max_count
                item_list[id].ot_max_count = data.ot_max_count
                item_list[id].supply = data.supply
                item_list[id].infinite = data.infinite
                item_list[id].default = data.default
                item_list[id].icon_can_eat = data.icon_can_eat
                item_list[id].effect_rare = data.effect_rare
                item_list[id].sell_val = data.sell_price
                item_list[id].buy_val = data.buy_price
                item_list[id].item_action_type = data.item_action_type
                item_list[id].rank_type = data.rank_type
                item_list[id].item_group = data.item_group
                item_list[id].category_worth = data.category_worth
                item_list[id].material_category = data.material_category
                item_list[id].evaluation_value = data.evaluation_value

    for i in reversed(range(max_length)):
        if not item_list[i] is None:
            break
    item_list = item_list[:i+1]
    for i in reversed(range(max_length_ec)):
        if not ec_list[i] is None:
            break
    ec_list = ec_list[:i+1]
    return item_list, ec_list

def parse_material_category_data(mat_cat_name_list):
    max_length = 100
    mat_cat_list = [None] * max_length
    for name in mat_cat_name_list:
        if parse_data_utils.verify_msg_name(name, 'ICT_Name'):
            id = int(name.name.split('_')[2])
            mat_cat_list[id] = IndividualMaterialCategoryData(id)
            mat_cat_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            mat_cat_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            mat_cat_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
    for i in reversed(range(max_length)):
        if not mat_cat_list[i] is None:
            break
    mat_cat_list = mat_cat_list[:i+1]
    return mat_cat_list

def item_list_to_json(pedia):
    item_list, ec_list = parse_item_data(pedia)
    with open('item/Item.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in item_list], f, ensure_ascii=False, indent=2)
    with open('item/EnviromentalCreature.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in ec_list], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    item_list_to_json(pedia)
