# How to dump Switch game files
Atmosphere is a Switch CFW (custom firmware) where you can dump game files, and Hekate is how you boot Switch into Atmosphere. To launch Hekate, you need to boot your Switch into RCM (recovery mode) first. This requires a prepared SD card, USB connection between Switch and PC, and a way to ground Switch pin #10 on the right joy-con slot.

[This link](https://yuzu-emu.org/help/quickstart/#dumping-cartridge-games) talks about file dumping in more detail.

## Preparing SD card
Please check [this useful reference](https://nh-server.github.io/switch-guide/extras/updating/).

### Atmosphere
When a new version of Atmosphere releases, you can update Atmosphere by following these steps:
* [Download](https://github.com/Atmosphere-NX/Atmosphere/releases) the latest release of Atmosphere (Download the `atmosphere-(version)-master-(version)+hbl-(version)+hbmenu-(version).zip` release of Atmosphere.)
* Copy the contents of the Atmosphere .zip file to the root of your SD card.
* If you are prompted to overwrite files, do so.
* Download `fusee.bin` from Atmosphere GitHub and put it under SD card `sd:/bootloader/payloads` directory, and then add this to `sd:/bootloader/hekate_ipl.ini`
```
[Payload Fusee]
fss0=atmosphere/package3
```

### Hekate
When a new version of Hekate releases, you can update by following these steps:
* [Download](https://github.com/CTCaer/Hekate/releases/) the latest version of Hekate (Download the `hekate_ctcaer_(version).zip` release of hekate).
* Copy the bootloader folder from the Hekate .zip file to the root of your SD card. If you are asked to overwrite or merge files while copying, say yes to merge/overwrite them.

### Homebrew App Store
[Download](https://github.com/fortheusers/hb-appstore/releases) Homebrew App Store and copy `appstore.nro` to `sd:/switch/appstore/appstore.nro`.

### Keys
Make sure `prod.keys` and `title.keys` are under an SD card directory `switch`. If you don't have the keys, you can dump them first by launching `Lockpick_RCM.bin` from Hekate, which can be downloaded [here](https://github.com/shchmue/Lockpick_RCM/releases). Put it under `sd:/bootloader/payloads` and it is launchable in Hekate just like Atmosphere (see below).

## Booting into RCM and launching Hekate
* With Switch turned off, insert the just prepared SD card. Ground pin #10 on the right joy-con slot. Connect Switch to PC through USB, open `TegraRcmGUI.exe` on PC. The Switch icon should be red saying "NO RCM".
* Press volume up button and power button on Switch to boot into RCM (recovery mode). The Switch should show black screen, but `TegraRcmGUI` should turn green saying "RCM OK".
* Inject the Hekate payload. This launches Hekate on Switch.

## Launching Atmosphere
In Hekate, click Launch then choose `fusee.bin`. Now you can unground the pins and put back joy-cons.

Useful apps to dump files (here I use NXDumpTool) are in the hbmenu by pressing the Album button. If it's not installed, you need to connect to the internet and install via Homebrew App Store.

## Using NXDumpTool
Please check [this useful reference](https://zeldamods.org/wiki/Help:Dumping_games).

Dump the game files directly to your SD card using nxdumptool. Update data can only be processed if the base game is available, because they share the same filesystem. DLCs don't, so they have to be dumped separately.

**Turn on airplane mode before dumping!**

### Dumping game files
On your Switch, open `nxdumptool`. Afterwards:
* If you have the gamecard: Select Dump gamecard content.
* If you have the eShop version: Select Dump SD card / eMMC content.

Select RomFS options. Highlight the Use update/DLC option and use the left/right buttons to cycle through the available updates/DLCs for the game.
If you have no available updates/DLCs, this option won't appear. You'll only be able to dump the files from the non-updated base game (which is the same to just leaving this option set to No).
* Updates are tagged as (UPD).
* DLCs are tagged as (DLC).

Select RomFS section data dump and wait for the process to finish. This will dump the internal filesystem from the selected update/DLC to the inserted SD card.
Just like it was previously mentioned, updates share their filesystem data with the base game, so dumping the RomFS from an update is equivalent to dumping the whole filesystem from the updated game data. In other words, it isn't necessary to dump the base game filesystem separately if you choose an update. DLCs, on the other hand, must be dumped separately. When you're done, you'll be able to find the output dumps in `sd:/switch/nxdumptool/RomFS`.

### Dumping binaries (executable files)
Executables in Switch titles are stored in a different section known as the ExeFS, which is only available in base games and updates. Unlike RomFS data, ExeFS data isn't shared between the update and its base game.

These files can also be dumped using nxdumptool. On your Switch, open nxdumptool. Afterwards:
* If you have the gamecard: Select Dump gamecard content.
* If you have the eShop version: Select Dump SD card / eMMC content.

Select ExeFS options. Highlight the Use update option and use the left/right buttons to cycle through the available updates for the game.
* If you have no available updates, this option won't appear. You'll only be able to dump the binaries from the non-updated base game (which is the same to just leaving this option set to No).

Select ExeFS section data dump and wait for the process to finish. This will dump the binaries from the selected update to the inserted SD card. When you're done, you'll be able to find the output dump in `sd:/switch/nxdumptool/ExeFS`.
