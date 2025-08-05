from boot.helpers import *
import os
import winsound
import win32com.client
from colorama import init, Fore

NO = Fore.WHITE
YL = Fore.YELLOW

os.system("mode con cols=80 lines=39")

startup("Win_Updater", os.path.abspath(__file__))

win_updater_logo()
print("                    ┌────────────────────────────────────┐")
print("                    │               " + YL + "Loading" + NO + "              │")
print("                    └────────────────────────────────────┘")

update_session = win32com.client.Dispatch("Microsoft.Update.Session")
update_searcher = update_session.CreateUpdateSearcher()
search_result = update_searcher.Search("IsInstalled=0")

clear_screen()
win_updater_logo()

if search_result.Updates.Count == 0 :
    sys.exit(0)
    
else :
    winsound.PlaySound('SystemQuestion', winsound.SND_ALIAS) 
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
            print("                        Update installation is complete.")
            input("                             Press Enter to Exit...")
            sys.exit(-1)