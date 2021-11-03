from bitstring import BitStream
from utils import OrderedAttibuteClass
import user
import json

class Monster(OrderedAttibuteClass):
    def __init__(self, id, sub_id, is_large_monster=True):
        self.is_large_monster = is_large_monster
        self.id = id
        self.sub_id = sub_id
        self.enemy_type = None
        self.get_data_base()
        self.get_data_tune()
        self.get_meat_data()
        self.get_condition_damage_data()
        self.get_anger_data()
        self.get_parts_break_data()
        self.get_boss_init_set_data()
        self.get_drop_item()
        if self.is_large_monster:
            self.enemy_type = self.boss_init_set_data.enemy_type

    def get_data_base(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_database.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_database.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.data_base, _ = user.read_rsz(data_type_list, data)

    def get_data_tune(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_datatune.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_datatune.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.data_tune, _ = user.read_rsz(data_type_list, data)

    def get_meat_data(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_meat_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_meat_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.meat_data, _ = user.read_rsz(data_type_list, data)

    def get_condition_damage_data(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_condition_damage_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_condition_damage_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.condition_damage_data, _ = user.read_rsz(data_type_list, data)

    def get_anger_data(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_anger_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_anger_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.anger_data, _ = user.read_rsz(data_type_list, data)

    def get_parts_break_data(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_parts_break_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_parts_break_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.parts_break_data, _ = user.read_rsz(data_type_list, data)

    def get_boss_init_set_data(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_boss_init_set_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            self.boss_init_set_data = None
            return
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.boss_init_set_data, _ = user.read_rsz(data_type_list, data)

    def get_drop_item(self):
        if self.is_large_monster:
            data = BitStream(filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_drop_item_info_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        else:
            data = BitStream(filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_drop_item_info_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id))
        data = user.read_usr_head(data)
        data_type_list, data = user.read_rsz_head(data)
        self.drop_item, _ = user.read_rsz(data_type_list, data)

def read_large_monster_data():
    large_monsters = []
    with open('user\\large_monster_ids.json', 'r') as f:
        large_monster_ids = json.loads(f.read())
    for key in large_monster_ids.keys():
        id = int(key)
        for sub_id in large_monster_ids[key]:
            large_monsters.append(Monster(id, sub_id, is_large_monster=True))
    return large_monster_ids, large_monsters

def read_small_monster_data():
    small_monsters = []
    with open('user\\small_monster_ids.json', 'r') as f:
        small_monster_ids = json.loads(f.read())
    for key in small_monster_ids.keys():
        id = int(key)
        for sub_id in small_monster_ids[key]:
            small_monsters.append(Monster(id, sub_id, is_large_monster=False))
    return small_monster_ids, small_monsters

if __name__ == '__main__':
    # monster = Monster(1, 0, is_large_monster=True)
    # user.print_hierarchical_object(monster)
    # large_monster_ids, large_monsters = read_large_monster_data()
    # user.print_hierarchical_object(large_monsters[0])
    small_monster_ids, small_monsters = read_small_monster_data()
    user.print_hierarchical_object(small_monsters[0])
