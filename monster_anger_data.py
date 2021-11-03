from utils import OrderedAttibuteClass
from enums import *
import utils

# This correspondes to MHRice anger_data.rs
# Classes for monster anger data, which will become part of Monster class

class EnemyAngerSeparateData(OrderedAttibuteClass):
    def __init__(self):
        self.val = 'u32'
    def human_readable(self):
        if self.val > 0x7FFFFFFF: self.val -= (0xFFFFFFFF + 1)

class EnemyAngerData(OrderedAttibuteClass):
    def __init__(self):
        self.data_info = ['EnemyAngerSeparateData']
        self.timer = 'u32'
        self.hyakuryu_cool_timer = 'u32'
        self.mot_rate = 'u32'
        self.atk_rate = 'u32'
        self.def_rate = 'u32'
        self.compensation_rate = ['u32']
        self.hyakuryu_compensation_rate = ['u32']
        self.anger_stay_add_sec = 'u32'
        self.life_area_timer_rate = 'u32'
    def human_readable(self):
        if self.timer > 0x7FFFFFFF: self.timer -= (0xFFFFFFFF + 1)
        if self.hyakuryu_cool_timer > 0x7FFFFFFF: self.hyakuryu_cool_timer -= (0xFFFFFFFF + 1)
        self.mot_rate = utils.hex_to_f32(hex(self.mot_rate)[2:])
        self.atk_rate = utils.hex_to_f32(hex(self.atk_rate)[2:])
        self.def_rate = utils.hex_to_f32(hex(self.def_rate)[2:])
        self.compensation_rate = [utils.hex_to_f32(hex(i)[2:]) for i in self.compensation_rate]
        self.hyakuryu_compensation_rate = [utils.hex_to_f32(hex(i)[2:]) for i in self.hyakuryu_compensation_rate]
        self.anger_stay_add_sec = utils.hex_to_f32(hex(self.anger_stay_add_sec)[2:])
        self.life_area_timer_rate = utils.hex_to_f32(hex(self.life_area_timer_rate)[2:])
