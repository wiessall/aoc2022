#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:48:52 2022

@author: tristan
"""
path =  '/home/tristan/01_Coding_Club/advent_of_code/2022/test_5.csv'
a = []

for line in open(path):
    elements = line.split(' ')
    positions = np.where(regex==elements)
    letters = regex(line)
    container_dic[positions[i]].append(letters[i])
    
    if line.split(" ")[0] == "move":
         re.findall(r"[0-9]+", line)
            
        # print(re.findall(r"[A-Z]", line))
#%%
containers = a[:3]

for line in containers[0]:
    for char in line:
        print(char)
#%%

from collections import defaultdict, OrderedDict
import re

class Container():
    def __init__(self, path: str) -> None:
        self.parse_containers(path)
        
    def parse_containers(self, path: str) -> None:
        container_dic = defaultdict(list)
        instruction_list = []
        p = re.compile("[A-Z]")
        for line in open(path):
            for m in p.finditer(line):
                container_dic[m.start()].insert(0, m.group())
            if line.split(" ")[0] == "move":
                 instruction_list.append(tuple(re.findall(r"[0-9]+", line)))
            elif (len(line.split(" ")) > 1):
                if (line.split(" ")[1].isdigit()):
                    keys = list(map(int, re.findall(r"[0-9]", line)))
        
        container_dic = OrderedDict(sorted(container_dic.items()))
        self.container_dic = dict(zip(keys, list(container_dic.values())))
        self.instruction_list = instruction_list
        
    def move_containers(self) -> str:
        for instruction in self.instruction_list:
            amount, origin, target = map(int, instruction)
            for i in range(1, amount + 1):
                self.container_dic[target].append(self.container_dic[origin].pop(-1))
        self.top_row = ''.join([column[-1] for column in self.container_dic.values()])
    
    def move_containers_9001(self) -> str:
        for instruction in self.instruction_list:
            amount, origin, target = map(int, instruction)
            print(self.container_dic)
            self.container_dic[target].extend(self.container_dic[origin][-amount:])
            self.container_dic[origin] = self.container_dic[origin][:-amount]
        self.top_row = ''.join([column[-1] for column in self.container_dic.values()])
            
        

        