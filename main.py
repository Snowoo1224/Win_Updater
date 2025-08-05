from imports import *
from df import *
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
        print("                    ┌─────────────────────────────────────┐")
        print("                    │                                     │")
        print("                    │           " + YL + "Host information" + NO + "          │")
        print("                    │                                     │")
        print("                    │         Windows :" + CY + "", end=' ')
        print(platform.version() + NO + "        │")
        print("                    │         Architecture :" + MA + "", end=' ')
        print(platform.machine() + NO + "        │")
        print("                    │           Python :" + YL + "", end=' ')
        print(platform.python_version() + NO + "           │")
        print("                    │                                     │")
        print("                    └─────────────────────────────────────┘")
        input()
        back_home()
        
    if choose == "2" :
        clear_screen()
        print()
        print()
        print()
        print("                    ┌─────────────────────────────────────┐")
        print("                    │                                     │")
        print("                    │             " + CY + "╔═══╗ ╔═══╗" + NO + "             │")
        print("                    │             " + CY + "║   ║ ║   ║" + NO + "             │")
        print("                    │             " + CY + "╚═══╝ ╚═══╝" + NO + "             │")
        print("                    │             " + CY + "╔═══╗ ╔═══╗" + NO + "             │")
        print("                    │             " + CY + "║   ║ ║   ║" + NO + "             │")
        print("                    │             " + CY + "╚═══╝ ╚═══╝" + NO + "             │")
        print("                    │                                     │")
        print("                    │        " + YL + " Program information" + NO + "         │")
        print("                    │                                     │")
        print("                    │          Version : " + GR + "1.0.0R" + NO + "           │")
        print("                    │        Builder : " + BL + "Snowoo1224" + NO + "         │")
        print("                    │                                     │")
        print("                    └─────────────────────────────────────┘")
        input()
        back_home()
            
    if choose == "3" :
        clear_screen()
        win_updater_logo()
        print("                    ┌─────────────────────────────────────┐")
        print("                    │                                     │")
        print("                    │        Getting information...       │")
        print("                    │                                     │")
        print("                    └─────────────────────────────────────┘")
        update_session = win32com.client.Dispatch("Microsoft.Update.Session")
        update_searcher = update_session.CreateUpdateSearcher()
        search_result = update_searcher.Search("IsInstalled=0")
        clear_screen()
        win_updater_logo()
        
        if search_result.Updates.Count == 0 :
            print("                          No update exists to install")
            input("                             Press Enter to Exit...")
            clear_screen()
            home_screen()
            
        else :
            print("                       An update has been found. (", search_result.Updates.Count, ")")
            yorn = input("                       Do you want to update it? (Y/N) ")
            if yorn.lower() in ["yes" , "y"] :
                clear_screen()
                win_updater_logo()
                updates_to_download = win32com.client.Dispatch("Microsoft.Update.UpdateColl")
                
                for i in range(search_result.Updates.Count):
                    update = search_result.Updates.Item(i)
                    print({update.Title})
                    updates_to_download.Add(update)   

                downloader = update_session.CreateUpdateDownloader()
                downloader.Updates = updates_to_download
                download_result = downloader.Download()
                
                if download_result.ResultCode == 2 :
                    installer = update_session.CreateUpdateInstaller()
                    installer.Updates = updates_to_download
                    installation_result = installer.Install()
                    input("Update installation is complete.")