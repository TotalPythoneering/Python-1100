#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: FormatFloatCaveats.py
# AUTHOR: Randall Nagy
# File: FormatEveryFloat.py
#

import math
def report(expr):
    print(expr, eval(expr), sep='\n>>> ')


report("'[%10f]' % 123.456")
report("'[%-10f]' % 123.456")
report("'[%0.10f]' % 123.456")

import decimal
zd = decimal.Decimal(123.456)
zd.is_finite()
zd = decimal.Decimal(math.pi)
zd.is_finite()
          
