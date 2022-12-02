# -*- coding: utf-8 -*- 
#%%
import struct
def parse_line(line: str) -> tuple:
    fieldwidths = (1, 1, 1)
    fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)
    
    # Convert Unicode input to bytes and the result back to Unicode string.
    unpack = struct.Struct(fmtstring).unpack_from  # Alias.
    parse = lambda line: tuple(s.decode() for s in unpack(line.encode()))

    fields = parse(line)
    
    return fields[::2]

def score_round(_round: tuple) -> int:
    elve = _round[0]
    you  = _round[1]
    
    score = 0
    win_dic = {"AB" : 6, "AC" : 0, "BA" : 0, "BC" : 6, "CA" : 6, "CB" : 0,
               "AA" : 3, "BB" : 3, "CC" : 3}

    if you == 'X':
        score += 1
        you = 'A'
    elif you == 'Y':
        score += 2
        you = 'B'
    elif you == 'Z':
        score += 3
        you = 'C'
    
    score += win_dic[elve + you]
    return score

def score_game(path: str) -> int:
    score_list = []
    with open(path) as f:
      for line in f.readlines():
          _round = parse_line(line)
          print(score_round(_round))
          score_list.append(score_round(_round))
    return sum(score_list)
#%%

    