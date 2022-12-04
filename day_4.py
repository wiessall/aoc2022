#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 10:07:51 2022

@author: tristan
"""
from typing import Generator
import re

def parse_newline_separated(path: str) -> Generator:
    with open(path) as f:
      for line in f.readlines():
          yield line.strip()
          
def count_fully_contained(reader: Generator) -> int:
    fully_contained_counter = 0
    for line in reader:
        indices = [int(idx) for idx in re.findall(r"[0-9]+", line)]
        if ((indices[0] >= indices[2]) and (indices[1] <= indices[3])) or\
        ((indices[2] >= indices[0]) and (indices[3] <= indices[1])):
            print(line)
            fully_contained_counter += 1
    return fully_contained_counter

def count_partially_contained(reader: Generator) -> int:
    partially_contained_counter = 0
    for line in reader:
        a,b,c,d = re.findall(r"[0-9]+", line)
        range_1, range_2 = set(range(int(a), int(b) + 1)), set(range(int(c), int(d) +1))
        if len(range_1.intersection(range_2)) >= 1:
            print(line)
            partially_contained_counter += 1
    return partially_contained_counter