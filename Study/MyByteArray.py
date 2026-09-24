# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyByteArray.py
# AUTHOR: Randall Nagy
# File: MyByteArray.py
#

zChars = "TheTest"
print("ascii", bytes(zChars, "ascii"))
print("utf8", bytes(zChars, "utf8"))
print("utf16", bytes(zChars, "utf16"))
print("utf32", bytes(zChars, "utf32"))
