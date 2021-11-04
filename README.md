# MHR_DataExtraction
Heavily inspired by [mhrice](https://github.com/wwylele/mhrice), this project uses Python to extract data from Monster Hunter Rise (MHR) game files.

mhrice is an awesome project and very instructive in understanding the data structure of MHR files. Unfortunately, I have very limited knowledge in rust (only studied for two weeks for this project), which mhrice is written in, and the codes themselves have few comments. This motivated me to write my own Python version of MHR data extractor, such that my Python-speaking friends and myself can use it more flexibly. 

This project starts with unpacked game data, so rather than working on the .pak file (which mhrice does), I already have a file structure of nested folders. To get this file structure, please follow these steps:

* Download raw data files from a hacked Switch. These Youtube videos can be helpful: [recovery mode](https://www.youtube.com/watch?v=3-UeB_enPrM), [get product keys](https://www.youtube.com/watch?v=2LyNjylC7yY), and [get .xci file](https://www.youtube.com/watch?v=PGjEyI_YFuo&t=440s) 
* Merge raw files into one .xci file. Merging is as easy as running the `copy /b "File1.xc0" + "File2.xc1" "FileOutput.xci"` command.
* Use [hactool](https://github.com/SciresM/hactool) to unpack the .xci file and obtain a .pak file (default name is re_chunk_000.pak).
* Use [REtool](https://residentevilmodding.boards.net/thread/10567/pak-tex-editing-tool) to unpack the .pak file and obtain the file structure. You will need a file list, which can be found [here](https://raw.githubusercontent.com/mhvuze/MonsterHunterRiseModding/main/files/mhrise.list). Save the following codes as a batch (.bat) file and drag your .pak file over it to unpack.
```@setlocal enableextensions
@pushd %~dp0
.\REtool.exe -h mhrise.list -x -skipUnknowns %1
@popd
@pause```
