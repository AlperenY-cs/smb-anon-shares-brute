#!/usr/bin/python3

import os
import subprocess

# Define target and wordlist
TARGET = ""
WORDLIST = ""

# Check wordlist file
if not os.path.isfile(WORDLIST):
    print(f"Wordlist not found: {WORDLIST}")
    exit(1)

# Read all lines of wordlist
with open(WORDLIST, "r") as file:
    for line in file:
        SHARE = line.strip()  # Remove space
        if not SHARE: 
            continue
        
        command = ["smbclient", f"//{TARGET}/{SHARE}", "-N", "-c", "ls"]
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        if result.returncode == 0:
            print(f"[+] Anonymous access allowed for: {SHARE}")
      
