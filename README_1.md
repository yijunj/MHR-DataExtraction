# Preparing SD card
## Install/Update Atmosphere and Hekate
Atmosphere is like the operation system of CFW mode, and Hekate is how you boot Switch into Atmosphere.
Copied from https://nh-server.github.io/switch-guide/extras/updating/

### Updating Atmosphere
When a new version of Atmosphere releases, you can update Atmosphere by following these steps:

Turn off your Nintendo Switch and plug your SD card in your computer.
Download the latest release of Atmosphere (Download the atmosphere-(version)-master-(version)+hbl-(version)+hbmenu-(version).zip release of Atmosphere.)
Copy the contents of the Atmosphere .zip file to the root of your SD card.

Download fusee.bin from Atmosphere GitHub and put it under SD card bootloader/payloads directory, and then add this to bootloader/hekate_ipl.ini

[Payload Fusee]
fss0=bootloader/payloads/fusee.bin

If you are prompted to overwrite files, do so.
(If your hekate is not on the latest version) Update hekate via the steps below.
Put your SD card back in your Switch and launch CFW.

### Updating Hekate
When a new version of Hekate releases, you can update by following these steps:

Turn off your Nintendo Switch and plug your SD card in your computer.
Download the latest version of Hekate (Download the hekate_ctcaer_(version).zip release of hekate).
Copy the bootloader folder from the Hekate .zip file to the root of your SD card. If you are asked to overwrite or merge files while copying, say yes to merge/overwrite them.
Put your SD card back in your Switch and launch Hekate.
Go to the Options tab at the top right of the screen. Turn "Update Reboot 2 Payload" on the bottom right ON (if it isn't on already). Tap "Save Options" at the bottom of the screen.

### Homebrew Appstore
https://github.com/fortheusers/hb-appstore/releases
Switch: copy appstore.nro to sd:/switch/appstore/appstore.nro

### Keys
Make sure prod.keys and title.keys are under an SD card directory named "switch". If you don't have the keys, you need to dump them first by launching Lockpick_RCM.bin from Hekate.

# Launch Hekate
## Boot into recovery mode
With Switch turned off, ground the correct pins on the right controller slot. Connect Switch to PC through USB, open TegraRcmGUI on PC. The Switch icon should be red saying "NO RCM".
Press volume up button and power button on Switch to boot into RCM (recovery mode). The Switch should show black screen, but TegraRcmGUI should turn green saying "RCM OK".
Inject the Hekate payload. This launches Hekate on Switch.

# Launch Atmosphere
In Hekate, click Launch then choose fusee.bin. Now you can unground the pins and put back joy-cons.

Useful apps to dump files (here I use NXDumpTool) are in the hbmenu by pressing the Album button. If it's not installed, you need to connect to the internet and install via Homebrew App Store.

# Using NXDumpTool
Copied from https://zeldamods.org/wiki/Help:Dumping_games

Dump the game files directly to your SD card using nxdumptool. Update data can only be processed if the base game is available, because they share the same filesystem. DLCs don't, so they have to be dumped separately.
Warning: If you misbehave (piracy, online cheating or anything equally stupid), you might get banned from Nintendo online services. If you do not want to leave any traces, turn on airplane mode, back up your eMMC before running any homebrew and do not ever go online before you have restored the backup.

Keys file generated using Lockpick_RCM, located at sdmc:/switch/prod.keys. Run the payload on your console through RCM in order to dump the keys needed by nxdumptool to decrypt contents.
Dumping game files
On your Switch, open nxdumptool. Afterwards:
If you have the gamecard: Select Dump gamecard content.
If you have the eShop version: Select Dump SD card / eMMC content, then select BotW.
Select RomFS options.
Highlight the Use update/DLC option and use the left/right buttons to cycle through the available updates/DLCs for the game.
If you have no available updates/DLCs, this option won't appear. You'll only be able to dump the files from the non-updated base game (which is the same to just leaving this option set to No).
Updates are tagged as (UPD), and they use 01007EF00011E800 as their ID. v786432 corresponds to BotW v1.6.0 update.
DLCs are tagged as (DLC). 01007EF00011F001 and 01007EF00011F002 are the known IDs for the existent BotW DLCs.
Select RomFS section data dump and wait for the process to finish. This will dump the internal filesystem from the selected update/DLC to the inserted SD card.
Just like it was previously mentioned, updates share their filesystem data with the base game, so dumping the RomFS from an update is equivalent to dumping the whole filesystem from the updated game data. In other words, it isn't necessary to dump the base game filesystem separately if you choose an update.

DLCs, on the other hand, must be dumped separately.

When you're done, you'll be able to find the output dumps in sdmc:/switch/nxdumptool/RomFS.

Dumping binaries (executable files)
Executables in Switch titles are stored in a different section known as the ExeFS, which is only available in base games and updates. Unlike RomFS data, ExeFS data isn't shared between the update and its base game.

These files can also be dumped using nxdumptool.

On your Switch, open nxdumptool. Afterwards:
If you have the gamecard: Select Dump gamecard content.
If you have the eShop version: Select Dump SD card / eMMC content, then select BotW.
Select ExeFS options.
Highlight the Use update option and use the left/right buttons to cycle through the available updates for the game.
If you have no available updates, this option won't appear. You'll only be able to dump the binaries from the non-updated base game (which is the same to just leaving this option set to No).
Updates use 01007EF00011E800 as their ID. v786432 corresponds to BotW v1.6.0 update.
Select ExeFS section data dump and wait for the process to finish. This will dump the binaries from the selected update to the inserted SD card.
When you're done, you'll be able to find the output dump in sdmc:/switch/nxdumptool/ExeFS.
