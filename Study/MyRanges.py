# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyRanges.py
# AUTHOR: Randall Nagy
# File: MyRanges.py
#
print("Type 1 - range(5)")
zrange = range(5)
print(zrange)
print(type(zrange))
for zint in zrange:
    print(zint)
print("Type 2 - range(1, 5)")
zrange = range(1, 5)
for zint in zrange:
    print(zint)
print("Type 3 - range(1, 5, 2)")
zrange = range(1, 5, 2)
for zint in zrange:
    print(zint)
