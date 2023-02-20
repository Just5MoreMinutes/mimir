#===============#
# IMPORTS       #
#===============#
import os
import sys
import subprocess
from   subprocess import Popen

import time

from   styling    import *

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

def timer(__file, __cwd, __sp, __bp):
    while True:
        time.sleep(__sp) # -> studying period
        play_sound = Popen(__file, cwd=__cwd)
        stdout, stderr = play_sound.communicate()
        time.sleep(__bp) # -> break period
        stdout, stderr = play_sound.communicate()

def test(x):
    print(x)