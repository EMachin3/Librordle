import time
import os
import enchant
import sys
from colorama import Fore
from colorama import Style
from colorama import Back
chosenWord = input("Type today's word.\n")
d = enchant.Dict("en_US")
realWord = False
while (not realWord):
    if (d.check(chosenWord)):
        realWord = True
    else:
        print("that's not a word")
        time.sleep(2.0)
        chosenWord = input("Type today's word.\n")
goodLength = False
while (not goodLength):
    if (len(chosenWord) == 5):
        print("Today's word has been chosen. The game will begin shortly.")
        goodLength = True
        time.sleep(2.0)
        os.system("cls")
    else:
        print("that's not the right length")
        time.sleep(2.0)
        chosenWord = input("Type today's word.\n")
correctLetter = [False, False, False, False, False]
correctLetterAndPosition = [False, False, False, False, False]
currentStatus = [None, None, None, None, None]
completionProgress = [None, None, None, None, None]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersAppearance = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
class Letters:
    name="default"
    color="black"
    def __init__(self, n):
        self.name = n
list=[]
with open('letters.txt', 'r') as file:
    for line in file:
        for letter in line.split():
            list.append ( Letters(letter) )
validWord = False
print("Welcome to...")
print(" _     _ _                       _ _      ")
print("| |   (_) |                     | | |     ")
print("| |    _| |__  _ __ ___  _ __ __| | | ___ ")
print("| |   | | '_ \\| '__/ _ \\| '__/ _` | |/ _ \\")
print("| |___| | |_) | | | (_) | | | (_| | |  __/")
print("\_____/_|_.__/|_|  \___/|_|  \__,_|_|\___|")
for bigLoop in range(6):
    while (not validWord):
        firstGuess = input("Enter guess number " + str(bigLoop + 1) + ".\n")
        if (d.check(firstGuess)):
            if (len(firstGuess) == 5):
                validWord = True
            else:
                print("that's not the right length")
        else:
            print("that's not a word")
    for i in range(5):
        currentStatus[i] = firstGuess[i]
    for i in range(5):
        if (chosenWord[i] == firstGuess[i]):
            correctLetter[i] = True
            correctLetterAndPosition[i] = True
        else:
            for j in range(5):
                if (j == i):
                    pass
                if (chosenWord[i] == firstGuess[j]):
                    correctLetter[j] = True
                else:
                    pass
    for k in range(5):
        if (correctLetterAndPosition[k] == True):
            completionProgress[k] = Back.GREEN + firstGuess[k] + Style.RESET_ALL + " "
        elif (correctLetter[k] == True and correctLetterAndPosition[k] == False):
            completionProgress[k] = Back.YELLOW + firstGuess[k] + Style.RESET_ALL + " "
        else:
            completionProgress[k] = Back.RED + firstGuess[k] + Style.RESET_ALL + " "
   
    for n in range(5):
        for o in range(26):
            if (letters[o] == firstGuess[n]):
                 if (correctLetterAndPosition[n] == True):
                     list[o].color = "green"
                 elif (correctLetter[n] == True and correctLetterAndPosition[k] == False and list[o].color!="green"):
                     list[o].color = "yellow"
                 elif (correctLetterAndPosition[n] == False and correctLetterAndPosition[k] == False and list[o].color!="green" and list[o].color!="yellow"):
                     list[o].color = "red"
                 else:
                     pass
    if (bigLoop == 0):
        print("Below is your progress with each letter. A red background means the letter is not in the word,\nA yellow background means the letter is in the word but in the wrong position,\nand a green background means the letter is in the right place.")
    for l in range(5):
        print(completionProgress[l], end='')
    print(Style.RESET_ALL)
    if (bigLoop != 0):
        print("Letter Bank:")
    if (bigLoop == 0):
        print("Here is every letter that you can guess. If the letter is not highlighted, you haven't guessed it yet.\nIf it is highlighted, the color indicates your progress.")
    for m in range(26):
          if (list[m].color=="green"):
              print(Back.GREEN + list[m].name + Style.RESET_ALL, end='')
          elif (list[m].color=="yellow"):
              print(Back.YELLOW + list[m].name + Style.RESET_ALL, end='')
          elif (list[m].color=="red"):
              print(Back.RED + list[m].name + Style.RESET_ALL, end='')
          else:
              print(list[m].name, end='')
          print(" ", end='')
    print(Style.RESET_ALL)
    if (correctLetter == [True, True, True, True, True]):
        print("Congratulations, you won!")
        time.sleep(20)
        sys.exit("Game over!")
    validWord = False
    correctLetter = [False, False, False, False, False]
    correctLetterAndPosition = [False, False, False, False, False]
    currentStatus = [None, None, None, None, None]
    completionProgress = [None, None, None, None, None]
print("You lose!")
time.sleep(20)
sys.exit("Game over!")
