#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 09:42:17 2022

@author: tristan
"""
#%%
set(first_compartment).intersection(second_compartment)
#%%
def char_to_int(char: str) -> int:
    
    if char.isupper():
        return (ord(char) - 64) + 26
    else:
        return (ord(char) - 96)
#%%
from dataclasses import dataclass, field

@dataclass(order=False)
class Rucksack():
    
    content: str
    compartment_one: str = field(init=False, repr=False)
    compartment_two: str = field(init=False, repr=False)
    wrong_item: str = field(init=False)
    
    def __post_init__(self):
        self.half_len        = len(self.content) // 2
        self.compartment_one = self.content[:self.half_len]
        self.compartment_two = self.content[self.half_len:]
        self.wrong_item      = ''.join(set(self.compartment_one).intersection(self.compartment_two))
        
class AllRuckSacks():
    def __init__(self, path: str):
        self.parse_newline_separated(path)
        self.rucksack_list = [Rucksack(content=content) for content in self.content_list]
        self.priority_sum = sum([char_to_int(rucksack.wrong_item) for rucksack in self.rucksack_list])
        self.badge_to_groups()
        self.group_badge_sum = sum([char_to_int(badge) for badge in self.group_badges])
        
    def parse_newline_separated(self, path) -> list:
        content_list = []
        with open(path) as f:
          for line in f.readlines():
              content_list.append(line.strip())
        self.content_list = content_list
        
    def split_into_groups(self, to_split: list, groupsize: int) -> list:
        for chunk in range(0, len(to_split), groupsize):
            yield to_split[chunk:chunk + groupsize]
    
    def badge_to_groups(self, groupsize=3) -> list:
        rucksack_groups = self.split_into_groups(self.content_list, groupsize=groupsize)
        # https://stackoverflow.com/questions/3852780/python-intersection-of-multiple-lists
        self.group_badges = [''.join(set.intersection(*map(set,group))) for group in rucksack_groups]
            
        
        
        
    
        