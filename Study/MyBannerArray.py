#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyBannerArray.py
# AUTHOR: Randall Nagy
#

prefix = ("DEBUG", "WARNING", "ERROR", "MESSAGE")

def ShowChars(num, token):
    return "\t" + (token * (num + 4))
            
def Show(ss, message):
    if ss < 1:
        ss = 1
    if ss > 4:
        ss = 4
    message = prefix[ss - 1] + ": " + message
    xx = len(message)
    stars = ShowChars(xx, '*')
    print(stars)
    print("\t* " + message + " *")
    print(stars)

Show(4, "The is a MESSAGE")
Show(1, "Doh!")
