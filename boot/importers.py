import os
import sys
import time
import ctypes
import platform
import winsound
import keyboard
import subprocess

try :
    from colorama import init, Fore
except ModuleNotFoundError :
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])

try :
    import readchar
except ModuleNotFoundError :
    subprocess.check_call([sys.executable, "-m", "pip", "install", "readchar"])

try :
    import win32com.client
except ModuleNotFoundError :
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
    
try :
    import keyboard
except ModuleNotFoundError :
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])
    
GR = Fore.GREEN
YL = Fore.YELLOW
MA = Fore.LIGHTMAGENTA_EX
NO = Fore.WHITE
BL = Fore.LIGHTBLUE_EX
CY = Fore.CYAN

selected_index = 0

def setup_console() :
    os.system("mode con cols=58 lines=39")

def clear_screen() :
    os.system('cls' if os.name == 'nt' else 'clear')
    
def is_admin() :
    try :
        return ctypes.windll.shell32.IsUserAnAdmin()
    except :
        return False  
    
def win_updater_logo() :
    print()
    print()
    print()
    print()
    print(" "*10+"┌"+"─"*36+"┐")
    print(" "*10+"│"+" "*36+"│")
    print(" "*10+"│             " + CY + "╔═══╗ ╔═══╗" + NO + " "*12+"│")
    print(" "*10+"│             " + CY + "║   ║ ║   ║" + NO + " "*12+"│")
    print(" "*10+"│             " + CY + "╚═══╝ ╚═══╝" + NO + " "*12+"│")
    print(" "*10+"│             " + CY + "╔═══╗ ╔═══╗" + NO + " "*12+"│")
    print(" "*10+"│             " + CY + "║   ║ ║   ║" + NO + " "*12+"│")
    print(" "*10+"│             " + CY + "╚═══╝ ╚═══╝" + NO + " "*12+"│")
    print(" "*10+"│                                    │")
    print(" "*10+"│            " + CY + " Win Updater" + NO + " "*12+"│")
    print(" "*10+"│"+" "*36+"│")
    print(" "*10+"└"+"─"*36+"┘")
    print()

def home_move() :
    global selected_index
    menu_items = ["Host information", "Program information", "Update"]

    while True :
        clear_screen()
        win_updater_logo()
        
        print(" "*10+"┌"+"─"*36+"┐")
        print(" "*10+"│"+" "*36+"│")

        for i, item in enumerate(menu_items) :
            if i == selected_index :
                print(f"          │     {YL}>>{NO}  {item:<25}  │")
            else :
                print(f"          │        {item:<25}   │")

        print(" "*10+"│"+" "*36+"│")
        print(" "*10+"└"+"─"*36+"┘")
        
        key = keyboard.read_key()

        if key == "down" :
            selected_index = (selected_index + 1) % len(menu_items)
            
        elif key == "up" :
            selected_index = (selected_index - 1 + len(menu_items)) % len(menu_items)
            
        elif key == "enter" :
            return selected_index
            
        time.sleep(.16)

if os.name != "nt" :
    print(YL + "ERROR" + NO + " : This program unsupport at this platform.")
    input("Press Enter to Exit...")
    sys.exit()

