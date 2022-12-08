#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 07:58:18 2022

@author: tristan
"""
from typing import Generator
import numpy as np

def parse_newline_separated(path: str) -> Generator:
    with open(path) as f:
      for line in f.readlines():
          yield line.strip()
# stream = list(parse_newline_separated(path))[0]

def all_equal(stream: list, header_len: int) -> Generator:
    return (position for position, packet in enumerate(stream) if len(set(packet)) == header_len)

#%%
path = '/home/tristan/01_Coding_Club/advent_of_code/2022/input_6.csv'
def get_first_message_index(path: str, header_len=4) -> None:
    for line in parse_newline_separated(path):
        packets = np.lib.stride_tricks.sliding_window_view(list(line), header_len)
        print(next(all_equal(packets, header_len)) + header_len)
