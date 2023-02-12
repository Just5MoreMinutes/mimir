#===============#
# IMPORTS       #
#===============#
import sys
import os

import json
import re

from styling import *
from utils import taskkill


#===============#
# GLOB VARIABLES#
#===============#


#===============#
# MAIN          #
#===============#
def add(arg): 
    print(info + 'Trying to add \'' + arg + '\' to '+bold+'blocked.json'+reset+'!')

        #: load json file
    if os.path.getsize('blocked.json') == 0:
        blocked_list = []
        pass

    else:
        with open('blocked.json', 'r', encoding='utf-8') as ljf:
            _ljf = json.load(ljf)
            blocked_list = _ljf.copy()

            if arg in _ljf:
                print(err + '\'' + arg + '\' already added to ' + bold + 'blocked.json'+reset+'! Aborting...')
                return

    #: check if there a multiple applications to be added
    if type(arg) == list and len(arg) > 1:
        blocked_list.append([i for i in blocked_list])

    #: add application to list
    blocked_list.append(arg)

    with open('blocked.json', 'w') as djf:
        json.dump(blocked_list, djf)
        print(info + 'Added \'' + arg + '\' to '+bold+'blocked.json'+reset+'!')

def remove(arg):
    print(info + 'Trying to remove \'' + arg + '\' from '+bold+'blocked.json'+reset+'!')

    with open('blocked.json', 'r', encoding='utf-8') as lrjf:
        _lrjf = json.load(lrjf)

        if arg not in _lrjf:
            print(err + 'Application not in '+bold+'blocked.json'+reset+'!')
            return
        
        else:
            _lrjf.remove(arg)
            blocked_list = _lrjf.copy()

    with open('blocked.json', 'w') as rjf:
        json.dump(blocked_list, rjf)
    
    print(info + 'Removed \'' + arg + '\' from '+bold+'blocked.json'+reset+'!')

def clear():
    print(warn + 'Do you really want to clear the following list of apps? (y/n)')

    with open('blocked.json', 'r', encoding='utf-8') as cjf:
        _cjf = json.load(cjf)
        print('│  '+str(_cjf))
    
    __confirm = input('├ ')
    if __confirm.lower() in ('y', 'yes'):
        __clear = open('blocked.json', 'w')
        __clear.write('')
        print(info + bold + 'blocked.json'+reset+' cleared. Use \'!add\' or \'?add\' to add new applications!')
    
    elif __confirm.lower() in ('n', 'no'):
        print(info + bold +'blocked.json'+reset+' not cleared! Continuing...')
        return

def start():

    __fallback = []

    print(warn + 'Any and all instances of the added programs will be closed.\n│  Make sure you have provided the full program name.\n│  If faulty names are given, some critical processes may be shut down.\n│  Do you want to continue? (y/n)')
    __confirm = input('├ ')
    if __confirm.lower() in ('y', 'yes'):
        print(info + 'Starting...')
        pass

    elif __confirm.lower() in ('n', 'no'):
        print(info + 'Process will not be started. Continuing...')
        return
    
    del __confirm

    with open('blocked.json', 'r') as sjf:
        _sjf = json.load(sjf)
        blocked_list = _sjf.copy()

    #: find all instances with given name
    output = os.popen('wmic process get description, processid').read()
    __output = output.split('\n')
    __d = lambda arg: re.findall(r'\s+(\d+)', arg)

    for instance in __output:
        for app in blocked_list:
            if app in instance.lower():
                tmp_index = __output.index(instance)
                __output[tmp_index] = rgb(255, 0, 0) + __output[tmp_index] + reset
                match = __d(instance)
                if match:
                    __fallback.append(instance.replace(match[0], '').replace(' ', ''))

    for running_instances in __output:
        print('│ ' + running_instances)

    tmp = []
    for item in __fallback:
        if item not in tmp:
            tmp.append(item)
        __fallback = tmp

    del (__output, __d, output, blocked_list, 
        sjf, _sjf, instance, running_instances, 
        tmp_index, match, app, tmp, item)

    while True:
        for instance in __fallback:
            taskkill(instance=instance)


def commandhandler(inpt):
    
    if inpt == '' or inpt == None:
        print(warn + 'Please enter a command!')

    __inpt = inpt.split(' ')
    del inpt

    #: check if command indicator is given
    if __inpt[0][0] == '!' or __inpt[0][0] == '?': 

        #: check remaining characters of list item
        if __inpt[0][1:] == 'a' or __inpt[0][1:] == 'add':

            if '/' in __inpt[1]:
                separated = __inpt[1].replace('/', ' ').split()
                for i in separated:
                    add(i)

            else:
                add(__inpt[1])

        #: check remaining characters of list item
        if __inpt[0][1:] == 'r' or __inpt[0][1:] == 'remove':
            
            if '/' in __inpt[1]:
                separated = __inpt[1].replace('/', ' ').split()
                for i in separated:
                    remove(i)
                
            else:
                remove(__inpt[1])
        
        #: check remaining characters of list item
        if __inpt[0][1:] == 'c' or __inpt[0][1:] == 'clear':
            clear()

        #: check remaining characters of list item
        if __inpt[0][1:] == 's' or __inpt[0][1:] == 'start':
            start()

        #: check remaining characters of list item
        if __inpt[0][1:] == 'exit':
            sys.exit(2)

    else:
        print(warn + 'Please use a valid command (prefix)! View the help panel for all commands (start argument -h).')
        del __inpt