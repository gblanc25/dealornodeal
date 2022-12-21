import random
import re
from project import Case
import math

case_values = [100, 500, 1000]
case_order = [1, 2, 3]

# Modified test version of create_cases, for ease of testing
def create_cases():
  global case_values
  global case_order
  random.shuffle(case_values)
  random.shuffle(case_order)
  cases = []
  for i in range(3):
    cases.append(Case(case_values[i], case_order[i]))
  return cases

def test_create_cases():
  cases = create_cases()
  assert (len(cases) == 3)
  assert (0 < cases[0].number < 4)
  assert (0 < cases[1].number < 4)
  assert (0 < cases[2].number < 4)

# Modified test version of print_cases, for ease of testing
def print_cases(cases):
  str = ""
  for i in range(3):
    str = str + cases[i].__str__() + " "
  return str

def test_print_cases():
  cases = create_cases()
  result = print_cases(cases)
  matches = re.search("💼 [1-3] 💼 [1-3] 💼 [1-3]", result)
  assert matches

# Modified test version of banker_value, for ease of testing
def banker_value(case_values):
  sum = 0
  for value in case_values:
    sum += value ** 2
  sum = sum / len(case_values)
  sum = round(math.sqrt(sum), 2)
  return sum

def test_banker_value():
  assert banker_value([100, 500, 1000]) == 648.07
  assert banker_value([0, 1, 3, 4, 5]) == 3.19
  assert banker_value([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 5.63




