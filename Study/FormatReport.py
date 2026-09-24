#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: FormatReport.py
# AUTHOR: Randall Nagy
# File: FormatReport.py
#

''' Report Creation:
1.) Name – Left-justified in 15 spaces
2.) Number – Zero-filled in 5 spaces
3.) Balance – Right-justified in 9 spaces
    (implies .00?)
'''

user = ("Randall", 123, 123.456)
print('Name: %-15s, \
Number: %05.d, \
Bal: [%9.2f]' % user)



