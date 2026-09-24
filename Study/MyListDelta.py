# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyListDelta.py
# AUTHOR: Randall Nagy
# File: MyListDelta.py
#

zList = ["Fred", "Ralph", "Zelda", "Zoe"]

# Lists are mutable
print(type(zList))
for ss in range(len(zList)):
    zList[ss] = "Guest " + zList[ss]
    print(zList[ss])

# TypeError: 'tuple' object does not support item assignment
zTuple = ("Fred", "Ralph", "Zelda", "Zoe")
print(type(zTuple))
for ss in range(len(zTuple)):
    zTuple[ss] = "Guest " + zTuple[ss]
    print(zTuple[ss])
