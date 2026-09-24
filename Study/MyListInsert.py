# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyListInsert.py
# AUTHOR: Randall Nagy
# File: MyListInsert.py
#

# Rational insertion
zList = ["is", "a"]
zList.insert(0, "This")
zList.insert(3, "TEST!")
print(zList)

# Irrational insertion
zList = ["a"]
zList.insert(98, "little")  # 'at ss or end'
zList.insert(90, "lamb!")
zList.insert(-99, "had")    # 'make it 0'
zList.insert(-100, "Mary")
print(zList)
