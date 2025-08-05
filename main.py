from boot.importers import *
from boot.helpers import *
import platform
import win32com.client
from colorama import init, Fore

init()

GR = Fore.GREEN
YL = Fore.YELLOW
MA = Fore.LIGHTMAGENTA_EX
NO = Fore.WHITE
BL = Fore.LIGHTBLUE_EX

if not is_admin() :
    run_as_admin(sys.argv[0])
    sys.exit()
    
if os.name != "nt" :
    print(YL + "ERROR" + NO + " : This program unsupport at this platform.")
    input("Press Enter to Exit...")
    sys.exit()
    
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
        print("                    │          Version : " + GR + "1.0.1R" + NO + "          │")
        print("                    │        Builder : " + BL + "Snowoo1224" + NO + "        │")
        print("                    │                                    │")
        print("                    └────────────────────────────────────┘")
        input()
        back_home()
            
    if choose == "3":
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            quick_py_path = os.path.join(current_dir, 'quick.py')
            python_exe = sys.executable
            result = subprocess.run([python_exe, quick_py_path])
            
            if result.returncode == 0:
                print("                          No update exists to install")
                input("                             Press Enter to Exit...")
                clear_screen()
                home_screen()
                
            if result.returncode == 1:
                clear_screen()
                home_screen()

        except FileNotFoundError:
            print("MISSING : [quick.py] file not found.")
        except Exception as e:
            print(f"ERROR : [quick.py] encountered a problem running.")