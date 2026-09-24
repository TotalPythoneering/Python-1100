#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ActFinal.py
# AUTHOR: Randall Nagy
# File: ActFinal.py
#

for ss, func in enumerate(\
    [f for f in dir(__builtins__) \
            if len(f) < 15 and f[0].islower()]):
	if not ss % 4:
	   print()
	print(f'{func.rjust(17)+"()"}', end='')
