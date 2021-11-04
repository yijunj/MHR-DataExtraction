# MHR_DataExtraction
Heavily inspired by [mhrice](https://github.com/wwylele/mhrice "mhrice"), this project uses Python to extract data from Monster Hunter Rise (MHR) game files.

mhrice is an awesome project and very instructive in understanding the data structure of MHR files. Unfortunately, I have very limited knowledge in rust (only studied for two weeks for this project), which mhrice is written in, and the codes themselves have few comments. This motivated me to write my own Python version of MHR data extractor, such that my Python-speaking friends and myself can use it more flexibly. 

This project starts with unpacked game data, so rather than working on the .pak file (which mhrice does), I already have a file structure of nested folders. To get this file structure, please follow these steps:

* Download raw data files from a hacked Switch. These Youtube videos can be helpful: [enter recovery mode](https://www.youtube.com/watch?v=3-UeB_enPrM "Enter recovery mode"), [get product keys](https://www.youtube.com/watch?v=2LyNjylC7yY "Dump prod.keys"), [get .xci file](https://www.youtube.com/watch?v=PGjEyI_YFuo&t=440s "Dump .xci from cartridge") 
* Merge raw files into one .xci file.
* Use hactool to unpack the .xci file and obtain the .pak file (default name is re_chunk_000.pak).
* Use REtool to unpack the .pak file and obtain the file structure.
