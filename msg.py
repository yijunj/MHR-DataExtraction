from bitstring import BitStream
import enums
import utils
from utils import OrderedAttibuteClass
import mmh3

class MsgEntry(OrderedAttibuteClass):
    def __init__(self, name, guid, hash, attributes, content):
        self.name = name
        self.guid = guid
        self.hash = hash
        self.attributes = attributes
        self.content = content

class MsgAttributeHeader(OrderedAttibuteClass):
    def __init__(self, j, name):
        self.j = j
        self.name = name

class Msg(OrderedAttibuteClass):
    def __init__(self, attribute_headers, entries):
        self.attribute_headers = attribute_headers
        self.entries = entries

# Reads meta data of a msg data file
def read_msg_head(data):
    version = data.read('uintle:32')
    if version != 0x11:
        raise Exception('Version should be 0x10')
    magic = data.read('uintle:32')
    if magic != 0x47534D47: # little-endian version of GMSG
        raise Exception('User magic should be "USR"')
    temp = data.read('uintle:64')
    if temp != 0x10: # little-endian version of GMSG
        raise Exception('Next 32 bits after magic should be 0x10')
    count_a = data.read('uintle:32')
    attribute_count = data.read('uintle:32')
    language_count = data.read('uintle:32')
    data = utils.pad_to_multiple_of(64, data)

    data_offset = data.read('uintle:64')
    p_offset = data.read('uintle:64')
    q_offset = data.read('uintle:64')
    attribute_js_offset = data.read('uintle:64')
    attribute_names_offset = data.read('uintle:64')

    entries = []
    for i in range(count_a):
        entries.append(data.read('uintle:64'))

    data.pos = p_offset * 8
    p = data.read('uintle:64')
    if p != 0:
        raise Exception('p should be zero')

    data.pos = q_offset * 8
    languages = []
    for i in range(language_count):
        languages.append(data.read('uintle:32'))

    data.pos = attribute_js_offset * 8
    attribute_js = []
    for i in range(attribute_count):
        attribute_js.append(data.read('iintle:32')) # i32 copied from MHRice

    # Some alignment check?
    data.pos = attribute_names_offset * 8
    attribute_names = []
    for i in range(attribute_count):
        attribute_js.append(data.read('uintle:64'))

    # MsgEntry
    for i in range(len(entries)):
        data.pos = entries[i] * 8
        guid = data.read('uintle:128')
        guid = enums.bytes_Guid(guid, 128)
        data.read('uintle:32')
        hash = data.read('uintle:32')
        name = data.read('uintle:64')
        attributes = data.read('uintle:64')
        content = []
        for j in range(language_count):
            content.append(data.read('uintle:64'))

        data.pos = attributes * 8
        attributes = []
        for attrubutes in range(attribute_count):
            attributes.append(data.read('uintle:64'))
        entries[i] = MsgEntry(name, guid, hash, attributes, content)

    # Data
    data.pos = data_offset * 8
    data_list = []
    while data.pos < data.len:
        data_list.append(data.read('uintle:8'))

    return entries, data_offset, data_list, attribute_js, attribute_names

# Reads actual data of a msg data file
def read_msg_data(entries, data_offset, data_list):
    # First parse data_list
    key = [0xCF, 0xCE, 0xFB, 0xF8, 0xEC, 0x0A, 0x33, 0x66, 0x93, 0xA9, 0x1D, 0x93, 0x50, 0x39, 0x5F, 0x09]
    prev = 0
    data_list_parsed = []
    for i in range(len(data_list)):
        byte = data_list[i]
        cur = byte
        byte ^= prev ^ key[i & 0xF]
        prev = cur
        data_list_parsed.append(byte)
    # data_list_parsed is a list of u8, every two entries define a char
    # char_list is a list of char
    # hash takes a subset of data_list_parsed, while name takes a subset of str_list
    str_parsed = utils.u8_list_to_u16_str(data_list_parsed)

    for entry in entries:
        entry.name = utils.read_str_until_x00(str_parsed[int((entry.name-data_offset)/2):])
        hash_name = utils.str_to_u16_hashable(entry.name)
        if utils.i32_to_u32(mmh3.hash(hash_name, 0xFFFFFFFF)) != entry.hash:
            raise Exception('Wrong hash')

        for i in range(len(entry.attributes)):
            entry.attributes[i] =\
                utils.read_str_until_x00(str_parsed[int((entry.attributes[i]-data_offset)/2):])

        for i in range(len(entry.content)):
            entry.content[i] =\
                utils.read_str_until_x00(str_parsed[int((entry.content[i]-data_offset)/2):])
    return entries, str_parsed

# Reads attribute header data of a msg data file
def read_msg_attr_header(attr_js, attr_names, data_offset, str_parsed):
    attribute_headers = []
    for i in range(len(attr_names)):
        name = attr_names[i]
        name = utils.read_str_until_x00(str_parsed[int((name-data_offset)/2):])
        attribute_headers.append(MsgAttributeHeader(attr_js[i], name))
    return attribute_headers

# # Combines everything together
def read_msg_file(filename):
    data = BitStream(filename = filename)
    entries, data_offset, data_list, attr_js, attr_names = read_msg_head(data)
    entries, str_parsed = read_msg_data(entries, data_offset, data_list)
    attr_headers = read_msg_attr_header(attr_js, attr_names, data_offset, str_parsed)
    return Msg(attr_headers, entries)

if __name__ == '__main__':
    # filename = 'msg\\HN_Hunternote_Menu.msg.17'
    # filename = 'msg\\Tag_EM_Name.msg.17'
    # filename = 'msg\\Tag_EM_Name_Alias.msg.17'
    # filename = 'msg\\QuestData_Hall.msg.17'
    # filename = 'msg\\QuestData_Village.msg.17'
    # filename = 'msg\\QuestData_Tutorial.msg.17'
    # filename = 'msg\\QuestData_Arena.msg.17'
    # filename = 'msg\\A_Head_Name.msg.17'
    # filename = 'msg\\A_Chest_Name.msg.17'
    # filename = 'msg\\A_Arm_Name.msg.17'
    # filename = 'msg\\A_Waist_Name.msg.17'
    # filename = 'msg\\A_Leg_Name.msg.17'
    # filename = 'msg\\ArmorSeries_Hunter_Name.msg.17'
    # filename = 'msg\\PlayerSkill_Detail.msg.17'
    # filename = 'msg\\PlayerSkill_Explain.msg.17'
    # filename = 'msg\\PlayerSkill_Name.msg.17'
    # filename = 'msg\\HyakuryuSkill_Name.msg.17'
    # filename = 'msg\\HyakuryuSkill_Explain.msg.17'
    # filename = 'msg\\Decorations_Name.msg.17'
    # filename = 'msg\\ItemName.msg.17'
    # filename = 'msg\\ItemExplain.msg.17'
    # filename = 'msg\\ItemCategoryType_Name.msg.17'
    # filename = 'msg\\GreatSword_Name.msg.17'
    # filename = 'msg\\GreatSword_Explain.msg.17'
    filename = 'msg\\Horn_UniqueParam.msg.17'
    msg = read_msg_file(filename)
    utils.print_hierarchical_object(msg)
