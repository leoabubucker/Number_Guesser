"""
To-do:
"""

import random

def toARandomPower(number):
   global power 
   power = random.randint(1,5)
   return number ** power

def dividedByARandomNumber(number):
  global divisor
  divisor= random.randint(1,100)
  remainder = number % divisor
  if remainder == 0:
    print("A given number to the power of " + str(power) + " is " + str(number) + " and is divisible by " + str(divisor) + " with no remainder")
    return toARandomPower(number)   
  else:
    print("A given number to the power of " + str(power) + " is " + str(number) + " and is divisible by " + str(divisor) + " with a remainder of " + str(remainder))
    return remainder
  runProgram()

def runProgram():
  global number 
  number = random.randint(1, 10)
  dividedByARandomNumber(toARandomPower(number))

  global userNumber
  userNumber = input("Enter your guess here: ")
  checkNumber()

def checkNumber():  
  if userNumber == "" or userNumber.isspace():
    print("Please enter a number!")
    runProgram()
  elif userNumber.isalpha():
    print("Please do not use any letters in your guess, numbers only!")
    runProgram()
  elif not userNumber.isdigit():
      print("Please do not use any symbols in your guess, numbers only!")
      runProgram()
  elif userNumber.isnumeric():
    programResults()
  else:
    print("Unknown error detected! Restarting program now.")
    runProgram()

    

def programResults():
  yesStringList = ["y", "Y", "yes", "Yes", "YES"]
  noStringList = ["n", "no", "NO", "N", "No"]
  if userNumber == str(number):
    print("Congratulations! You guessed the number, " + str(number) + ", correctly!")
    playAgain = input("Play Again? Type Y or N")
    yesFilter = [y for y in yesStringList if y == playAgain]
    noFilter = [n for n in noStringList if n == playAgain]
    if yesFilter != []:
      runProgram()
    elif noFilter != []:
      print("Exiting Game: ")
    else:
        print("Unknown value detected! Please stick to Y or N")
        programResults()
        
  else:
    print("Incorrect Guess. You guessed " + userNumber + " The correct number was " + str(number))
    userDecision = input("Do you want to try again? Type Y or N.")
    yesFilter2= [y for y in yesStringList if y == userDecision]
    noFilter2 = [n for n in noStringList if n == userDecision]
    if yesFilter2 != []:
      runProgram()
    elif noFilter2 != []:
      print("Exiting Game: ")
    else:
        print("Unknown value detected! Please stick to Y or N")
        programResults()

runProgram()


