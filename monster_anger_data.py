import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice anger_data.rs
# Classes for monster anger data, which will become part of Monster class

class EnemyAngerSeparateData(OrderedAttibuteClass):
    def __init__(self):
        self.val = 'u32'
    def human_readable(self):
        self.val = utils.u32_to_i32(self.val)

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
        self.timer = utils.u32_to_i32(self.timer)
        self.hyakuryu_cool_timer = utils.u32_to_i32(self.hyakuryu_cool_timer)
        self.mot_rate = utils.u32_to_f32(self.mot_rate)
        self.atk_rate = utils.u32_to_f32(self.atk_rate)
        self.def_rate = utils.u32_to_f32(self.def_rate)
        self.compensation_rate = [utils.u32_to_f32(i) for i in self.compensation_rate]
        self.hyakuryu_compensation_rate = [utils.u32_to_f32(i) for i in self.hyakuryu_compensation_rate]
        self.anger_stay_add_sec = utils.u32_to_f32(self.anger_stay_add_sec)
        self.life_area_timer_rate = utils.u32_to_f32(self.life_area_timer_rate)
