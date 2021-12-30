# MHR-DataExtraction
Heavily inspired by [mhrice](https://github.com/wwylele/mhrice), this project uses Python to extract data from Monster Hunter Rise (MHR) game files.

mhrice is an awesome project and very instructive in understanding the data structure of MHR files. Unfortunately, I have very limited knowledge in rust (only studied for two weeks for this project), which mhrice is written in, and the scripts themselves have few comments. This motivated me to write my own Python version of MHR data extractor, such that my Python-speaking friends and myself can use it more flexibly. 

## Preparation
This project starts with unpacked game data, so rather than working on the .pak file (which mhrice does), I already have a file structure of nested folders. To get this file structure, please follow these steps:

* Download raw data files from a hacked Switch. These links can be helpful: [recovery mode](https://www.youtube.com/watch?v=3-UeB_enPrM), [file dumping](https://yuzu-emu.org/help/quickstart/#dumping-cartridge-games), and [my dumping notes](HOW_TO_DUMP.md).
* There could be multiple raw files, with extensions like .xc0 or .xc1. Merge them into one .xci file. Merging is as easy as running the `copy /b "File1.xc0" + "File2.xc1" "FileOutput.xci"` command.
* Use [hactool](https://github.com/SciresM/hactool) to unpack the .xci file and obtain a .pak file (default name is re_chunk_000.pak).
* Use [REtool](https://residentevilmodding.boards.net/thread/10567/pak-tex-editing-tool) to unpack the .pak file and obtain the desired nested folders of game data. You will need a file list, which can be found [here](https://raw.githubusercontent.com/mhvuze/MonsterHunterRiseModding/main/files/mhrise.list). Save the following code as a batch (.bat) file and drag your .pak file over it to unpack.
```@setlocal enableextensions
@pushd %~dp0
.\REtool.exe -h mhrise.list -x -skipUnknowns %1
@popd
@pause
```

For unpacking, please also refer to [this link](https://github.com/mhvuze/MonsterHunterRiseModding/wiki/Extracting-Game-Files).

## Data structure
By 11/03/2021, I have only implemented reading some .user files (their actual extension is .user.2) that contain the magic "RSZ". These are number-based data, such as weapon, armor and monster stats.

All data are stored as binary files. The general file structure is magic (like "USR" and "RSZ") followed by some meta data, then many 64-bit keys which are murmur3 hashes of data type names. Then data are stored sequentially (in the order of these keys). Some data types may contain others as their values. It's important to note that the binary file should be read in little-endian fashion: the lowest 8 bits in each 32-bit chunk are on the left.

mhrice creates rust structs for different data types, while here I use Python classes. Each class has attributes in the exact same order as they appear in the data file, so the .user file reader knows which piece of data it's looking at. Moreover, the .user file reader needs to know how many bits each attribute takes up, which can be different depending on the type (int, float, bool, etc.). There are some observed rules about bit count and padding, which are handled generally in the code.

## How to run
The relevant game files are supposed to be stored under folders named with the prefix `game_file`. Inside such a folder, you need to run the copy file script (e.g. `copy_msg_files.py`) to copy the game files from their original location (i.e. the unpacked raw game data folder), which is poorly organized. After you have these folders populated with game files, just run `python pedia.py` from the root directory. This will create a pickle file inside `parse_pedia` folder, where it gets further parsed by the parsing scripts (e.g. `parse_monsters.py`).

The parsing scripts take in the pickle file and generate one or more json files containing human-readable data.
