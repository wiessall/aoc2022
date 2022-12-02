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


def play_round(_round: tuple) -> int:
    elve = _round[0]
    you  = _round[1]
    
    score = 0
    
    loose_dic = {'A': 'C', 'B': 'A', 'C': 'B'}
    win_dic   = {'A': 'B', 'B': 'C', 'C': 'A'}
    choice_values = {'A': 1, 'B': 2, 'C': 3}
    
    if you == 'X':
        score += 0
        you = loose_dic[elve]
    elif you == 'Y':
        score += 3
        you = elve
    elif you == 'Z':
        score += 6
        you = win_dic[elve]
    
    score += choice_values[you]
    
    return score

class play_rps():
    def __init__(self, path: str) -> list:
        game_strategy = []
        with open(path) as f:
          for line in f.readlines():
              game_strategy.append(parse_line(line))
        self.game_strategy = game_strategy
        
    def score_game(self) -> int:
        score_list = [score_round(_round) for _round in self.game_strategy]
        return sum(score_list)
    
    def score_plays(self) -> int:
        score_list = [play_round(_round) for _round in self.game_strategy]
        return sum(score_list)
#%%

    
    
    

    