import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to part of MHRice parts_break_data.rs
# Classes for monster part break data, which will become part of Monster class

class PartsLockParam(OrderedAttibuteClass):
    def __init__(self):
        self.hash_value = 'u32'

class PartsBreakData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_condition_id = 'u32'
        self.effect_container_id = 'u32'
        self.effect_element_id = 'u32'
        self.ignore_tag_value = 'u32'
    def human_readable(self):
        self.parts_condition_id = utils.u32_to_i32(self.parts_condition_id)
        self.effect_container_id = utils.u32_to_i32(self.effect_container_id)
        self.effect_element_id = utils.u32_to_i32(self.effect_element_id)

class ConditionPartsBreakData(OrderedAttibuteClass):
    def __init__(self):
        self.condition_id = 'u32'
        self.parts_break_data_list = ['PartsBreakData']
    def human_readable(self):
        self.condition_id = utils.u32_to_i32(self.condition_id)

class PartsBreakGroupData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_group = 'u16'
        self.parts_lock_group_hash = ['PartsLockParam']
        self.condition_parts_break_data_list = ['ConditionPartsBreakData']

class PartsLossData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_condition_id = 'u32'
        self.ignore_tag_value = 'u32'
        self.parts_loss_effect_container_id = 'u32'
        self.parts_loss_effect_element_id = 'u32'
        self.on_ground_effect_container_id = 'u32'
        self.on_ground_effect_element_id = 'u32'
    def human_readable(self):
        self.parts_condition_id = utils.u32_to_i32(self.parts_condition_id)

class ConditionPartsLossData(OrderedAttibuteClass):
    def __init__(self):
        self.condition_id = 'u32'
        self.parts_loss_data = 'PartsLossData'
    def human_readable(self):
        self.condition_id = utils.u32_to_i32(self.condition_id)

class PartsLossGroupData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_group = 'u16'
        self.parts_lock_group_hash = ['PartsLockParam']
        self.condition_parts_loss_data_list = ['ConditionPartsLossData']

class EnemyPartsBreakData(OrderedAttibuteClass):
    def __init__(self):
        self.parts_break_group_data_list = ['PartsBreakGroupData']
        self.parts_loss_group_data_list = ['PartsLossGroupData']
