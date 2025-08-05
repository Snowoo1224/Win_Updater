import os
import sys
import ctypes
import win32api
import win32con
from colorama import init, Fore

os.system("mode con cols=80 lines=39")

NO = Fore.WHITE
CY = Fore.CYAN

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def win_updater_logo():
    print()
    print()
    print()
    print("                    ┌────────────────────────────────────┐")
    print("                    │                                    │")
    print("                    │             " + CY + "╔═══╗ ╔═══╗" + NO + "            │")
    print("                    │             " + CY + "║   ║ ║   ║" + NO + "            │")
    print("                    │             " + CY + "╚═══╝ ╚═══╝" + NO + "            │")
    print("                    │             " + CY + "╔═══╗ ╔═══╗" + NO + "            │")
    print("                    │             " + CY + "║   ║ ║   ║" + NO + "            │")
    print("                    │             " + CY + "╚═══╝ ╚═══╝" + NO + "            │")
    print("                    │                                    │")
    print("                    │            " + CY + " Win Updater" + NO + "            │")
    print("                    │                                    │")
    print("                    └────────────────────────────────────┘")
    print()

def is_admin() :
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    
def run_as_admin(script_path):
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, script_path, None, 1)
    
def home_screen() :
    win_updater_logo()
    print("                    ┌────────────────────────────────────┐")
    print("                    │                                    │")
    print("                    │      1 . Host information          │")
    print("                    │      2 . Program information       │")
    print("                    │      3 . Update                    │")
    print("                    │                                    │")
    print("                    └────────────────────────────────────┘")
    
def back_home() :
        clear_screen()
        home_screen()
        
def startup(app_name, file_path):
    try:
        key = win32api.RegOpenKeyEx(
            win32con.HKEY_CURRENT_USER,
            "Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            0,
            win32con.KEY_SET_VALUE
        )
        win32api.RegSetValueEx(key, app_name, 0, win32con.REG_SZ, file_path)
        win32api.RegCloseKey(key)
        
    except Exception as e:
        print("ERROR : [df.py] encountered a problem running.")