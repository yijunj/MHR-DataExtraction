import user
import json
from utils import OrderedAttibuteClass
from collections import OrderedDict

weapon_type = 'DualBlades'
filename = 'user\\weapon\\{}\\{}UpdateTreeData.user.2'.format(weapon_type, weapon_type)
object = user.read_user_file(filename)

with open('msg\\{}_Name_zhCN.txt'.format(weapon_type), 'rb') as f:
    text = f.read().decode('utf-16')\
            .replace('Ⅰ',' I').replace('Ⅱ',' II').replace('Ⅲ',' III').replace('Ⅳ',' IV')\
            .replace('Ⅴ',' V').replace('】 I','】I').replace('】 V','】V')
    weapon_name_zh_list = text.split('\n')
weapon_name_zh_list = [i[8:].strip() for i in weapon_name_zh_list if len(i) >= 8]

with open('msg\\{}_Name_en.txt'.format(weapon_type), 'rb') as f:
    text = f.read().decode('utf-16')\
            .replace('Ⅰ',' I').replace('Ⅱ',' II').replace('Ⅲ',' III').replace('Ⅳ',' IV')\
            .replace('Ⅴ',' V').replace('】 I','】I').replace('】 V','】V')
    weapon_name_en_list = text.split('\n')
weapon_name_en_list = [i[8:].strip() for i in weapon_name_en_list if len(i) >= 8]

with open('tree\\Game8_weapon_tree\\{}_tree.txt'.format(weapon_type), 'rb') as f:
    text = weapon_tree_list = f.read().decode('utf-8')\
            .replace('┗','').replace('┃','').replace('┣','')
    weapon_tree_list = text.split('\n')
weapon_tree_list = [i.strip() for i in weapon_tree_list]

class WeaponInTree(OrderedAttibuteClass):
    def __init__(self, weapon_id, tree_type, index, next_weapon_type_list,\
                next_weapon_index_list, prev_weapon_type, prev_weapon_index):
        self.weapon_type = ''
        self.weapon_id = weapon_id
        self.name_zh = ''
        self.name_en = ''
        self.tree_id = tree_type
        self.tree_sort_id = -1
        self.index_in_tree = index
        self.next_weapon_tree_id_list = next_weapon_type_list
        self.next_weapon_index_in_tree_list = next_weapon_index_list
        self.next_weapon_name_zh_list = [''] * 5
        self.prev_weapon_tree_id = prev_weapon_type
        self.prev_weapon_index_in_tree = prev_weapon_index
        self.prev_weapon_name_zh = ''
        self.clean_up()

    def clean_up(self):
        if self.weapon_id != 'None':
            self.weapon_type = self.weapon_id.split('(')[0]
            self.weapon_id = int(self.weapon_id.split('(')[1][:-1])

weapon_list = [None] * 150
for w in object.param:
    weapon = WeaponInTree(w.weapon_id, w.tree_type, w.index, w.next_weapon_type_list,\
                        w.next_weapon_index_list, w.prev_weapon_type, w.prev_weapon_index)
    if weapon.weapon_id != 'None':
        weapon_list[weapon.weapon_id] = weapon

for weapon in weapon_list:
    if not weapon is None:
        weapon.name_zh = weapon_name_zh_list[weapon.weapon_id]
        weapon.name_en = weapon_name_en_list[weapon.weapon_id]

for weapon in weapon_list:
    if not weapon is None:
        for prev_candidate in weapon_list:
            if not prev_candidate is None and\
                    prev_candidate.tree_id == weapon.prev_weapon_tree_id and\
                    prev_candidate.index_in_tree == weapon.prev_weapon_index_in_tree:
                weapon.prev_weapon_name_zh = prev_candidate.name_zh
        for i in range(5):
            for next_candidate in weapon_list:
                if not next_candidate is None and\
                        next_candidate.tree_id == weapon.next_weapon_tree_id_list[i] and\
                        next_candidate.index_in_tree == weapon.next_weapon_index_in_tree_list[i]:
                    weapon.next_weapon_name_zh_list[i] = next_candidate.name_zh

tree_id_dict = {}
for weapon in weapon_list:
    if not weapon is None:
        if not weapon.tree_id in tree_id_dict.keys():
            tree_id_dict[weapon.tree_id] = weapon_tree_list.index(weapon.name_en)
tree_id_dict = OrderedDict(sorted(tree_id_dict.items(), key=lambda item: item[1]))
for i in range(len(tree_id_dict)):
    tree_id_dict[list(tree_id_dict.keys())[i]] = i

for weapon in weapon_list:
    if not weapon is None:
        weapon.tree_sort_id = tree_id_dict[weapon.tree_id]

weapon_list_sorted = []
for i in range(1000): # Enough to cover all trees
    for j in range(20):
        for weapon in weapon_list:
            if not weapon is None and weapon.tree_sort_id == i and weapon.index_in_tree == j:
                weapon_list_sorted.append(weapon)

json_weapon_list_sorted = {}
for weapon in weapon_list_sorted:
    json_weapon_list_sorted[weapon.name_zh] = {\
        'tree_sort_id': weapon.tree_sort_id,\
        'index_in_tree': weapon.index_in_tree,\
        'prev_weapon_name_zh': weapon.prev_weapon_name_zh,\
        'next_weapon_name_zh': list(filter(('').__ne__, weapon.next_weapon_name_zh_list))}
# print(json_weapon_list_sorted)

with open('tree\\{}_tree.json'.format(weapon_type), 'w', encoding='utf8') as f:
    json.dump(json_weapon_list_sorted, f, ensure_ascii=False)
