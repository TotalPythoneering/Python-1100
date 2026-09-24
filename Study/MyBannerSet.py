#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyBannerSet.py
# AUTHOR: Randall Nagy
#

prefix = set()
prefix.add("Pig")
prefix.add("Cat")
prefix.add("Pig")
prefix.add("Dog")

for dat in prefix:
    print(dat)
        

prefix2 = set(("pig", "Mouse", "Pig", "Dog"))

print(prefix2.intersection(prefix))

print(prefix2.union(prefix))

prefix = frozenset()
prefix.add("Pig")
