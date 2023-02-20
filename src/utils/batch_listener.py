'''
NOTE: While the opener.bat file *can* be altered, for the sake of stability, it shouldn't be.
'''

#===============#
# IMPORTS       #
#===============#
import os

#===============#
# GLOBAL VARS   #
#===============#
__fallback = int
PATH       = os.getcwd() + '\\batch\\opener.bat' # -> gets path to batch file on any (windows) system
JSON_PATH  = os.getcwd() + '\\preferences.json'  # -> gets path to preferences file on any (windows) system

#===============#
# MAIN          #
#===============#
#: openes batch file
with open(PATH, 'r') as rbf:
    lines = rbf.readlines()

    for line in lines:
        if line.startswith('set'):
            __fallback = lines.index(line)

lines[__fallback] = 'set directory=' + str(JSON_PATH) + '\n'

with open(PATH, 'w') as wbf:
    wbf.writelines(lines)