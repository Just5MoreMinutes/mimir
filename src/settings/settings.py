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
ON  = on
OFF = off

PREFERENCES = {
#   setting : default
    'OUTPUT': ON,
    'TRAY'  : ON,
}

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
    return

def modify() -> dict:
    print(info + '''You are trying to modify the current settings.
│ Please note that this could alter how the program currently works.
│ If you are unsure or need to troubleshoot the program please visit one of the following sources:
│  - integrated help page: pass the starting arguments -h or --help
│  - GitHub: https://github.com/Just5MoreMinutes/mimir
│  - Website: mimir.just5moreminutes.dev (WIP!)
│ Thank you!
│ 
│ Please enter the setting you wish to modify:''')
    __modfiys = input('├ ')

    alter = __modfiys.split(':')
    if alter[0] in PREFERENCES.keys():
        pass
    else: return

    for i in PREFERENCES.keys():
        if i == alter[0] and PREFERENCES[i] != alter[1]:
            PREFERENCES[i] = alter[1]
        else: return

    print(info + 'Setting' + str(alter[0]) + ' successfully changed to '+ str(alter[1]) + '.')
    return PREFERENCES

def reset(pref):
    print(info + '''You are trying to reset the settings to factory default.
│ Please note that this could alter how the program currently works.
│ If you are unsure or need to troubleshoot the program please visit one of the following sources:
│  - integrated help page: pass the starting arguments -h or --help
│  - GitHub: https://github.com/Just5MoreMinutes/mimir
│  - Website: mimir.just5moreminutes.dev (WIP!)
│ Thank you!''')
    _default = {
     #   setting : default
        'OUTPUT': ON,
        'TRAY'  : ON,
    }
    pref = _default

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
        reset(PREFERENCES)
    
    if __selection.lower() == 'e':
        sys.exit(2)