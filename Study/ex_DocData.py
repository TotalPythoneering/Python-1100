#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_DocData.py
# AUTHOR: Randall Nagy
# File: ex_DocData.py
#

words = """
I wish I were a sailor,
upon yon gentle sea.

Where 'dems who do a COVID,
ARE FAR AWAY FROM WE!
"""

for word in words.split('\n'):
    if word.strip():
        print(f'{word}')
