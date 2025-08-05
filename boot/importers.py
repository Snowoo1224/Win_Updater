import sys
import subprocess

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