#===============#
# IMPORTS       #
#===============#
import os
import sys
import subprocess
# from psutil import *

from styling import *

#===============#
# MAIN          #
#===============#
def processlistener():
    ...


def taskkill(instance):
    with open(os.devnull, 'w') as dnull:
        print(info + 'Killing process '+instance+'...')
        subprocess.run(['taskkill', '/F', '/IM', instance], stdout=dnull, stderr=dnull)
        print(success + 'Killed process '+instance+' successfully!')