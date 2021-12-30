from bitstring import BitStream
import utils
from utils import RSZ_TYPE_MAP

from collision import *
from user import read_rsz_head, read_rsz_chunk, read_rsz

# This script is about reading rcol data files
# Basically, it reads a certain number of bits, assigns it to the current class attribute, then repeat
# This only partially implements what mhrice rcol.rs does

# Reads meta data of a user data file
def read_rcol_head(data):
    magic = data.read('uintle:32')
    if magic != 0x4C4F4352: # little-endian version of RCOL
        raise Exception('Rcol magic should be "RCOL"')

    collider_group_count = data.read('uintle:32')
    total_collider_count = data.read('uintle:32')
    dummy = data.read('uintle:32')
    group_attachment_count = data.read('uintle:32')
    dummy = data.read('uintle:32')
    ignore_tag_count = data.read('uintle:32')
    e_count = data.read('uintle:32')
    rsz_len = data.read('uintle:32')
    dummy = data.read('uintle:32')

    collider_group_offset = data.read('uintle:64')
    rsz_offset = data.read('uintle:64')
    group_attachment_offset = data.read('uintle:64')
    ignore_tag_offset = data.read('uintle:64')
    e_offset = data.read('uintle:64')
    string_table_offset = e_offset + e_count * 64

    # Now read RSZ
    data.pos = rsz_offset * 8
    return data

# Combines everything together: only reads part names, from EmHitDamageRsData
def read_rcol_file(filename):
    data = BitStream(filename = filename)
    data = read_rcol_head(data)
    data_type_list, data = read_rsz_head(data)

    for i in reversed(range(len(data_type_list))):
        if data_type_list[i] == 'EmHitDamageRsData':
            break
    data_type_list = data_type_list[:i+1]

    data_stack, _ = read_rsz(data_type_list, data)
    data_type = type(data_stack[-1])

    max_length = 100
    part_list = [None] * max_length
    for part in data_stack:
        if type(part) == data_type and part.parts_group < max_length:
            part_list[part.parts_group] = part.base.name

    for i in reversed(range(max_length)):
        if not part_list[i] is None:
            break
    part_list = part_list[:i+1]

    return part_list

if __name__ == '__main__':
    filename = 'rcol\\em007_00_colliders.rcol.18'
    part_list = read_rcol_file(filename)
    print(part_list)
