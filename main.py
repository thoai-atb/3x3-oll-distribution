from oll_case import OllCase
from oll_draw import *
from utils import get_directory

class UniqueCase:
  def __init__(self, case):
    self.case = case
    self.count = 1

def main():
  dir = get_directory()
  if len(dir) <= 0:
    print("Path was not selected.")
    return

  unique_cases = []

  population_count = 1000000 # reduce this number to run faster
  hundredth = population_count / 100

  for i in range(0, population_count):
    new_case = OllCase.random_case()
    existed = False
    for unique_case in unique_cases:
      if OllCase.is_equivalent(unique_case.case, new_case):
        unique_case.count += 1
        existed = True
        break
    if not existed:
      unique_cases.append(UniqueCase(new_case))
    if (i + 1) % hundredth == 0:
      print(f"{int((i + 1)/population_count * 100)}% completed")

  def get_count(unique_case):
    return unique_case.count

  unique_cases.sort(reverse=True, key=get_count)

  id = 0
  for unique_case in unique_cases:
    id += 1
    prob = unique_case.count / population_count * 100
    save_case(unique_case.case, f"{prob:.2f}% - {unique_case.count} / {population_count}", dir, f"Case #{id} - {prob:.2f}%" )
  
  print(f"Oll cases generated, {len(unique_cases)} unique cases in total.")
  
main()