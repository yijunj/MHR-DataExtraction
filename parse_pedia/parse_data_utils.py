import sys
sys.path.append('..')

import re
import unicodedata
from utils import OrderedAttibuteClass
from collections import OrderedDict

class PartNameTranslation(OrderedAttibuteClass):
    def __init__(self, name_zh, name_en, name_ja):
        self.name_zh = name_zh
        self.name_en = name_en
        self.name_ja = name_ja

class BulletNameTranslation(OrderedAttibuteClass):
    def __init__(self, name_zh, name_en, name_ja):
        self.name_zh = name_zh
        self.name_en = name_en
        self.name_ja = name_ja

with open('part_name_dict.csv', 'rb') as f:
    file_contents = f.read().decode('utf-8').split('\r\n')
part_name_dict = OrderedDict()
for line in file_contents:
    line_split = line.split(',')
    if len(line_split) == 4:
        part_name_dict[line_split[0]] = PartNameTranslation(line_split[2], line_split[3], line_split[1])

with open('bullet_name_dict.csv', 'rb') as f:
    file_contents = f.read().decode('utf-8').split('\r\n')
bullet_name_dict = OrderedDict()
for line in file_contents:
    line_split = line.split(',')
    if len(line_split) == 4:
        bullet_name_dict[line_split[0]] = BulletNameTranslation(line_split[1], line_split[2], line_split[3])

def beautify_string(str, space_before_roman=True):
    if space_before_roman:
        str = str.replace('Ⅰ',' I').replace('Ⅱ',' II').replace('Ⅲ',' III').replace('Ⅳ',' IV')\
                .replace('Ⅴ',' V').replace('】 I','】I').replace('】 V','】V')
    str = unicodedata.normalize('NFKC', str)
    str = str.replace(',','，').replace('!','！').replace('?','？').replace(':','：').replace(';','；')
    return str

def verify_msg_name(msg_entry, name_str):
    return msg_entry.name.startswith(name_str) and not msg_entry.name.startswith(name_str+'_None')\
            and not 'Rejected' in msg_entry.content[0]

def translate_part_name(name):
    if name in part_name_dict:
        return part_name_dict[name]
    else:
        return None

def translate_bullet_name(name):
    if name in bullet_name_dict:
        return bullet_name_dict[name]
    else:
        return None

if __name__ == '__main__':
    print(translate_part_name('上半身').name_zh)
