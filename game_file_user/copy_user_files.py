import shutil
import os
import json

pak_dir = 'M:\\MHR game data extraction\\[PAK TO DATA] Switch RETool hacking\\natives\\NSW'

# Reads file names and directories of the relevant user files
with open('user_file_list_excl_monsters.csv', 'r') as f:
    user_file_list = f.read().split('\n')

# Copy these user files from the pak folder to the current folder
user_file_dict = {}
for line in user_file_list:
    if line != '':
        user_file_dict[line.split(',')[0].strip()] =\
            {'to_path':line.split(',')[1].strip(), 'from_path':line.split(',')[2].strip()}
for key in user_file_dict.keys():
    to_dir = '\\'.join(user_file_dict[key]['to_path'].split('\\')[:-1])
    try:
        os.makedirs(to_dir)
    except FileExistsError:
        pass
    shutil.copy2(os.path.join(pak_dir, user_file_dict[key]['from_path']), user_file_dict[key]['to_path'])

# Copy large monster user files
large_monster_ids = {}
data_type_list = ['database', 'datatune', 'meat_data', 'condition_damage_data', 'anger_data', 'parts_break_data',\
                'boss_init_set_data', 'drop_item_info_data', 'parts_break_reward_data']
for id in range(1000):
    for sub_id in range(10):
        pfb_path = os.path.join(pak_dir,\
            'enemy\\em{:03}\\{:02}\\prefab\\em{:03}_{:02}.pfb.17'.format(id, sub_id, id, sub_id))
        if not os.path.exists(pfb_path):
            continue
        to_dir = 'monster\\em{:03}\\{:02}'.format(id, sub_id)
        try:
            os.makedirs(to_dir)
        except FileExistsError:
            pass
        for data_type in data_type_list:
            from_path = os.path.join(pak_dir,\
                'enemy\\em{:03}\\{:02}\\user_data\\em{:03}_{:02}_{}.user.2'.format(id, sub_id, id, sub_id, data_type))
            to_path = 'monster\\em{:03}\\{:02}\\em{:03}_{:02}_{}.user.2'.format(id, sub_id, id, sub_id, data_type)
            try:
                shutil.copy2(from_path, to_path)
            except FileNotFoundError:
                print('Cannot find path {}'.format(from_path))
        if id in large_monster_ids.keys():
            large_monster_ids[id].append(sub_id)
        else:
            large_monster_ids[id] = [sub_id]

# Copy small monster user files
small_monster_ids = {}
data_type_list = ['database', 'datatune', 'meat_data', 'condition_damage_data',\
                'anger_data', 'parts_break_data', 'drop_item_info_data']
for id in range(1000):
    for sub_id in range(10):
        pfb_path = os.path.join(pak_dir,\
            'enemy\\ems{:03}\\{:02}\\prefab\\ems{:03}_{:02}.pfb.17'.format(id, sub_id, id, sub_id))
        if not os.path.exists(pfb_path):
            continue
        to_dir = 'monster\\ems{:03}\\{:02}'.format(id, sub_id)
        try:
            os.makedirs(to_dir)
        except FileExistsError:
            pass
        for data_type in data_type_list:
            from_path = os.path.join(pak_dir,\
                'enemy\\ems{:03}\\{:02}\\user_data\\ems{:03}_{:02}_{}.user.2'.format(id, sub_id, id, sub_id, data_type))
            to_path = 'monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_{}.user.2'.format(id, sub_id, id, sub_id, data_type)
            try:
                shutil.copy2(from_path, to_path)
            except FileNotFoundError:
                print('Cannot find path {}'.format(from_path))
        if id in small_monster_ids.keys():
            small_monster_ids[id].append(sub_id)
        else:
            small_monster_ids[id] = [sub_id]

# Dump file names into json
with open('user_file_list_excl_monsters.json', 'w') as f:
    json.dump(user_file_dict, f)

with open('large_monster_ids.json', 'w') as f:
    json.dump(large_monster_ids, f)

with open('small_monster_ids.json', 'w') as f:
    json.dump(small_monster_ids, f)
