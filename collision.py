import utils
from utils import OrderedAttibuteClass
from enums import *

# This correspondes to part of MHRice collision.rs
# Classes for monster collision data, and part names.

class RequestSetColliderUserData(OrderedAttibuteClass):
    def __init__(self):
        self.name = 'string'
        self.zero = 'u32'

class PhysicsUserData(OrderedAttibuteClass):
    def __init__(self):
        self.name = 'string'

class EmHitDamageRsData(OrderedAttibuteClass):
    def __init__(self):
        self.base = 'PhysicsUserData'
        self.parts_group = 'u16'
