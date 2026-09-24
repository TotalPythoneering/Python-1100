# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyFirstDictionary.py
# AUTHOR: Randall Nagy
# File: MyFirstDictionary.py
#

zList = {1:"Mr. Ed", 2:"Miss Daisy", 3:"Mr. T", 4:"Dr. Who"}
print(type(zList))
for ss, entry in enumerate(zList):
    print(ss, ".)", entry.__hash__())
