from boot.importers import *


setup_console()


while True :
    selected_choice = home_move()
    if selected_choice == 0 :
        clear_screen()
        win_updater_logo()
        print(" " * 10 + "┌"+"─" * 36 + "┐")
        print(" " * 10 + "│"+" " * 36 + "│")
        print(" " * 10 + "│          " + YL + "Host information" + NO + " " * 10 + "│")
        print(" " * 10 + "│" + " " * 36 + "│")
        print(" " * 10 + "│        Windows :" + CY + "", end=' ')
        print(platform.version() + NO + " " * 8 + "│")
        print(" " * 10 + "│        Architecture :" + MA + "", end=' ')
        print(platform.machine() + NO + " " * 8 + "│")
        print(" " * 10 + "│          Python :" + YL + "", end=' ')
        print(platform.python_version() + NO + " " * 11 + "│")
        print(" " * 10 + "│"+" " * 36 + "│")
        print(" " * 10 + "└"+"─" * 36 + "┘")
        keyboard.wait("enter")
        time.sleep(0.25)


    elif selected_choice == 1 :
        clear_screen()
        print()
        print()
        print()
        print()
        print(" " * 10 + "┌"+"─" * 36 + "┐")
        print(" " * 10 + "│"+" " * 36 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "╔═══╗ ╔═══╗" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "║   ║ ║   ║" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "╚═══╝ ╚═══╝" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "╔═══╗ ╔═══╗" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "║   ║ ║   ║" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 13 + CY + "╚═══╝ ╚═══╝" + NO + " " * 12 + "│")
        print(" " * 10 + "│" + " " * 36 + "│")
        print(" " * 10 + "│        " + YL + " Program information" + NO + " " * 8 + "│")
        print(" " * 10 + "│" + " " * 36 + "│")
        print(" " * 10 + "│          Version : " + GR + "1.0.6R" + NO + " " * 10 + "│")
        print(" " * 10 + "│        Builder : " + BL + "Snowoo1224" + NO + " " * 8 + "│")
        print(" " * 10 + "│"+" " * 36 + "│")
        print(" " * 10 + "└"+"─" * 36 + "┘")
        keyboard.wait("enter")
        time.sleep(0.25)


    elif selected_choice == 2 :
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            quick_py_path = os.path.join(current_dir, 'quick', 'quick.exe')
            result = subprocess.run([quick_py_path])
            
        except FileNotFoundError :
            print()
            winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
            print(" " * 11 + RD + "MISSING" + NO + " : [quick.exe] file not found.")
            print(" " * 18 + "Press Enter to Exit...")
            keyboard.wait("enter")
            sys.exit()
            
        except Exception as e :
            print()
            winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
            print("    " + YL + "ERROR" + NO + " : [quick.exe] encountered a problem running.")
            print(" " * 18 + "Press Enter to Exit...")
            keyboard.wait("enter")
            sys.exit()