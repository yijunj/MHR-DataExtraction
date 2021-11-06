from utils import OrderedAttibuteClass
from enums import *

# This correspondes to part of MHRice meat_data.rs
# Classes for monster meat data, which will become part of Monster class

class MeatGroupInfo(OrderedAttibuteClass):
    def __init__(self):
        self.slash = 'u16,np'
        self.strike = 'u16,np'
        self.shell = 'u16,np'
        self.fire = 'u16,np'
        self.water = 'u16,np'
        self.ice = 'u16,np'
        self.elect = 'u16,np'
        self.dragon = 'u16,np'
        self.piyo = 'u16,np'

class EnemyMeatContainer(OrderedAttibuteClass):
    def __init__(self):
        self.meat_group_info = ['MeatGroupInfo']

class EnemyMeatData(OrderedAttibuteClass):
    def __init__(self):
        self.meat_container = ['EnemyMeatContainer']
