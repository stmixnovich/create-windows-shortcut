import os
import winshell
import win32com.client
import shutil
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def create_shortcut_windowns():
    desktop = winshell.desktop()

    shortcut_path = os.path.join(desktop, 'gbby.lnk')

    target = "https://my_site.com"

    appdata_dir = os.path.join(os.getenv('APPDATA'), 'gbby')

    if not os.path.exists(appdata_dir):
        os.makedirs(appdata_dir)

    icon_path = os.path.join(appdata_dir, 'gb5.ico')

    original_icon = resource_path('icon.ico')
    if not os.path.exists(icon_path):
        shutil.copyfile(original_icon, icon_path)

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = target
    shortcut.WorkingDirectory = desktop
    shortcut.IconLocation = icon_path
    shortcut.save()

    print(f"Shortcut was created: {shortcut_path}")

if __name__ == '__main__':
    create_shortcut_windowns()
