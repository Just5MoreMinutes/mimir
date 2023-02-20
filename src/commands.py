#===============#
# IMPORTS       #
#===============#
import sys
import os
from   subprocess import Popen

import json
import re
import time

from   styling    import *
from   utils.utils      import taskkill, timer

#===============#
# GLOBAL VARS   #
#===============#
PREFERENCES = {}

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

def pomodoro(t):

    S_PERIOD = int(t[0])
    B_PERIOD = int(t[1])

    print(type(S_PERIOD))
    print(type(B_PERIOD))

    print(info + 'Do you want to automatically block all distractions in your list while the timer is active? (y/n)')
    __confirm = input('├ ')

    __cwd = os.getcwd() + '\\batch'
    Sound = os.path.join(__cwd, 'play_sound.bat')

    if __confirm.lower() == 'y' or __confirm.lower() == 'yes':
        start(); timer(Sound, __cwd, S_PERIOD, B_PERIOD)
    else: timer(Sound, __cwd, S_PERIOD, B_PERIOD)


def commandhandler(inpt):

    indicator = ('!', '?')

    if not inpt or inpt == None:
        print(warn + 'Please enter a command!')
        return
        
    __inpt = inpt.split(' ')
    del inpt

    if __inpt[0][0] not in indicator:
        print(warn + 'Please use a valid command (prefix)! View the help panel for all commands (start argument -h).')
        return

    command = __inpt[0][1:]

    if len(__inpt) > 1:
        argument = __inpt[1]

    if command == 'a' or command == 'add':
        if '/' in argument:
            for i in argument.replace('/', ' ').split():
                add(i)
        else:
            add(argument)

    if command == 'r' or command == 'remove':
        if '/' in argument:
            for i in argument.replace('/', ' ').split():
                remove(i)
        else:
            remove(argument)

    if command == 'c' or command == 'clear':
        clear()

    if command == 's' or command == 'start':
        start()

    if command == 'p' or command == 'pomodoro':
        if '/' not in argument and '|' in argument:
            argument = argument.replace('|', ' ').split()
        else:
            argument = argument.replace('/', ' ').split()
            pomodoro(argument)

    if command == 'exit':
        sys.exit(2)

def help():
    ...

def settings():
    ...