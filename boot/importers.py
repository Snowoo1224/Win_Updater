import os
import sys
import subprocess

if os.name != "nt" :
    print(YL + "ERROR" + NO + " : This program unsupport at this platform.")
    input("Press Enter to Exit...")
    sys.exit()

try:
    from colorama import init, Fore
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])

try:
    import readchar
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "readchar"])

try:
    import win32com.client
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32"])