from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to MHRice data_base.rs
# Classes for monster data, which will become part of Monster class

class EnemyDataBase(OrderedAttibuteClass):
    def __init__(self):
        self.caution_to_combat_vision_timer = 'u32'
        self.caution_to_non_combat_timer = 'u32'
        self.combat_to_non_combat_timer = 'u32'
        self.non_combat_kehai_rate = 'u32'
        self.base_scale = 'u32'
    def human_readable(self):
        self.caution_to_combat_vision_timer = utils.hex_to_f32(hex(self.caution_to_combat_vision_timer)[2:])
        self.caution_to_non_combat_timer = utils.hex_to_f32(hex(self.caution_to_non_combat_timer)[2:])
        self.combat_to_non_combat_timer = utils.hex_to_f32(hex(self.combat_to_non_combat_timer)[2:])
        self.non_combat_kehai_rate = utils.hex_to_f32(hex(self.non_combat_kehai_rate)[2:])
        self.base_scale = utils.hex_to_f32(hex(self.base_scale)[2:])
