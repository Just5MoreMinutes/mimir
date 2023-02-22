'''
NOTE: While the opener.bat file *can* be altered, for the sake of stability, it shouldn't be.
'''

#===============#
# IMPORTS       #
#===============#
import os

#===============#
# MAIN          #
#===============#
def batch_edit(PATH, *DUMP_PATH):

    __fallback = int
    _PATH = os.getcwd() + '\\batch\\' + PATH
    _DUMP = os.getcwd() + '\\' + DUMP_PATH

    #: openes batch file
    with open(_PATH, 'r') as rbf:
        lines = rbf.readlines()

        for line in lines:
            if line.startswith('set'):
                __fallback = lines.index(line)

    lines[__fallback] = 'set directory=' + str(_DUMP) + '\n'

    with open(_PATH, 'w') as wbf:
        wbf.writelines(lines)