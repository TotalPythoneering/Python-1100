#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MySetVenn2.py
# AUTHOR: Randall Nagy
#
cat = {'c','a','t'}
car = set()
car.add('c');car.add('a');car.add('r')

print(type(cat))
print("Normalized cat:", cat)
print("Normalized car:", car)

# set() = unique set, 'venn style
print("cat | car:", cat | car) # union
print("cat & car:", cat & car) # intersect
print("cat - car:", cat - car) # 'remove common car from cat'
print("cat ^ car:", cat ^ car) # order dif

print(type(cat - car))
