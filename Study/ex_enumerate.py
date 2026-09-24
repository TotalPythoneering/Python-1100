# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_enumerate.py
# AUTHOR: Randall Nagy
# File: ex_enumerate.py
#

# Pythonic Construct

for ss, ref in enumerate("nagy"):
    print(ss, ".)", ref)

print()

for ss, ref in enumerate("nagy", 9000):
    print(ss, ".)", ref)
