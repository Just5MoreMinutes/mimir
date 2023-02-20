#===============#
# IMPORTS       #
#===============#
import sys
sys.dont_write_bytecode = True # -> evade creation of pycache
import os

import getopt
import json

from   styling           import *
from   commands          import commandhandler
from   settings.settings import settings_handler

#===============#
# MAIN          #
#===============#
def start(argv):
    
    #: check if user requested help
    if '-h' in argv or '--help' in argv:

        print(info + 'HELP PAGE')

    #: check if user opened settings
    elif '-s' in argv or '--settings' in argv:

        print(info + 'SETTINGS')
        settings_handler()

    else:
        while True:
            try:
                command_input = input('├ ')
                commandhandler(command_input)
            except Exception as ex:
                __err_msg_tmp = err + 'An error occured:\n│  TYPE: {0}\n│  ARGS: {1!r}'
                __err_msg = __err_msg_tmp.format(type(ex).__name__, ex.args)
                print(__err_msg)

    try:
        return command_input
    except UnboundLocalError:
        pass


#: start
if __name__ == '__main__':
    start(sys.argv[1:])