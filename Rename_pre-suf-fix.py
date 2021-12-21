#!/usr/bin/env python
# coding: utf-8


import os,sys



old_name_prefix = input('The prefix would be changed from: ')
new_name_prefix = input('The prefix would be changed into: ')
old_name_suffix = input('The suffix would be changed from: ')
new_name_suffix = input('The suffix would be changed into: ')
old_names = os.listdir('./')


for name in old_names:
    if not ('.ipynb' in name) and not('.py' in name) == True:
        new_name = name
        if old_name_prefix != new_name_prefix:
            if name[:len(old_name_prefix)] == old_name_prefix:
                new_name = new_name_prefix + new_name[len(old_name_prefix):]
                os.rename(name , new_name)
                print(name)
            new_new_name = new_name
        if old_name_suffix != new_name_suffix:
            if new_name[len(name)-len(old_name_suffix):] == old_name_suffix:
                new_new_name = new_name[:len(new_name)-len(old_name_suffix)] + new_name_suffix
                os.rename(new_name , new_new_name)
                print(name)




