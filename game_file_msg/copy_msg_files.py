import shutil
import os
import time
import json

# Reads file names and directories of the relevant msg files
with open('msg_file_list.csv', 'r') as f:
    msg_file_list = f.read().split('\n')

# Copy these msg files from the pak folder to the current folder
pak_dir = 'M:\\MHR game data extraction\\[PAK TO DATA] Switch RETool hacking\\natives\\NSW'
msg_file_dict = {}
for line in msg_file_list:
    msg_file_dict[line.split(',')[0].strip()] = {'file':line.split(',')[1].strip(), 'dir':line.split(',')[2].strip()}
for key in msg_file_dict.keys():
    shutil.copy2(os.path.join(pak_dir, msg_file_dict[key]['dir']), msg_file_dict[key]['file'])
time.sleep(5)

# Dump file names into json
with open('msg_file_list.json', 'w') as f:
    json.dump(msg_file_dict, f)
