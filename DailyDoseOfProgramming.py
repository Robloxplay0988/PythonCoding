import sys
import re 
import urllib.request
import urllib.error
import urllib.parse
import random 
import hashlib 
import requests 
import os
import argparse
import pyvirtualdisplay
from selenium import webdriver
import datetime
import time
y = ["y"]
n = ["n"]

timestamp_now = datetime.datetime.now().strftime('%Y-%m-%d')

print("""\n
#Written By nOt_tHe_CoDeR
#READ UP HERE ^
              |
# %%%%&&&&..............%%%/       Happy Teacher Appreciation Week Mrs McLean!
# %%%%&&&&.........&&&..%%%%%      
# %%%%&&&&.........&&&..%%%%%%%
# %%%%&&&&.........&&&..%%%%%%%    
# %%%%&&&&.........,,,..%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
# %%%%  _________________ .%%%%
# %%%%  _________________ .%%%%
# %%%%  _________________ .%%%%
# %%%%  _________________ .%%%%
# %%%%  _________________ .%%%%
# %%%%  _________________ .%%%%
# %&&%                    ,%&&%
# %&&%%%%%%%%%%%%%%%%%%%%%%%&&%
# %&&%%%%%%%%%%%%%%%%%%%%%%%&&%\n""")
# Flags
parser = argparse.ArgumentParser(description='DDoM v2.0')
parser.add_argument("-c", "--count", nargs=1, type=int, help="Defines the number of malware samples you want, up to 5000. If the argument is omitted, sets to 100 by default.",
                required=False, default=argparse.SUPPRESS, metavar="SAMPLES")
parser.add_argument("-r", "--rename", help="[Not recommended] Makes the samples executable. Don't use this unless you're confident you won't execute them on your host.",
                required=False, action="store_const", const=True)              
parser.add_argument("-y", "--yes-to-all", help="Skips the confirmation prompt.",
                required=False, action="store_const", const=True)

def confirmation(question, default="no"):    
    valid = {"yes": True, "y": True, "ye": True,
                "no": False, "n": False} 
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    validInputEntered = False
    while not validInputEntered:
        data = input("{}{}".format(question, prompt)).lower()
        if data in valid:
            validInputEntered = True
            return valid[data]
        if data == "":
            validInputEntered = True
            return default



args = parser.parse_args()
if not "count" in args:
    print("[*]  Resions why Mrs. McLean is the best teacher are completed - going with These Resions by defult")
    scount = 100
else:
    scount = args.count[0]

print("""\nYou'll get resions why Mrs. Mclean is the best teacher:
She Makes Class really Fun!
She Makes math fun and not boring!
She Reads really cool books!

""")

confirmed = confirmation("Confirm go With these Resions")
if not confirmed:
    sys.exit(0)

print("\nSearching...")

resion = " 1. She Makes Class really Fun! 2. She Makes math fun and not boring! 3. She Reads really cool books"
time.sleep(5)
print("\nWriting...")
time.sleep(5)
choice = input("The resions have been Wrote! Would you like to view it? (only answer in y or n)")
if choice in n:
    quit()
if choice in y:
    for count in range(65):
         print(resion)
         print("---------------------------------------------------------------")
         time.sleep(3)
# End of Script
#------------------------------------------------#




        
    
    
                      
           

           

                      




