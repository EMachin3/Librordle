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
#print(letter1 + letter2 + letter3 + letter4 +letter5)
validWord = False
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
            #completionProgress[k] = "Letter+Position"
            completionProgress[k] = Back.GREEN + firstGuess[k] + Style.RESET_ALL + " "
        elif (correctLetter[k] == True and correctLetterAndPosition[k] == False):
            #completionProgress[k] = "Letter"
            completionProgress[k] = Back.YELLOW + firstGuess[k] + Style.RESET_ALL + " "
        else:
            #completionProgress[k] = "None"
            completionProgress[k] = Back.RED + firstGuess[k] + Style.RESET_ALL + " "
    #print("This is what you have guessed:")
    #print(currentStatus)
    if (bigLoop == 0):
        #print("This is what you have guessed.")
        print("Below is your progress with each letter. A red background means the letter is not in the word,\nA yellow background means the letter is in the word but in the wrong position,\nand a green background means the letter is in the right place.")
    #print(completionProgress)
    for l in range(5):
        print(completionProgress[l], end='')
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
