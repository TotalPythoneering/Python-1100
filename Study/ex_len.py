# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_len.py
# AUTHOR: Randall Nagy
# File: ex_len.py
#

zstring = "123,456,789"
print(len(zstring))

print()

ss = 0
for ch in zstring:
    print(ss, "=", ch)
    ss += 1
