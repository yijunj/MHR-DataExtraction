from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice alchemy.rs
# Classes for alchemy data

class AlchemyPatturnUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.patturn = 'u32' # This is a typo made in the game file, so let's keep it
        self.color = 'u32'
        self.cost_village_point = 'u32'
        self.usable_item_list = ['u32']
        self.cost_material_point = 'u32'
        self.require_talisman_num = 'u32'
        self.output_min_num = 'u32'
        self.output_max_num = 'u32'
    def human_readable(self):
        if self.patturn > 0x7FFFFFFF: self.patturn -= (0xFFFFFFFF + 1)
        self.patturn += 1
        self.color = enum_ColorTypes(self.color)
        self.usable_item_list = [enum_ItemId(i) for i in self.usable_item_list]

class AlchemyPatturnUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['AlchemyPatturnUserDataParam']

class AlchemyPlSkillTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.sort_id = 'u32'
        self.skill_id = 'u32'
        self.grade = 'u32'
        self.patturn = 'u32'
        self.pick_rate = 'u32'
        self.skill1_rate_list = ['u32']
        self.miss_rate_list = ['u32']
        self.skill2_rate_list = ['u32']
    def human_readable(self):
        if self.sort_id > 0x7FFFFFFF: self.sort_id -= (0xFFFFFFFF + 1)
        self.skill_id = enum_PlEquipSkillId(self.skill_id)
        self.grade = enum_GradeTypes(self.grade)
        self.patturn += 1

class AlchemyPlSkillTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['AlchemyPlSkillTableUserDataParam']

class GradeWorthTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.grade_point = 'u32'
        self.add_point = 'u32'

class GradeWorthTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['GradeWorthTableUserDataParam']

class RareTypeTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.worth_point = 'u32'
        self.rare_type_list = ['u8']
    def human_readable(self):
        self.rare_type_list = [i+1 for i in self.rare_type_list]

class RareTypeTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['RareTypeTableUserDataParam']

class SecondSkillLotRateTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.skill1_grade = 'u32'
        self.probability_list = ['u32']
    def human_readable(self):
        self.skill1_grade = enum_GradeTypes(self.skill1_grade)

class SecondSkillLotRateTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['SecondSkillLotRateTableUserDataParam']

class SkillGradeLotRateTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.patturn_type = 'u32'
        self.probability1_list = ['u32']
        self.probability_list = ['u32']
        self.probability2_list = ['u32']
    def human_readable(self):
        self.patturn_type += 1

class SkillGradeLotRateTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['SkillGradeLotRateTableUserDataParam']

class SlotNumTableUserDataSkillParam(OrderedAttibuteClass):
    def __init__(self):
        self.skill1_grade = 'u32'
        self.skill2_grade = 'u32'
        self.table0_probability_list = ['u32']
        self.table1_probability_list = ['u32']
        self.table2_probability_list = ['u32']
        self.table3_probability_list = ['u32']
        self.table4_probability_list = ['u32']
    def human_readable(self):
        self.skill1_grade = enum_GradeTypesForSlotNumTable(self.skill1_grade)
        self.skill2_grade = enum_GradeTypesForSlotNumTable(self.skill2_grade)

class SlotNumTableUserDataSlotParam(OrderedAttibuteClass):
    def __init__(self):
        self.slot_param = ['SlotNumTableUserDataSkillParam']

class SlotNumTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['SlotNumTableUserDataSlotParam']

class SlotWorthTableUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.worth_point = 'u32'

class SlotWorthTableUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['SlotWorthTableUserDataParam']
