# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_array.py
# AUTHOR: Randall Nagy
#
import array
data = array.array('b')

print(data)

zbytes = b'123'
data.append(zbytes[0])
data.append(zbytes[1])
data.append(zbytes[2])

data.append(b'ABC'[0])

print(data)

data = array.array("b", b"Bizinga")
print(data)


data.append("Badinga")
