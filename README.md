# Shortcut Creator for Windows
This Python script creates a shortcut on the Windows desktop that links to a specified URL. It also sets a custom icon for the shortcut.

# Features
- Creates a desktop shortcut linking to a specific website.
- Copies a custom icon to the user's application data folder (APPDATA).
- Automatically sets the custom icon for the shortcut.

# Prerequisites
Before running the script, make sure you have the following Python libraries installed:
```sh
pip install -r requirements.txt
```

# How to Use
1. Clone this repository or copy the script to your local machine.
2. Prepare the icon. (Ensure that the icon file (icon.ico) is in the same directory as the script or bundled with it.)
3. Run the script: Run the script with Python. It will create a shortcut on your desktop that links to https://my_site.com.
```sh
python create_shortcut_windowns.py
```

# Bundling with PyInstaller
```sh
pyinstaller --onefile --windowed --name=gbby --icon=icon.ico --add-data "icon.ico;." create_shortcut_windowns.py
```
