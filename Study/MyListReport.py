#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyListReport.py
# AUTHOR: Randall Nagy
#

def list_report(info, a_list):
    nelem = len(a_list)
    message = info + " has " + \
              str(nelem) + " items"
    banner = '*' * len(message)
    print(banner)
    print(message)
    print(banner)
    return nelem

list_report("BUILTINS", dir(__builtins__))

    
