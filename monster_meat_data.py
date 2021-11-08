from utils import OrderedAttibuteClass
from enums import *

# This correspondes to part of MHRice meat_data.rs
# Classes for monster meat data, which will become part of Monster class

class MeatGroupInfo(OrderedAttibuteClass):
    def __init__(self):
        self.slash = 'u16'
        self.strike = 'u16'
        self.shell = 'u16'
        self.fire = 'u16'
        self.water = 'u16'
        self.ice = 'u16'
        self.elect = 'u16'
        self.dragon = 'u16'
        self.piyo = 'u16'

class EnemyMeatContainer(OrderedAttibuteClass):
    def __init__(self):
        self.meat_group_info = ['MeatGroupInfo']

class EnemyMeatData(OrderedAttibuteClass):
    def __init__(self):
        self.meat_container = ['EnemyMeatContainer']
