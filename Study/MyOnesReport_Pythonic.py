# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyOnesReport_Pythonic.py
# AUTHOR: Randall Nagy
# File: MyOnesReport_Pythonic.py
#

zTuple = ("Mr. Ed", "Miss Daisy", "Mr. T", "Dr. Who")

# Pythonic Solution
for ss, ref in enumerate(zTuple, 1):
    print(ss, ".)", ref)
