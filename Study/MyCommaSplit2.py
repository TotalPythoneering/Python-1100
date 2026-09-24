# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyCommaSplit2.py
# AUTHOR: Randall Nagy
# File: MyCommaSplit2.py
#

data = []
data.append("John Doe, 1235 Fifth Ave., 813-318-9999")
data.append("Mr. Goober, 8712 Main Street, 415-514-9999")
data.append("Prof. Nagy, 105 Baker Street, 742-427-9999")
data.append("Doctor Quote, 666 Social Security Lane, 781-187-9999")

for ss, line in enumerate(data, 1):
    fields = line.split(',')
    if len(fields) != 3:
        print("Field Error!")
    else:
        print(str(ss) + ".) " + fields[2])
