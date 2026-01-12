# Welcome Screen (PySide6)

A simple Windows startup welcome screen built with Python and PySide6.
# Features 
- Displays a welcome message
- Shows user name
- Shows current time and date
- Updates time every second
- Can run automatically on Windows startup
- Optional frameless splash-style window

## Requirements
- Python 3.9+
- PySide6

Install dependencies:
```bash
pip install pyside6

# How To Run
python welcome_new.py

#Build Executable (WINDOWS)
pyinstaller --onefile --windowed welcome_new.py

#Auto Run On StartUp
Auto-Run on Startup
Build the .exe
Press Win + R → shell:startup
Place the .exe or shortcut in the Startup folder

#Project Structure

welcome-screen/
welcome_new.py
updater.py
version.txt
README.md
