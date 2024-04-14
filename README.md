# AutoBeatPack

Automatic parallel download of osu! beatmap packs from the official source. No more relying on 3rd party mirrors or outdated lists.

## Setup and usage
### Requirements
- Python >=3.4 (3.12 tested)

### Commands
All commands are run in the main AutoBeatPack folder.

1. Create virtual environment
   - `python -m venv .venv`
2. Activate virtual environment
   - PowerShell: `.venv\Scripts\Activate.ps1`  
   - Command Prompt: `.venv\Scripts\activate.bat`
   - macOS / Linux: `source myvenv/bin/activate`
3. Run script
   - `python download.py`