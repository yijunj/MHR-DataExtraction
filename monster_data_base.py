import utils
from utils import OrderedAttibuteClass
from enums import *

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
        self.caution_to_combat_vision_timer = utils.u32_to_f32(self.caution_to_combat_vision_timer)
        self.caution_to_non_combat_timer = utils.u32_to_f32(self.caution_to_non_combat_timer)
        self.combat_to_non_combat_timer = utils.u32_to_f32(self.combat_to_non_combat_timer)
        self.non_combat_kehai_rate = utils.u32_to_f32(self.non_combat_kehai_rate)
        self.base_scale = utils.u32_to_f32(self.base_scale)
