from dataclasses import dataclass, field

@dataclass(order=True)
class Elve():
    sort_index: int = field(init=False, repr=False)
    number: int
    calories: int
    
    def __post_init__(self):
        self.sort_index = self.calories
#%%    
    

class GroupOfElves():
    def __init__(self, path: str):
        # Read csv
        # Generate one elve per entry
        self.parse_space_separated(path)
        self.all_elves = [Elve(number + 1, calory_entry) for number, calory_entry in enumerate(self.calory_list)]

    def find_most_caloric_elve(self) -> Elve:
        self.most_caloric_elve = sorted(self.all_elves)[-1]
        print(self.most_caloric_elve)
   
    def find_top_three_caloric_elves(self) -> list:
        self.top_three_caloric_elves = sorted(self.all_elves)[-3:]
        self.sum_top_three_calories = sum([i.calories for i in self.top_three_caloric_elves])
        print(self.top_three_caloric_elves, f"Top 3 sum: {self.sum_top_three_calories}")
        
    def parse_space_separated(self, path: str) -> list:
        calory_list = []
        elve_list   = []
        with open(path) as f:
          for line in f.readlines():
              line = line.strip()
              if line != "":      
                  elve_list.append(int(line))
              else:
                  calory_list.append(sum(elve_list))
                  elve_list = []
        self.calory_list = calory_list      
#%%
score_game("/home/tristan/01_Coding_Club/advent_of_code/2022/test_2.csv")
    
