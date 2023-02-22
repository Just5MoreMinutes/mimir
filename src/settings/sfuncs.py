#===============#
# IMPORTS       #
#===============#
import os

import json

from src.styling import *

#===============#
# MAIN          #
#===============#
def OUTPUT(yn) -> str or None:
    if yn in (on, off):
        pass
    else: return

    if yn == on:
        return
    
    if yn == off:
        ...