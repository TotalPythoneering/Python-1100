#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyBanner1.py
# AUTHOR: Randall Nagy
#

def ShowStars(num):
    return "\t*" + ("*" * (num + 3))
            
def Show(message):
    xx = len(message)
    stars = ShowStars(xx)
    print(stars)
    print("\t* " + message + " *")
    print(stars)

Show("The is a MESSAGE")
