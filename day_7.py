#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 18:22:51 2022

@author: tristan
"""
from dataclasses import dataclass, field
import collections
from typing import Generator


@dataclass(order=False)
class File():
    size: int
    name: str
    is_folder: bool = False


class Folder(collections.defaultdict):
    def __init__(self, name: str) -> None:
        self.is_folder = True
        self.name = name
        super(Folder, self).__init__(list) 
    def get_size(self) -> None:
        self.sizes = [int(item.size) if not item.is_folder else item.get_size() for item in self.values()]
        # self.size = sum()
    def get_children(self) -> None:
        self.children = [item.name if not item.is_folder else (item.name, item.get_children) for item in self.values()] 
#%%
def parse_newline_separated(path: str) -> Generator:
    with open(path) as f:
        content = []
        for line in f.readlines():
            content.append(line.strip().split(' '))
        return content
    
path = '/home/tristan/01_Coding_Club/advent_of_code/2022/test_7.csv'

commands = parse_newline_separated(path)
parent_counter = 0
visited_directories = []
all_folders = Folder('/')

for i, line in enumerate(commands):
    # print(line)
    #cd command
    if (len(line) == 3):
        if line[-1] == "..":
            parent_counter += 1
            current_dir = visited_directories[-(1 + parent_counter)]
        else:
            current_dir = line[-1]
            # print(current_dir)
            parent_counter = 0
            visited_directories.append(current_dir)
            if current_dir not in all_folders.keys():
                all_folders[current_dir] = Folder(current_dir)
            
            if commands[i + 1][1] == 'ls':
                j = i + 2
                while (j < len(commands)) and (commands[j][0] != '$'):
                    line = commands[j]
                    if line[0] != "dir":
                        all_folders[current_dir][line[1]] = File(size=line[0], name=line[1])
                        
                    elif line[0] == 'dir':
                        all_folders[current_dir][line[1]] = Folder(name=line[1])
                        pass
    
                    j += 1
all_folders
# all_folders.get_size()
#%%
def stitch(top_level, all_f, keys): 
    keys_b = top_level.keys() = keys[0]                 
    if isinstance(all_f[key], Folder):
        keys.remove(key)
        stitch(top_level, all_f[key], keys)
    else:
        all_f[keys] = top_level[key]
#%%        
a = all_folders
tks = a.keys()
a
def stitch(tks, a):
    for key in tks:
        if key in a.keys():
            if (tlfs := set(a[key].keys()).intersection(tks)):
                print(f"stepping into {key}")
    
                for tlf in tlfs:
                    a[key][tlf]  = a.pop(tlf)
                    a['/']
                    print('')
                if a[key].is_folder:
                    stitch(a[key].keys(), a[key])
    return a
a            
#%%
def get_size(a):
    c = []
    for item in a.values():
        if item.is_folder == False:
            c.append(item.size)
        else:
            get_size(item)
    return(sum(c))
get_size(a)