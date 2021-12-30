import shutil
import os
import json

pak_dir = 'M:\\MHR game data extraction\\[PAK TO DATA] Switch RETool hacking\\natives_patch007\\NSW'

# Copy large monster user files
for id in range(1000):
    for sub_id in range(10):
        pfb_path = os.path.join(pak_dir,\
            'enemy\\em{:03}\\{:02}\\prefab\\em{:03}_{:02}.pfb.17'.format(id, sub_id, id, sub_id))
        if not os.path.exists(pfb_path):
            continue
        from_path = os.path.join(pak_dir,\
            'enemy\\em{:03}\\{:02}\\collision\\em{:03}_{:02}_colliders.rcol.18'.format(id, sub_id, id, sub_id))
        to_path = 'em{:03}_{:02}_colliders.rcol.18'.format(id, sub_id)
        try:
            shutil.copy2(from_path, to_path)
        except FileNotFoundError:
            print('Cannot find path {}'.format(from_path))

# Copy small monster user files
for id in range(1000):
    for sub_id in range(10):
        pfb_path = os.path.join(pak_dir,\
            'enemy\\ems{:03}\\{:02}\\prefab\\ems{:03}_{:02}.pfb.17'.format(id, sub_id, id, sub_id))
        if not os.path.exists(pfb_path):
            continue
        from_path = os.path.join(pak_dir,\
            'enemy\\ems{:03}\\{:02}\\collision\\ems{:03}_{:02}_colliders.rcol.18'.format(id, sub_id, id, sub_id))
        to_path = 'ems{:03}_{:02}_colliders.rcol.18'.format(id, sub_id)
        try:
            shutil.copy2(from_path, to_path)
        except FileNotFoundError:
            print('Cannot find path {}'.format(from_path))
