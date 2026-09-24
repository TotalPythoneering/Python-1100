# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyTupleLoop.py
# AUTHOR: Randall Nagy
# File: MyTupleLoop.py
#

zList = ("Fred", 21, "Zelda", "Zoe", 54, 33)

print(type(zList))
for entry in zList:
    print(entry, "is", type(entry))


# TypeError: 'tuple' object does not support item assignment
zTuple = ("Fred", "Ralph", "Zelda", "Zoe")
print(type(zTuple))
for ss in range(len(zTuple)):
    zTuple[ss] = "Guest " + zTuple[ss]
    print(zTuple[ss])
