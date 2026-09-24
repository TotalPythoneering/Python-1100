#!/usr/bin/env python3
# MISSION: The complete set of examples and source code for ''Python 1100 - Python
# for Beginners.''
# STATUS: Public Release
# VERSION: 0.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Python-1100
# DATE: 2020-12-19 06:09:38
# FILE: MyBanner2Test.py
# AUTHOR: Randall Nagy
#

# Change tab to spaces:
def ShowChars(num, token):
    return (token * (num + 4))
            
def Show(message):
    xx = len(message)
    stars = ''
    if xx > 5:
        stars = ShowChars(xx, '$')
    else: 
        stars = ShowChars(xx, '*')
    print(stars)
    print("* " + message + " *")
    print(stars)

def test_show():
    '''>>> Show("The is a MESSAGE")
$$$$$$$$$$$$$$$$$$$$
* The is a MESSAGE *
$$$$$$$$$$$$$$$$$$$$
>>> Show("Doh!")
********
* Doh! *
********
    '''
    return True

from doctest import testmod

testmod()
