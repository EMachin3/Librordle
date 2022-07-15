import time
import os
import enchant
import sys
from colorama import Fore
from colorama import Style
from colorama import Back
chosenWord = input("Type today's word.\n")
#print(chosenWord)
d = enchant.Dict("en_US")
realWord = False
while (not realWord):
    if (d.check(chosenWord)):
        #print("that's a word")
        #time.sleep(1.0)
        realWord = True
    else:
        print("that's not a word")
        time.sleep(2.0)
        chosenWord = input("Type today's word.\n")
        #sys.exit("choose a real word")
goodLength = False
while (not goodLength):
    if (len(chosenWord) == 5):
        #print("okay that word works")
        print("Today's word has been chosen. The game will begin shortly.")
        goodLength = True
        time.sleep(2.0)
        os.system("cls")
    else:
        print("that's not the right length")
        time.sleep(2.0)
        chosenWord = input("Type today's word.\n")
        #sys.exit("choose a word that's the correct length")
#firstGuess = input("Enter your first guess.\n")
#letter1 = chosenWord[0]
#letter2 = chosenWord[1]
#letter3 = chosenWord[2]
#letter4 = chosenWord[3]
#letter5 = chosenWord[4]
correctLetter = [False, False, False, False, False]
correctLetterAndPosition = [False, False, False, False, False]
currentStatus = [None, None, None, None, None]
completionProgress = [None, None, None, None, None]
#logicProgress = [None, None, None, None, None]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersAppearance = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
class Letters:
    name="default"
    color="black"
    def __init__(self, n):
        self.name = n
list=[]
list.append( Letters("a") )
list.append( Letters("b") )
list.append( Letters("c") )
list.append( Letters("d") )
list.append( Letters("e") )
list.append( Letters("f") )
list.append( Letters("g") )
list.append( Letters("h") )
list.append( Letters("i") )
list.append( Letters("j") )
list.append( Letters("k") )
list.append( Letters("l") )
list.append( Letters("m") )
list.append( Letters("n") )
list.append( Letters("o") )
list.append( Letters("p") )
list.append( Letters("q") )
list.append( Letters("r") )
list.append( Letters("s") )
list.append( Letters("t") )
list.append( Letters("u") )
list.append( Letters("v") )
list.append( Letters("w") )
list.append( Letters("x") )
list.append( Letters("y") )
list.append( Letters("z") )
#print(letter1 + letter2 + letter3 + letter4 +letter5)
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
            #print("that's a word")
            #time.sleep(1.0)
            if (len(firstGuess) == 5):
                #print("okay that word works")
                validWord = True
            else:
                print("that's not the right length")
                #time.sleep(2.0)
        else:
            print("that's not a word")
            #time.sleep(2.0)
            #sys.exit("choose a real word")
    for i in range(5):
        currentStatus[i] = firstGuess[i]
    #print(currentStatus)
    for i in range(5):
        #if (correctLetterAndPosition[i] == True):
        #    pass
        if (chosenWord[i] == firstGuess[i]):
            #print(i)
            correctLetter[i] = True
            correctLetterAndPosition[i] = True
            #currentStatus[i] = firstGuess[i]
        else:
            for j in range(5):
                if (j == i):
                    pass
                if (chosenWord[i] == firstGuess[j]):
                    correctLetter[j] = True
                    #currentStatus[j] = firstGuess[i]
                else:
                    pass
                    #currentStatus[i] = firstGuess[i]
    for k in range(5):
        if (correctLetterAndPosition[k] == True):
            #logicProgress[k] = "Letter+Position"
            completionProgress[k] = Back.GREEN + firstGuess[k] + Style.RESET_ALL + " "
        elif (correctLetter[k] == True and correctLetterAndPosition[k] == False):
            #logicProgress[k] = "Letter"
            completionProgress[k] = Back.YELLOW + firstGuess[k] + Style.RESET_ALL + " "
        else:
            #logicProgress[k] = "None"
            completionProgress[k] = Back.RED + firstGuess[k] + Style.RESET_ALL + " "
   # for k in range(5):
   #     if (correctLetterAndPosition[k] == True):
   #         logicProgress[k] = "Letter+Position"
   #     elif (correctLetter[k] == True and correctLetterAndPosition[k] == False and logicProgress[k] != "Letter+Position"):
   #         logicProgress[k] = "Letter"
   #     elif (correctLetterAndPosition[k] == True or correctLetter[k] == True):
   #         pass
   #     else:
   #         logicProgress[k] = "None"
    #print("This is what you have guessed:")
    #print(currentStatus)
    #Issue with current loop system: Once you guess a letter it can't be guessed again, so that means the color quality of the letter can't go up.
            #Idea: keep the "letters" array as a constant reference and then have another letter appearance array. Also when you get a GREEN letter make it so that the loop can't access it
                #Don't know yet how to make it so that you can only change the color when it's Blue
    #This above issue  is fixed as far as I can tell.
   
    #Another issue: For some reason, when you guess the right letter but wrong position, the system will mark the letter as not being in the word.
    #Think  this is fixed, but not sure. This was an issue with the earlier system so it's probably better now.
   
    for n in range(5):
        for o in range(26):
            if (letters[o] == firstGuess[n]):
                 if (correctLetterAndPosition[n] == True):
                     list[o].color = "green"
                     #lettersAppearance[o] = Back.GREEN + letters[o] + Style.RESET_ALL
                 elif (correctLetter[n] == True and correctLetterAndPosition[k] == False and list[o].color!="green"):
                     list[o].color = "yellow"
                     #lettersAppearance[o] = Back.YELLOW + letters[o] + Style.RESET_ALL
                 elif (correctLetterAndPosition[n] == False and correctLetterAndPosition[k] == False and list[o].color!="green" and list[o].color!="yellow"):
                     list[o].color = "red"
                 else:
                     pass
                     #lettersAppearance[o] = Back.RED + letters[o] + Style.RESET_ALL
    if (bigLoop == 0):
        #print("This is what you have guessed.")
        print("Below is your progress with each letter. A red background means the letter is not in the word,\nA yellow background means the letter is in the word but in the wrong position,\nand a green background means the letter is in the right place.")
    #print(logicProgress)
    #print(completionProgress)
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
              #print(lettersAppearance[m] + " ", end='')
          print(" ", end='')
    print(Style.RESET_ALL)
    if (correctLetter == [True, True, True, True, True]):
        print("Congratulations, you won!")
        time.sleep(20)
        sys.exit("Game over!")
    #print('Correct letters\n')
    #print(correctLetter)
    #print('Correct letters and correct position\n')
    #print(correctLetterAndPosition)
    validWord = False
    correctLetter = [False, False, False, False, False]
    correctLetterAndPosition = [False, False, False, False, False]
    currentStatus = [None, None, None, None, None]
    completionProgress = [None, None, None, None, None]
print("You lose!")
time.sleep(20)
sys.exit("Game over!")
