
import time
import platform
import os
from tqdm import tqdm
import random


__App_Version__ = '2.0'
__App_Name__ = 'PassGen'

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile "PassGen.py"
###
### Website: http://www.hypernylium.com
###
### GitHub: https://github.com/HyperNylium/PassGen
###
### License: Mozilla Public License Version 2.0
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug.
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Text Colors
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_CYAN = "\033[36m"
CLR_WHİTE = "\033[37m"
# Background Colors
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_CYAN = "\033[46m"
BG_WHİTE = "\033[47m"
# Styles 
BRİGHT = "\033[1m"
RESET_ALL = "\033[0m"

clear_command = "cls" if platform.system() == "Windows" else "clear"

Numbers = "12345689"
Uppercase_Letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lowercase_Letters = "abcdefghijklmnopqrstuvwxyz"
Simbols = "!$"

upper, lower, nums, syms = True, True, True, True
all = ""
if upper:
    all += Uppercase_Letters
if lower:
    all +=Lowercase_Letters
if nums:
    all += Numbers
if syms:
    all += Simbols

passlength = 15
amount = 50

for x in range(amount):

 def LoadingSequence():

    os.system(clear_command)
    for i in tqdm(range(100), unit="KB", position=2, desc=" Getting Ready To Generate"):
        time.sleep(0.04)
    os.system(clear_command)
    passgen()

 def passgen():

    os.system(clear_command)
    password1 = "".join(random.sample(all, passlength))
    password2 = "".join(random.sample(all, passlength))
    password3 = "".join(random.sample(all, passlength))
    password4 = "".join(random.sample(all, passlength))
    password5 = "".join(random.sample(all, passlength))
    password6 = "".join(random.sample(all, passlength))
    password7 = "".join(random.sample(all, passlength))
    password8 = "".join(random.sample(all, passlength))
    password9 = "".join(random.sample(all, passlength))
    password10 = "".join(random.sample(all, passlength))
    password11 = "".join(random.sample(all, passlength))
    password12 = "".join(random.sample(all, passlength))
    password13 = "".join(random.sample(all, passlength))
    password14 = "".join(random.sample(all, passlength))
    password15 = "".join(random.sample(all, passlength))
    RESET_ALL

    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " Google "+ RESET_ALL + "Password:    " + password1)
    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " Facebook "+ RESET_ALL + "Password:    " + password2)
    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " İnstagram "+ RESET_ALL + "Password:    " + password3)
    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " Tiktok "+ RESET_ALL + "Password:    " + password4)
    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " Github "+ RESET_ALL + "Password:    " + password5)
    print(CLR_CYAN + "\n     Suggested" + CLR_YELLOW + " Youtube "+ RESET_ALL + "Password:    " + password6)
    RESET_ALL

    print(CLR_YELLOW + "\n    ============ Other Suggested Passwords ============    \n" + RESET_ALL)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password7)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password8)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password9)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password10)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password11)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password12)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password13)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password14)
    print(CLR_CYAN + "     Suggested Password:     " + RESET_ALL + password15)
    RESET_ALL

    print(CLR_CYAN + "\n     press 'q' to quit the app")
    print(CLR_CYAN + "     press 'r' to generate new passwords")

    input_ = input("\n====> ")

    if input_ == "r":
        passgen()

    if input_ == "R":
        passgen()

    if input_ == "q":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App")
        time.sleep(1)
        RESET_ALL
        os.system(clear_command)
        exit()

    if input_ == "Q":
        os.system(clear_command)
        print(CLR_RED + "\n\n\n          Terminating App")
        time.sleep(1)
        RESET_ALL
        os.system(clear_command)
        exit()

os.system(clear_command)
print(CLR_CYAN + "\n\n            Welcome To PassGen")
RESET_ALL
input(CLR_GREEN + "\n    Press 'Enter' to start generating a password")
RESET_ALL
LoadingSequence()