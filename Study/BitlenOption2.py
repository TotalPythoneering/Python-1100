# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: BitlenOption2.py
# AUTHOR: Randall Nagy
#
MASK = "{:<5d}[{:<2d}] Bits"
last = None
for ss in range(0, 4097, 2):
    zlen = ss.bit_length()
    if zlen == last:
        continue
    last = zlen
    report = MASK.format(ss, zlen)
    print(report)
