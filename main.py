import os
import sys
import platform
import readchar
from readchar import key
from colorama import init, Fore
os.system("mode con cols=80 lines=40")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def win_updater_logo():
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

GR = Fore.GREEN
YL = Fore.YELLOW
RD = Fore.RED
NO = Fore.WHITE
CY = Fore.CYAN

if os.name != "nt" :
    print(YL + "ERROR : this program unsupport at this platform.")
    input("Press Enter to Exit...")
    sys.exit()

win_updater_logo()
print("                    ┌─────────────────────────────────────┐")
print("                    │                                     │")
print("                    │       1 .  Host information         │")
print("                    │       2 .  Program information      │")
print("                    │       3 .  Update                   │")
print("                    │                                     │")
print("                    └─────────────────────────────────────┘")
choose = input()

if choose == "1" :
    clear_screen()
    win_updater_logo()
    print("                    ┌─────────────────────────────────────┐")
    print("                    │                                     │")
    print("                    │           Host information          │")
    print("                    │                                     │")
    print("                    │         Windows :", end=' ')
    print(platform.version() + "        │")
    print("                    │         Architecture :", end=' ')
    print(platform.machine() + "        │")
    print("                    │           Python :", end=' ')
    print(platform.python_version() + "           │")

    print("                    │                                     │")
    print("                    └─────────────────────────────────────┘")
    input()