[preview]:          https://github.com/Saltssaumure/AutoBeatPack/blob/main/preview/preview.png?raw=true

[github]:           https://github.com/Saltssaumure/AutoBeatPack
[issues]:           https://github.com/Saltssaumure/AutoBeatPack/issues
[pullrequest]:      https://github.com/Saltssaumure/AutoBeatPack/pulls
[license]:          https://github.com/Saltssaumure/AutoBeatPack/blob/main/LICENSE

[discord]:          https://discord.gg/uy8nKQVatp

[shield-donate]:    https://img.shields.io/badge/Donate-ko--fi-orange?style=flat-square&logo=kofi&logoColor=orange
[ko-fi]:            https://ko-fi.com/saltssaumure "Buy me a coffee!"

# [AutoBeatPack][github]
[![Buy me a coffee on ko-fi][shield-donate]][ko-fi]

Automatic parallel download of osu! beatmap packs from the official source. No more relying on 3rd party mirrors or outdated lists.

![A screenshot of AutoBeatPack running in Powershell.][preview]

## Setup and usage
### Requirements
- Python >=3.4 (3.11-3.12 tested)

### Commands
All commands are run in the main AutoBeatPack folder.

1. Create virtual environment
   - `python -m venv .venv`
2. Activate virtual environment
   - PowerShell: `.venv\Scripts\Activate.ps1`  
   - Command Prompt: `.venv\Scripts\activate.bat`
   - macOS / Linux: `source myvenv/bin/activate`
3. Install requirements
   - `python -m pip install -r requirements.txt`
4. Run script
   - `python download.py`

## Config
This script has a `DEFAULT` config profile provided, which will download every standard osu! Beatmap Pack from 1 to 1411, in batches of 3, to `./beatpacks`

All of these values can be changed in `config.txt`.

### Variables
#### FirstPack
- Number of the first pack to be downloaded
- Use a whole number between 1 and `LastPack`
- Default: 1
#### LastPack
- Number of the last pack to be downloaded
- Use a whole number greater than 1
- Default: `1411`
#### BatchSize
- Maximum number of beatmaps to download at once
- Too high a number will cause all connections to drop (anti-spam), 1 to 10 recommended
- Default: `3`
#### DownloadFolder
- Location to store downloaded beatmap packs
- Relative to the main AutoBeatPack folder.
- Default: `beatpacks`

### Creating a new profile
You may want to have more than one profile for organisational or testing purposes.

1. Add a section to config.txt starting with the name of the profile in square brackets:
   ```
   [CoolProfileName]
   ```
2. Underneath, copy and edit variables you wish to change from the `DEFAULT` profile. Any missing variables will inherit its value from `DEFAULT` automatically.
   ```
   [CoolProfileName]
   StartPack = 750
   BatchSize = 6
   # This profile starts downloading at the 750th beatmap pack
   # And does it groups of 6
   ```
3. Save your changes before running `download.py`. Enter your profile name when prompted, without square brackets.

## License
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [GNU General Public License][license] for more details.

- <span title="Too long; didn't read; not a lawyer">TL;DR;NAL</span>: Do whatever you want with this, as long as you allow others to do the same.

## Questions or suggestions?
- Post [an issue][issues].
- Make [a pull request][pullrequest] if you're extra cool.
- Post on [my support server][discord].