#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_FormatAsciiComp.py
# AUTHOR: Randall Nagy
#

for base in 0x1202, 32:
    for offset in range(6):
        num = base + offset
        ## Operation Associations (L->R)
        print('%c' % num * 3)
        ## Escaped ASCII:
        # which = chr(num)
        # print(ascii(which), which)
