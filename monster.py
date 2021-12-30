from bitstring import BitStream
from utils import OrderedAttibuteClass
from os.path import exists
import user
import rcol
import utils
import json

class Monster(OrderedAttibuteClass):
    def __init__(self, id, sub_id, is_large_monster=True):
        self.is_large_monster = is_large_monster
        self.id = id
        self.sub_id = sub_id
        self.enemy_type = None
        self.data_base = None
        self.data_tune = None
        self.meat_data = None
        self.condition_damage_data = None
        self.anger_data = None
        self.parts_break_data = None
        self.parts_map = []
        self.boss_init_set_data = None
        self.collider_mapping = None # Rcol not implemented, mhrice::extract::pedia::ColliderMapping
        self.drop_item = None
        self.parts_break_reward = None

        self.get_data_base()
        self.get_data_tune()
        self.get_meat_data()
        self.get_condition_damage_data()
        self.get_anger_data()
        self.get_parts_break_data()
        self.get_parts_map()
        self.get_boss_init_set_data()
        self.get_drop_item()
        self.get_parts_break_reward()
        if not self.boss_init_set_data is None:
            self.enemy_type = self.boss_init_set_data.enemy_type

    def get_data_base(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_database.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_database.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.data_base = user.read_user_file(filename)
        else:
            self.data_base = None

    def get_data_tune(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_datatune.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_datatune.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.data_tune = user.read_user_file(filename)
        else:
            self.data_tune = None

    def get_meat_data(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_meat_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_meat_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.meat_data = user.read_user_file(filename)
        else:
            self.meat_data = None

    def get_condition_damage_data(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_condition_damage_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_condition_damage_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.condition_damage_data = user.read_user_file(filename)
        else:
            self.condition_damage_data = None

    def get_anger_data(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_anger_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_anger_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.anger_data = user.read_user_file(filename)
        else:
            self.anger_data = None

    def get_parts_break_data(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_parts_break_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_parts_break_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.parts_break_data = user.read_user_file(filename)
        else:
            self.parts_break_data = None

    def get_parts_map(self):
        if self.is_large_monster:
            filename = 'rcol\\em{:03}_{:02}_colliders.rcol.18'\
                .format(self.id, self.sub_id)
        else:
            filename = 'rcol\\ems{:03}_{:02}_colliders.rcol.18'\
                .format(self.id, self.sub_id)
        if exists(filename):
            self.parts_map = rcol.read_rcol_file(filename)
        else:
            self.parts_map = None

    def get_boss_init_set_data(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_boss_init_set_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_boss_init_set_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.boss_init_set_data = user.read_user_file(filename)
        else:
            self.boss_init_set_data = None

    def get_drop_item(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_drop_item_info_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_drop_item_info_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.drop_item = user.read_user_file(filename)
        else:
            self.drop_item = None

    def get_parts_break_reward(self):
        if self.is_large_monster:
            filename = 'user\\monster\\em{:03}\\{:02}\\em{:03}_{:02}_parts_break_reward_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        else:
            filename = 'user\\monster\\ems{:03}\\{:02}\\ems{:03}_{:02}_parts_break_reward_data.user.2'\
                .format(self.id, self.sub_id, self.id, self.sub_id)
        if exists(filename):
            self.parts_break_reward = user.read_user_file(filename)
        else:
            self.parts_break_reward = None

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
    # utils.print_hierarchical_object(monster)
    large_monster_ids, large_monsters = read_large_monster_data()
    # for i in large_monsters:
    #     utils.print_hierarchical_object(i)
    utils.print_hierarchical_object(large_monsters[0])
    # small_monster_ids, small_monsters = read_small_monster_data()
    # for i in small_monsters:
    #     utils.print_hierarchical_object(i)
