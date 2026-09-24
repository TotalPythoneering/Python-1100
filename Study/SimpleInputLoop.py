# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: SimpleInputLoop.py
# AUTHOR: Randall Nagy
#
zOpts = ("Loop", "Break")

while True:
    for ss, opt in enumerate(zOpts, 1):
        print(ss, ".)", opt)
    zChoice = input("What number? ")
    if zChoice is "2":
        break
    print("Looping ...")
