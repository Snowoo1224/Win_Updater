from boot.importers import *

import platform
from colorama import Fore

GR = Fore.GREEN
YL = Fore.YELLOW
MA = Fore.LIGHTMAGENTA_EX
NO = Fore.WHITE
BL = Fore.LIGHTBLUE_EX
CY = Fore.CYAN

def setup_console():
    os.system("mode con cols=79 lines=39")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def back_home() :
        clear_screen()
        home_screen()   

def home_screen() :
    win_updater_logo()
    print("                    ┌────────────────────────────────────┐")
    print("                    │                                    │")
    print("                    │      1 . Host information          │")
    print("                    │      2 . Program information       │")
    print("                    │      3 . Update                    │")
    print("                    │                                    │")
    print("                    └────────────────────────────────────┘")    
    
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
    
setup_console()
home_screen()

while True :
    choose = input()
    if choose == "1" :
        clear_screen()
        win_updater_logo()
        print("                    ┌────────────────────────────────────┐")
        print("                    │                                    │")
        print("                    │          " + YL + "Host information" + NO + "          │")
        print("                    │                                    │")
        print("                    │        Windows :" + CY + "", end=' ')
        print(platform.version() + NO + "        │")
        print("                    │        Architecture :" + MA + "", end=' ')
        print(platform.machine() + NO + "        │")
        print("                    │          Python :" + YL + "", end=' ')
        print(platform.python_version() + NO + "           │")
        print("                    │                                    │")
        print("                    └────────────────────────────────────┘")
        input()
        back_home()
        
    if choose == "2" :
        clear_screen()
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
        print("                    │        " + YL + " Program information" + NO + "        │")
        print("                    │                                    │")
        print("                    │          Version : " + GR + "1.0.3R" + NO + "          │")
        print("                    │        Builder : " + BL + "Snowoo1224" + NO + "        │")
        print("                    │                                    │")
        print("                    └────────────────────────────────────┘")
        input()
        back_home()
            
    if choose == "3":
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            quick_py_path = os.path.join(current_dir, 'quick', 'quick.exe')
            result = subprocess.run([quick_py_path])
            
            if result.returncode == 0 :
                clear_screen()
                home_screen()
                
            if result.returncode == 1 :
                clear_screen()
                home_screen()

        except FileNotFoundError:
            print("MISSING : [quick.py] file not found.")
            
        except Exception as e:
            print(f"ERROR : [quick.py] encountered a problem running.")