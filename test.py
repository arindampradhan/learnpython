
import os
import sys
import curses
import traceback
import atexit
import time

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


LINER = "-----------------------------------------------"
TITLE = "LEARN PYTHON"
PROBLEMS = os.listdir('./problems')



def create_list(PROBLEMS):
    names = [i.upper().replace('-',' ') for i in PROBLEMS]
    menu_list = []
    for name in names:
        obj = {}
        if name == 'HELP':
            obj = {name: "help"}
        else:
            obj = {name:"task(name)"}
        menu_list.append(obj)
    menu_list.append({'EXIT':exit})
    return menu_list

print create_list(PROBLEMS)