import sys
sys.path.append('..')

import re
import pickle
import json
import utils
from utils import OrderedAttibuteClass
from pedia import *
from collections import OrderedDict
import parse_data_utils

class IndividualWeaponData(OrderedAttibuteClass):
    def __init__(self, type, id):
        self.type = type

        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}

        ## From base data
        self.id = id
        self.sort_id = None
        self.rare_type = None
        self.model_id = None
        self.forge_val = None
        self.upgrade_val = None
        self.buy_val = None
        self.atk = None
        self.critical_rate = None
        self.def_bonus = None
        self.hyakuryu_skill_id_list = []
        self.slot_num_list = []

        # Element weapon (every type except light bowgun and heavy bowgun)
        self.main_element_type = None
        self.main_element_val = None

        # Close range weapon (every type except light bowgun, heavy bowgun, and bow)
        self.sharpness_val_list = []
        self.takumi_val_list = []

        # Slash axe only
        self.slash_axe_bottle_type = None
        self.slash_axe_bottle_element_val = None

        # Gunlance only
        self.gun_lance_fire_type = None
        self.gun_lance_fire_lv = None

        # Dual blades only
        self.sub_element_type = None
        self.sub_element_val = None

        # Horn (a.k.a. melody horn) only
        self.horn_melody_type_list = []

        # Insect glaive only
        self.insect_glaive_insect_lv = None

        # Charge axe (a.k.a. charge blade) only
        self.charge_axe_bottle_type = None

        # Bullet weapon only (light bowgun and heavy bowgun)
        self.fluctuation = None
        self.reload = None
        self.recoil = None
        self.kakusan_type = None
        self.bullet_equip_flag_list = [] # Dropped eventually
        self.bullet_num_list = [] # Dropped eventually
        self.bullet_type_list = [] # Dropped eventually
        self.bullet_dict = OrderedDict()

        # Light bowgun only
        self.rapid_shot_list = [] # Dropped eventually
        self.light_bowgun_unique_bullet_type = None

        # Heavy bowgun only
        self.heavy_bowgun_unique_bullet_type = None

        # Bow only
        self.bow_bottle_power_up_type_list = []
        self.bow_bottle_equip_flag_list = [] # Dropped eventually
        self.bow_bottle_equip_flag_dict = OrderedDict()
        self.bow_default_charge_lv_limit = None
        self.bow_charge_type_list = []
        self.bow_curve_type = None

        ## From product data (a.k.a. forge materials)
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

        ## From change data (a.k.a. layer materials)
        self.layer_item_flag = None
        self.layer_enemy_is_large = None
        self.layer_enemy_flag = None
        self.layer_progress_flag = None
        self.layer_item = []
        self.layer_item_num = []
        self.layer_material_category = None
        self.layer_material_category_num = None

        ## From process data (a.k.a. upgrade materials)
        self.upgrade_item_flag = None
        self.upgrade_enemy_is_large = None
        self.upgrade_enemy_flag = None
        self.upgrade_progress_flag = None
        self.upgrade_item = []
        self.upgrade_item_num = []
        self.upgrade_material_category = None
        self.upgrade_material_category_num = None
        self.upgrade_output_item = []
        self.upgrade_output_item_num = []

        ## From tree data
        self.tree_id = None
        self.index_in_tree = None
        self.village_progress = None
        self.hall_progress = None
        self.next_weapon_tree_id_list = []
        self.next_weapon_index_in_tree_list = []
        self.prev_weapon_tree_id = None
        self.prev_weapon_index_in_tree = None

    def clean_up(self):
        if self.type == 'Bow':
            self.bow_bottle_equip_flag_dict['CloseRange'] = self.bow_bottle_equip_flag_list[0]
            self.bow_bottle_equip_flag_dict['Power'] = self.bow_bottle_equip_flag_list[1]
            self.bow_bottle_equip_flag_dict['Poison'] = self.bow_bottle_equip_flag_list[2]
            self.bow_bottle_equip_flag_dict['Para'] = self.bow_bottle_equip_flag_list[3]
            self.bow_bottle_equip_flag_dict['Sleep'] = self.bow_bottle_equip_flag_list[4]
            self.bow_bottle_equip_flag_dict['Blast'] = self.bow_bottle_equip_flag_list[5]
            self.bow_bottle_equip_flag_dict['Exhaust'] = self.bow_bottle_equip_flag_list[6]
        elif self.type == 'LightBowgun' or self.type == 'HeavyBowgun':
            keys = list(parse_data_utils.bullet_name_dict.keys())
            for i in range(len(keys)):
                self.bullet_dict[keys[i]] = []
                self.bullet_dict[keys[i]].append(self.bullet_equip_flag_list[i+1])
                self.bullet_dict[keys[i]].append(self.bullet_num_list[i+1] * self.bullet_equip_flag_list[i+1])
                bullet_type = self.bullet_type_list[i+1]
                if bullet_type == 'MovingShot':
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(False)
                    self.bullet_dict[keys[i]].append(False)
                elif bullet_type == 'MovingReload':
                    self.bullet_dict[keys[i]].append(False)
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(False)
                elif bullet_type == 'MovingShotReload':
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(False)
                elif bullet_type == 'MovingShotReloadSingleAuto':
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                    self.bullet_dict[keys[i]].append(True and self.bullet_equip_flag_list[i+1])
                else:
                    self.bullet_dict[keys[i]].append(False)
                    self.bullet_dict[keys[i]].append(False)
                    self.bullet_dict[keys[i]].append(False)
                self.bullet_dict[keys[i]].append(keys[i] in self.rapid_shot_list)

        delattr(self, 'bow_bottle_equip_flag_list')
        delattr(self, 'bullet_equip_flag_list')
        delattr(self, 'bullet_num_list')
        delattr(self, 'bullet_type_list')
        delattr(self, 'rapid_shot_list')

class IndividualHornMelodyData(OrderedAttibuteClass):
    def __init__(self, id):
        self.name = {'zh':None, 'en':None, 'ja':None}
        self.explain = {'zh':None, 'en':None, 'ja':None}

        self.id = id

def parse_weapon_data(weapon_type, weapon_data):
    max_length = 1000
    weapon_list = [None] * max_length

    name_list = weapon_data.name.entries
    for name in name_list:
        if name.name.startswith('W_' + weapon_type) and name.content[0] != '':
            id = int(name.name.split('_')[2])
            weapon_list[id] = IndividualWeaponData(weapon_type, id)
            weapon_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
            weapon_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
            weapon_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))

    explain_list = weapon_data.explain.entries
    for explain in explain_list:
        if explain.name.startswith('W_' + weapon_type) and explain.content[0] != '':
            id = int(explain.name.split('_')[2])
            if not weapon_list[id] is None:
                weapon_list[id].explain['zh'] = parse_data_utils.beautify_string(explain.content[13].replace('\r\n', ''))
                weapon_list[id].explain['en'] = explain.content[1].replace('\r\n', ' ')
                weapon_list[id].explain['ja'] = parse_data_utils.beautify_string(explain.content[0].replace('\r\n', ''))

    base_list = weapon_data.base_data.param
    for base_data in base_list:
        if not base_data.id is None and base_data.id.startswith(weapon_type):
            id = int(base_data.id.split('(')[1].split(')')[0])
            if not weapon_list[id] is None:
                weapon_list[id].sort_id = base_data.sort_id
                weapon_list[id].rare_type = base_data.rare_type
                weapon_list[id].model_id = base_data.model_id
                weapon_list[id].forge_val = int(base_data.base_val * 1.5)
                weapon_list[id].upgrade_val = base_data.base_val
                weapon_list[id].buy_val = base_data.buy_val
                weapon_list[id].atk = base_data.atk
                weapon_list[id].critical_rate = base_data.critical_rate
                weapon_list[id].def_bonus = base_data.def_bonus
                weapon_list[id].hyakuryu_skill_id_list = base_data.hyakuryu_skill_id_list
                weapon_list[id].slot_num_list = base_data.slot_num_list

                if hasattr(base_data, 'main_element_type'):
                    weapon_list[id].main_element_type = base_data.main_element_type
                if hasattr(base_data, 'main_element_val'):
                    weapon_list[id].main_element_val = base_data.main_element_val
                if hasattr(base_data, 'sharpness_val_list'):
                    weapon_list[id].sharpness_val_list = base_data.sharpness_val_list
                if hasattr(base_data, 'takumi_val_list'):
                    weapon_list[id].takumi_val_list = [0,0,0] + base_data.takumi_val_list # Now takumi list also has 7 entries
                if hasattr(base_data, 'slash_axe_bottle_type'):
                    weapon_list[id].slash_axe_bottle_type = base_data.slash_axe_bottle_type
                if hasattr(base_data, 'slash_axe_bottle_element_val'):
                    weapon_list[id].slash_axe_bottle_element_val = base_data.slash_axe_bottle_element_val
                if hasattr(base_data, 'gun_lance_fire_type'):
                    weapon_list[id].gun_lance_fire_type = base_data.gun_lance_fire_type
                if hasattr(base_data, 'gun_lance_fire_lv'):
                    weapon_list[id].gun_lance_fire_lv = base_data.gun_lance_fire_lv
                if hasattr(base_data, 'sub_element_type'):
                    weapon_list[id].sub_element_type = base_data.sub_element_type
                if hasattr(base_data, 'sub_element_val'):
                    weapon_list[id].sub_element_val = base_data.sub_element_val
                if hasattr(base_data, 'horn_melody_type_list'):
                    weapon_list[id].horn_melody_type_list = base_data.horn_melody_type_list
                if hasattr(base_data, 'insect_glaive_insect_lv'):
                    weapon_list[id].insect_glaive_insect_lv = base_data.insect_glaive_insect_lv
                if hasattr(base_data, 'charge_axe_bottle_type'):
                    weapon_list[id].charge_axe_bottle_type = base_data.charge_axe_bottle_type
                if hasattr(base_data, 'fluctuation'):
                    weapon_list[id].fluctuation = base_data.fluctuation
                if hasattr(base_data, 'reload'):
                    weapon_list[id].reload = base_data.reload
                if hasattr(base_data, 'recoil'):
                    weapon_list[id].recoil = base_data.recoil
                if hasattr(base_data, 'kakusan_type'):
                    weapon_list[id].kakusan_type = base_data.kakusan_type
                if hasattr(base_data, 'bullet_equip_flag_list'):
                    weapon_list[id].bullet_equip_flag_list = base_data.bullet_equip_flag_list
                if hasattr(base_data, 'bullet_num_list'):
                    weapon_list[id].bullet_num_list = base_data.bullet_num_list
                if hasattr(base_data, 'bullet_type_list'):
                    weapon_list[id].bullet_type_list = base_data.bullet_type_list
                if hasattr(base_data, 'rapid_shot_list'):
                    weapon_list[id].rapid_shot_list = base_data.rapid_shot_list
                if hasattr(base_data, 'unique_bullet'):
                    weapon_list[id].light_bowgun_unique_bullet_type = base_data.unique_bullet
                if hasattr(base_data, 'heavy_bowgun_unique_bullet_type'):
                    weapon_list[id].heavy_bowgun_unique_bullet_type = base_data.heavy_bowgun_unique_bullet_type
                if hasattr(base_data, 'bow_bottle_power_up_type_list'):
                    weapon_list[id].bow_bottle_power_up_type_list = base_data.bow_bottle_power_up_type_list
                if hasattr(base_data, 'bow_bottle_equip_flag_list'):
                    weapon_list[id].bow_bottle_equip_flag_list = base_data.bow_bottle_equip_flag_list
                if hasattr(base_data, 'bow_default_charge_lv_limit'):
                    weapon_list[id].bow_default_charge_lv_limit = base_data.bow_default_charge_lv_limit
                if hasattr(base_data, 'bow_charge_type_list'):
                    weapon_list[id].bow_charge_type_list = base_data.bow_charge_type_list
                if hasattr(base_data, 'bow_curve_type'):
                    weapon_list[id].bow_curve_type = base_data.bow_curve_type

    product_list = weapon_data.product.param
    for product in product_list:
        if not product.id is None and product.id.startswith(weapon_type):
            id = int(product.id.split('(')[1].split(')')[0])
            if not weapon_list[id] is None:
                if not product.item_flag is None:
                    weapon_list[id].forge_item_flag = int(product.item_flag.split('(')[1].split(')')[0])
                if not product.enemy_flag is None:
                    weapon_list[id].forge_enemy_is_large = product.enemy_flag.startswith('Em(')
                    weapon_list[id].forge_enemy_flag = int(product.enemy_flag.split('(')[1].split(')')[0])
                weapon_list[id].forge_progress_flag = product.progress_flag
                weapon_list[id].forge_item = [int(i.split('(')[1].split(')')[0]) for i in product.item if not i is None]
                weapon_list[id].forge_item_num = [i for i in product.item_num if i != 0]
                weapon_list[id].forge_material_category = product.material_category
                weapon_list[id].forge_material_category_num = product.material_category_num
                weapon_list[id].forge_output_item = [int(i.split('(')[1].split(')')[0]) for i in product.output_item if not i is None]
                weapon_list[id].forge_output_item_num = [i for i in product.output_item_num if i != 0]

    change_list = weapon_data.change.param
    for change in change_list:
        if not change.id is None and change.id.startswith(weapon_type):
            id = int(change.id.split('(')[1].split(')')[0])
            if not weapon_list[id] is None:
                if not change.item_flag is None:
                    weapon_list[id].layer_item_flag = int(change.item_flag.split('(')[1].split(')')[0])
                if not change.enemy_flag is None:
                    weapon_list[id].layer_enemy_is_large = change.enemy_flag.startswith('Em(')
                    weapon_list[id].layer_enemy_flag = int(change.enemy_flag.split('(')[1].split(')')[0])
                weapon_list[id].layer_progress_flag = change.progress_flag
                weapon_list[id].layer_item = [int(i.split('(')[1].split(')')[0]) for i in change.item if not i is None]
                weapon_list[id].layer_item_num = [i for i in change.item_num if i != 0]
                weapon_list[id].layer_material_category = change.material_category
                weapon_list[id].layer_material_category_num = change.material_category_num

    process_list = weapon_data.process.param
    for process in process_list:
        if not process.id is None and process.id.startswith(weapon_type):
            id = int(process.id.split('(')[1].split(')')[0])
            if not weapon_list[id] is None:
                if not process.item_flag is None:
                    weapon_list[id].upgrade_item_flag = int(process.item_flag.split('(')[1].split(')')[0])
                if not process.enemy_flag is None:
                    weapon_list[id].upgrade_enemy_is_large = process.enemy_flag.startswith('Em(')
                    weapon_list[id].upgrade_enemy_flag = int(process.enemy_flag.split('(')[1].split(')')[0])
                weapon_list[id].upgrade_progress_flag = process.progress_flag
                weapon_list[id].upgrade_item = [int(i.split('(')[1].split(')')[0]) for i in process.item if not i is None]
                weapon_list[id].upgrade_item_num = [i for i in process.item_num if i != 0]
                weapon_list[id].upgrade_material_category = process.material_category
                weapon_list[id].upgrade_material_category_num = process.material_category_num
                weapon_list[id].upgrade_output_item = [int(i.split('(')[1].split(')')[0]) for i in process.output_item if not i is None]
                weapon_list[id].upgrade_output_item_num = [i for i in process.output_item_num if i != 0]

    tree_list = weapon_data.tree.param
    for tree in tree_list:
        if not tree.weapon_id is None and tree.weapon_id.startswith(weapon_type):
            id = int(tree.weapon_id.split('(')[1].split(')')[0])
            if not weapon_list[id] is None:
                weapon_list[id].tree_id = tree.tree_type
                weapon_list[id].index_in_tree = tree.index
                weapon_list[id].village_progress = tree.village_progress
                weapon_list[id].hall_progress = tree.hall_progress
                weapon_list[id].next_weapon_tree_id_list = [i for i in tree.next_weapon_type_list if not i is None]
                weapon_list[id].next_weapon_index_in_tree_list = [i for i in tree.next_weapon_index_list if i != -1]
                weapon_list[id].prev_weapon_tree_id = tree.prev_weapon_type
                if tree.prev_weapon_index != -1:
                    weapon_list[id].prev_weapon_index_in_tree = tree.prev_weapon_index

    for i in reversed(range(max_length)):
        if not weapon_list[i] is None:
            break
    weapon_list = weapon_list[:i+1]
    for weapon in weapon_list:
        if weapon.forge_progress_flag is None:
            weapon.forge_val = None
        if weapon.upgrade_progress_flag is None:
            weapon.upgrade_val = None
        if weapon.buy_val == 0:
            weapon.buy_val = None

    for weapon in weapon_list:
        if not weapon is None:
            weapon.clean_up()
    return weapon_list

def parse_horn_melody_data(melody_name_list):
    max_length = 100
    horn_melody_list = [None] * max_length
    for name in melody_name_list:
        if parse_data_utils.verify_msg_name(name, 'Horn_UniqueParam'):
            if name.name.endswith('Name'):
                id = int(name.name.split('_')[2])
                horn_melody_list[id] = IndividualHornMelodyData(id)
                horn_melody_list[id].name['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                horn_melody_list[id].name['en'] = name.content[1].replace('\r\n', ' ')
                horn_melody_list[id].name['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
            elif name.name.endswith('Explain'):
                id = int(name.name.split('_')[2])
                if not horn_melody_list[id] is None:
                    horn_melody_list[id].explain['zh'] = parse_data_utils.beautify_string(name.content[13].replace('\r\n', ''))
                    horn_melody_list[id].explain['en'] = name.content[1].replace('\r\n', ' ')
                    horn_melody_list[id].explain['ja'] = parse_data_utils.beautify_string(name.content[0].replace('\r\n', ''))
    for i in reversed(range(max_length)):
        if not horn_melody_list[i] is None:
            break
    horn_melody_list = horn_melody_list[:i+1]
    return horn_melody_list

def weapon_list_to_json(pedia):
    weapon_type_list = ['GreatSword', 'ShortSword', 'Hammer', 'Lance', 'LongSword', 'SlashAxe', 'GunLance',\
                        'DualBlades', 'Horn', 'InsectGlaive', 'ChargeAxe', 'LightBowgun', 'HeavyBowgun', 'Bow']
    pattern = re.compile(r'(?<!^)(?=[A-Z])')
    for weapon_type in weapon_type_list:
        weapon_data = eval(('pedia.' + pattern.sub('_', weapon_type).lower())) # To snake case
        weapon_list = parse_weapon_data(weapon_type, weapon_data)
        with open('weapon/{}.json'.format(weapon_type), 'w', encoding='utf8') as f:
            json.dump([i if i is None else i.__odict__ for i in weapon_list], f, ensure_ascii=False, indent=2)

def horn_melody_to_json(pedia):
    horn_melody_list = parse_horn_melody_data(pedia.horn_melody.entries)
    with open('weapon/HornMelody.json', 'w', encoding='utf8') as f:
        json.dump([i if i is None else i.__odict__ for i in horn_melody_list], f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    with open('pedia.pickle', 'rb') as f:
        pedia = pickle.load(f)

    weapon_list_to_json(pedia)
    horn_melody_to_json(pedia)
