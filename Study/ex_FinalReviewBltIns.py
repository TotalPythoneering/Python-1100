#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_FinalReviewBltIns.py
# AUTHOR: Randall Nagy
# File: ex_FinalReviewBltIns.py
#

from words2 import words

for ss, func in enumerate(words):
    if not ss % 2:
       print()
    print(f'{ss+1:0>2}.) {func:<10}', end='')

