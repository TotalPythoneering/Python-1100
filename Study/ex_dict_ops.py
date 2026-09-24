# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: ex_dict_ops.py
# AUTHOR: Randall Nagy
#
zDict = {"Code":None,
         "Tested":"All",
         7:"Seven",
         "Nine":9}

zDict["Code"] = "Ready!"
zDict.pop(7)
zDict.pop("Nine")
print(zDict)

zDict.clear()

zDict = dict("Code"="",
         "Tested"="All",
         7="Seven",
         "Nine"=9)
print(zDict)
