# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyHashCode.py
# AUTHOR: Randall Nagy
# File: MyHashCode.py
#

# Since Python 3.2.3
#import os
#print(os.environ['PYTHONHASHSEED'])
#print(os.environ)

# Changes EACH RUN!
print("a".__hash__())
print(hash("a"))

# Work Around:
import zlib
zBytes = bytes("a","utf8") # more later!
print("Classic:",
      zlib.crc32(zBytes) )

# Work Around:
import hashlib
zBytes = bytes("a","utf8") # more later!
print("hashlib:",
      hashlib.md5(zBytes).hexdigest() )
