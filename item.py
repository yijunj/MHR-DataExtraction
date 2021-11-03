from utils import OrderedAttibuteClass
from enums import *

# This correspondes to MHRice item.rs
# Classes for item data

class ItemUserDataParam(OrderedAttibuteClass):
    def __init__(self):
        self.id = 'u32'
        self.cariable_filter = 'u32'
        self.type = 'u32'
        self.rare = 'u8'
        self.pl_max_count = 'u32'
        self.ot_max_count = 'u32'
        self.sort_id = 'u16'
        self.supply = 'u8'
        self.show_item_window = 'u8'
        self.show_action_window = 'u8'
        self.infinite = 'u8'
        self.default = 'u8'
        self.icon_can_eat = 'u8'
        self.icon_item_rank = 'u32'
        self.effect_rare = 'u32'
        self.icon_chara = 'u32'
        self.icon_color = 'u32'
        self.se_type = 'u32'
        self.sell_price = 'u32'
        self.buy_price = 'u32'
        self.item_action_type = 'u32'
        self.rank_type = 'u32'
        self.item_group = 'u32'
        self.category_worth = 'u32'
        self.material_category = ['u32']
        self.evaluation_value = 'u32'
    def human_readable(self):
        self.id = enum_ItemId(self.id)
        self.cariable_filter = enum_CarriableFilter(self.cariable_filter)
        self.type = enum_ItemTypes(self.type)
        self.rare += 1
        self.supply = bool(self.supply)
        self.show_item_window = bool(self.show_item_window)
        self.show_action_window = bool(self.show_action_window)
        self.icon_item_rank = enum_IconRank(self.icon_item_rank)
        self.infinite = bool(self.infinite)
        self.default = bool(self.default)
        self.icon_can_eat = bool(self.icon_can_eat)
        self.icon_item_rank = bool(self.icon_item_rank)
        self.effect_rare = bool(self.effect_rare)
        if self.icon_chara > 0x7FFFFFFF: self.icon_chara -= (0xFFFFFFFF + 1)
        if self.icon_color > 0x7FFFFFFF: self.icon_color -= (0xFFFFFFFF + 1)
        if self.se_type > 0x7FFFFFFF: self.se_type -= (0xFFFFFFFF + 1)
        if self.item_action_type > 0x7FFFFFFF: self.item_action_type -= (0xFFFFFFFF + 1)
        self.rank_type = enum_RankTypes(self.rank_type)
        self.item_group = enum_ItemGroupTypes(self.item_group)
        self.material_category = [enum_MaterialCategory(i) for i in self.material_category]

class ItemUserData(OrderedAttibuteClass):
    def __init__(self):
        self.param = ['ItemUserDataParam']
