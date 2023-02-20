#===============#
# IMPORTS       #
#===============#
import sys
import os

import json

from   src.styling import *

#===============#
# GLOBAL VARS   #
#===============#
JSON_PATH   = os.getcwd() + r'\preferences.json'
D_JSON_FILE = lambda preferences: json.dump(preferences)
L_JSON_FILE = lambda preferences: json.load(preferences)

#===============#
# MAIN          #
#===============#
def dsettings(pref) -> D_JSON_FILE and str:
    D_JSON_FILE(pref, open(JSON_PATH, 'w'))

def lsettings(ret: bool) -> L_JSON_FILE and str:
    L_JSON_FILE(open(JSON_PATH, 'r'))
    if ret == True:
        return str(L_JSON_FILE(open(JSON_PATH, 'r')))

def display():
    print('│ ' + lsettings(True))

def modify(): ...

def reset(): ...

def settings_handler():
    print(info + 'Please select what you want to do:\n│ [d] - Display current preferences\n│ [m] - Modify preferences\n│ [r] - Reset preferences\n│ [e] Exit\n│ ')
    __selection = input('├ ')

    if __selection.lower() in ('d', 'm', 'r', 'e'):
        pass
    else: return

    if __selection.lower() == 'd':
        display()

    if __selection.lower() == 'm':
        modify()
    
    if __selection.lower() == 'r':
        reset()
    
    if __selection.lower() == 'e':
        sys.exit(2)