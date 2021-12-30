import sys
sys.path.append('..')

import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualArmorData(OrderedAttibuteClass):
    def __init__(self, type, id):
        self.type = type
        self.name = {'zh':None, 'en':None, 'ja':None}
        # self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = id
        self.sort_id = None
        self.rare_type = None
        self.is_valid = None
        self.series = None
        self.model_id = None
        self.forge_val = None
        self.buy_val = None
        self.sexual_equipable = None
        self.def_val = None
        self.fire_reg_val = None
        self.water_reg_val = None
        self.ice_reg_val = None
        self.thunder_reg_val = None
        self.dragon_reg_val = None
        self.buildup_table = None
        self.buff_formula = None
        self.decorations_num_list = []
        self.skill_list = []
        self.skill_lv_list = []

        self.forge_item_flag = None
        self.forge_enemy_is_large = None
        self.forge_enemy_flag = None
        self.forge_progress_flag = None
        self.forge_item = []
        self.forge_item_num = []
        self.forge_material_category = None
        self.forge_material_category_num = None
        self.forge_output_item = []
        self.forge_output_item_num = []

class IndividualArmorSeriesData(OrderedAttibuteClass):
    def __init__(self, series_id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        # self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = series_id
        self.difficulty_group = None
        self.is_collabo = None
        self.sort_id = None
        self.overwear_sort_id = None
        self.sexual_enable = None
        self.head = None
        self.chest = None
        self.arm = None
        self.waist = None
        self.leg = None

def parse_armor_data(armor_type, name_list, data_list, product_list):
    max_length = 1000
    armor_list = [None] * max_length

    for name in name_list:
        if name.name.startswith('A_' + armor_type) and not 'Rejected' in name.content[0]:
            id = int(name.name.split('_')[2])
            armor_list[id] = IndividualArmorData(armor_type, id)
            armor_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            armor_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            armor_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    for data in data_list:
        if not data.pl_armor_id is None and data.pl_armor_id.startswith(armor_type):
            id = int(data.pl_armor_id.split('(')[1].split(')')[0])
            if not armor_list[id] is None:
                armor_list[id].sort_id = data.sort_id
                armor_list[id].rare_type = data.rare
                armor_list[id].is_valid = data.is_valid
                armor_list[id].series = data.series
                armor_list[id].model_id = data.model_id
                armor_list[id].forge_val = data.value
                armor_list[id].buy_val = data.buy_value
                armor_list[id].sexual_equipable = data.sexual_equipable
                armor_list[id].def_val = data.def_val
                armor_list[id].fire_reg_val = data.fire_reg_val
                armor_list[id].water_reg_val = data.water_reg_val
                armor_list[id].ice_reg_val = data.ice_reg_val
                armor_list[id].thunder_reg_val = data.thunder_reg_val
                armor_list[id].dragon_reg_val = data.dragon_reg_val
                armor_list[id].buildup_table = data.buildup_table
                armor_list[id].buff_formula = data.buff_formula
                armor_list[id].decorations_num_list = data.decorations_num_list
                armor_list[id].skill_list = [i for i in data.skill_list if not i is None]
                armor_list[id].skill_lv_list = [i for i in data.skill_lv_list if i != 0]

    for product in product_list:
        if not product.id is None and product.id.startswith(armor_type):
            id = int(product.id.split('(')[1].split(')')[0])
            if not armor_list[id] is None:
                if not product.item_flag is None:
                    armor_list[id].forge_item_flag = int(product.item_flag.split('(')[1].split(')')[0])
                if not product.enemy_flag is None:
                    armor_list[id].forge_enemy_is_large = product.enemy_flag.startswith('Em(')
                    armor_list[id].forge_enemy_flag = int(product.enemy_flag.split('(')[1].split(')')[0])
                armor_list[id].forge_progress_flag = product.progress_flag
                armor_list[id].forge_item = [int(i.split('(')[1].split(')')[0]) for i in product.item if not i is None]
                armor_list[id].forge_item_num = [i for i in product.item_num if i != 0]
                armor_list[id].forge_material_category = product.material_category
                armor_list[id].forge_material_category_num = product.material_category_num
                armor_list[id].forge_output_item = [int(i.split('(')[1].split(')')[0]) for i in product.output_item if not i is None]
                armor_list[id].forge_output_item_num = [i for i in product.output_item_num if i != 0]

    return armor_list

def parse_armor_series_data(pedia):
    max_length = 1000
    armor_series_list = [None] * max_length

    armor_head_list = parse_armor_data('Head', pedia.armor_head_name_msg.entries, pedia.armor.param, pedia.armor_product.param)
    armor_chest_list = parse_armor_data('Chest', pedia.armor_chest_name_msg.entries, pedia.armor.param, pedia.armor_product.param)
    armor_arm_list = parse_armor_data('Arm', pedia.armor_arm_name_msg.entries, pedia.armor.param, pedia.armor_product.param)
    armor_waist_list = parse_armor_data('Waist', pedia.armor_waist_name_msg.entries, pedia.armor.param, pedia.armor_product.param)
    armor_leg_list = parse_armor_data('Leg', pedia.armor_leg_name_msg.entries, pedia.armor.param, pedia.armor_product.param)

    name_list = pedia.armor_series_name_msg.entries
    for name in name_list:
        if parse_data_utils.verify_msg_name(name, 'ArmorSeries'):
            id = int(name.name.split('_')[2])
            armor_series_list[id] = IndividualArmorSeriesData(id)
            armor_series_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            armor_series_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            armor_series_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    data_list = pedia.armor_series.param
    for data in data_list:
        if not data.armor_series is None:
            id = data.armor_series
            if not armor_series_list[id] is None:
                armor_series_list[id].difficulty_group = data.difficulty_group
                armor_series_list[id].is_collabo = data.is_collabo
                armor_series_list[id].sort_id = data.index
                armor_series_list[id].overwear_sort_id = data.overwear_sort_index
                armor_series_list[id].sexual_enable = data.sexual_enable

    for i in range(max_length):
        if not armor_series_list[i] is None:
            armor_series_list[i].head = armor_head_list[i]
            armor_series_list[i].chest = armor_chest_list[i]
            armor_series_list[i].arm = armor_arm_list[i]
            armor_series_list[i].waist = armor_waist_list[i]
            armor_series_list[i].leg = armor_leg_list[i]

    for i in reversed(range(max_length)):
        if not armor_series_list[i] is None:
            break
    armor_series_list = armor_series_list[:i+1]
    return armor_series_list

def armor_series_list_to_json(pedia):
    armor_series_list = parse_armor_series_data(pedia)
    with open('armor/ArmorSeries.json', 'w', encoding='utf8') as f:
        armor_series_list_json = [i if i is None else i.__odict__ for i in armor_series_list]
        for armor_series_json in armor_series_list_json:
            if armor_series_json is None:
                continue
            if not armor_series_json['head'] is None:
                armor_series_json['head'] = armor_series_json['head'].__odict__
            if not armor_series_json['chest'] is None:
                armor_series_json['chest'] = armor_series_json['chest'].__odict__
            if not armor_series_json['arm'] is None:
                armor_series_json['arm'] = armor_series_json['arm'].__odict__
            if not armor_series_json['waist'] is None:
                armor_series_json['waist'] = armor_series_json['waist'].__odict__
            if not armor_series_json['leg'] is None:
                armor_series_json['leg'] = armor_series_json['leg'].__odict__
        json.dump(armor_series_list_json, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    armor_series_list_to_json(pedia)
