import random
import sys
import math
import time
import os

# List of all possible prize values
case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 250, 500, 1000, 5000, 10000,
  25000, 50000, 75000, 100000, 200000, 350000, 500000, 750000, 1000000]

# Base list of all possible case numbers
case_order = list(range(1, 23))

# Creates individual cases with prize values, numbers, and opening procedures
class Case:
  def __init__(self, value=0.01, number=0):
    self.value = value
    self.number = number
    self.iscase = False
    self.opened = False

  def __str__(self):
    if self.opened:
      return ("💼 ❌")
    elif self.iscase:
      return ("💼 🔒")
    else:
      return ("💼 " + str(self.number))

  # Changes status to reflect if case is chosen as stored case
  def assign_case(self):
    self.iscase = True
    case_order.remove(self.number)

  # Changes status of case and reveals case prize value
  def open(self):
    print(f"\nOpening case number {str(self.number)}...\n")
    time.sleep(3)
    print(self.__str__() + " = $" + "{:,}".format(self.value) + "\n")
    time.sleep(1)
    if self.value <= 25000 and not self.iscase:
      print("Nice!!!\n")
    elif self.value <= 200000 and not self.iscase:
      print("Well, it could be worse...\n")
    elif not self.iscase:
      print("Aw, darn! That hurts.\n")
    if not self.iscase:
      case_order.remove(self.number)
    case_values.remove(self.value)
    self.opened = True

def main():
  global case_values
  os.system("clear")
  print("\nWelcome to Deal or No Deal!")
  cases = create_cases()
  banker = 6
  print_cases(cases)

  # Prompt user to choose one case to store away
  while True:
    checker = False
    choice = (input("Choose your case to save for later! Case: ")).strip()
    try:
      for case in cases:
        if case.number == int(choice):
          case.assign_case()
          checker = True
    except:
      pass
    if checker:
      break
    else:
      print("\nPlease enter a valid case number!\n")

  print("\nCase locked in! Let's play.")
  time.sleep(2)
  os.system("clear")

  # Repeatedly have user open cases until one remains along with stored one
  while len(case_order) > 1:
    print("\nHere are the prizes still in play:\n")
    for item in sorted(case_values):
      print("$" + "{:,}".format(item))

    print("\nAnd here are the cases you can choose from:")
    print_cases(cases)

    while True:
      checker = False
      opened = (input("Which case would you like to open? Case: ")).strip()
      try:
        for case in cases:
          if case.number == int(opened) and case.number in case_order:
            case.open()
            checker = True
      except:
        pass
      if checker:
        break
      else:
        print("\nPlease enter a valid case number!\n")

    time.sleep(3)
    banker -= 1

    # After every 6 cases, initiates a banker call and option to choose a deal
    if banker == 0:
      print("INCOMING BANKER CALL!!!\n")
      time.sleep(2)
      print("...ring...")
      time.sleep(2)
      print("...ring...")
      time.sleep(2)
      bankerval = banker_value()
      print(f"\nThe banker offers $" + "{:,}".format(bankerval) + ".")

      while True:
        decision = input("\nDEAL OR NO DEAL? (D/ND): ")
        if decision.lower().strip() == "d" or decision.lower().strip() == "nd":
          break
        else:
          print("\nPlease enter the letter d or the letters nd!\n")
      if decision.lower().strip() == "d":
        print(f"\nCongrats!! You win $" + "{:,}".format(bankerval) + "!\n")
        time.sleep(2)
        print("Now let's see what you could have won in your case!")
        time.sleep(2)
        for stored in cases:
          if stored.iscase:
            stored.open()
            if stored.value < bankerval:
              print("Good choice, and congrats! Play again!\n")
              sys.exit()
            else:
              print("Aw, darn! Better luck next time! Play again!\n")
              sys.exit()
        sys.exit()
      else:
        print("\nNo deal! Continuing on...\n")
        time.sleep(3)
        banker = 6

    os.system("clear")

  # When down to last two cases, initiates final banker sequence
  print("\nHere are the prizes still in play:\n")
  for item in sorted(case_values):
    print("$" + "{:,}".format(item))
  print_cases(cases)
  print("Down to the last two cases! Time for one last banker offer.\n")
  time.sleep(2)
  print("INCOMING BANKER CALL!!!\n")
  time.sleep(2)
  print("...ring...")
  time.sleep(2)
  print("...ring...")
  time.sleep(2)
  bankerval = banker_value()
  print(f"\nThe banker offers $" + "{:,}".format(bankerval) + ".")

  while True:
    decision = input("\nDEAL OR NO DEAL? (D/ND): ")
    if decision.lower().strip() == "d" or decision.lower().strip() == "nd":
      break
    else:
      print("\nPlease enter the letter d or the letters nd!")
  if decision.lower().strip() == "d":
    print(f"\nCongrats!! You win $" + "{:,}".format(bankerval) + "!\n")
    time.sleep(2)
    print("Now let's see what you could have won in your case!")
    time.sleep(2)
    for stored in cases:
      if stored.iscase:
        stored.open()
        if case.value < bankerval:
          print("Good choice, and congrats! Play again!\n")
          sys.exit()
        else:
          print("Aw, darn! Better luck next time! Play again!\n")
          sys.exit()
    sys.exit()
  else:
    print("\nNo deal! Which case would you like to open?\n")
    for case in cases:
      if case.iscase:
        case_order.append(case.number)
    while True:
      decision = input(f"Case number {str(case_order[0])} or {str(case_order[1])} (your case)? Enter a number: ")
      for case in cases:
        if case.number == int(decision) and case.number in case_order:
          case.open()
          print(f"Congrats!! You win $" + "{:,}".format(case.value) + "!\n")
          sys.exit()
      print("\nPlease enter a valid case number!\n")

# Randomizes case numbers and values and stores them in a list for later use
def create_cases():
  global case_values
  global case_order
  random.shuffle(case_values)
  random.shuffle(case_order)
  cases = []
  for i in range(22):
    cases.append(Case(case_values[i], case_order[i]))
  return cases

# Prints a visual depiction using emojis of each case's status
def print_cases(cases):
  print()
  for i in range(11):
    print(cases[i].__str__() + " ", end="")
  print("\n")
  for i in range(11):
    print(cases[i+11].__str__() + " ", end="")
  print("\n")

# Calculates the root-mean-squared value of all in-play prize values
def banker_value():
  global case_values
  sum = 0
  for value in case_values:
    sum += value ** 2
  sum = sum / len(case_values)
  sum = round(math.sqrt(sum), 2)
  return sum

if __name__ == "__main__":
    main()