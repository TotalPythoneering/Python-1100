# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyListDelete.py
# AUTHOR: Randall Nagy
# File: MyListDelete.py
#

# OKAY! Rational item removal
zList = ["This", "is", "a", "Test"]
zPop = zList.pop(0)
print("Popped:", zPop)
print("Result:", zList)

# ERROR! Irrational removal
zList = ['Mary', 'had', 'a', 'little', 'lamb!']
zList.pop(-100) # IndexError: pop index out of range
zList.pop(99)   # IndexError: pop index out of range
print(zList)
