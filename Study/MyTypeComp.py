# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyTypeComp.py
# AUTHOR: Randall Nagy
# File: MyTypeComp.py
#

sNum = "20" # type-name encoding!

iNum = int(sNum) # int copy
if iNum == sNum:
    print("iNum == sNum")
else:
    print("iNum != sNum")

if str(iNum) == sNum:  # str copy
    print("str(iNum) == sNum")
else:
    print("str(iNum) != sNum")
