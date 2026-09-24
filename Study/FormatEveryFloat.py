#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: FormatEveryFloat.py
# AUTHOR: Randall Nagy
# File: FormatEveryFloat.py
#

import math
for fval in 123.0, -123.0, math.pi:
    for code in 'efg':
        mask = '%' + code
        print(mask, mask % fval)
        umask = mask.upper()
        print('\t', umask, umask % fval)
