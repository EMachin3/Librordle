import time
import os
import enchant
import sys
chosenWord = input("Type today's word.\n")
#print(chosenWord)
d = enchant.Dict("en_US")
if (d.check(chosenWord)):
    print("that's a word")
    time.sleep(1.0)
else:
    print("that's not a word")
    time.sleep(2.0)
    sys.exit("choose a real word")
if (len(chosenWord) == 5):
    print("okay that word works")
    time.sleep(2.0)
    os.system("cls")
else:
    print("that's not the right length")
    time.sleep(2.0)
    sys.exit("choose a word that's the correct length")
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
        #***This section of code works***
        #if (correctLetterAndPosition[i] == True):
        #    pass
        if (chosenWord[i] == firstGuess[i]):
            #print(i)
            correctLetter[i] = True
            correctLetterAndPosition[i] = True
            #currentStatus[i] = firstGuess[i]
        #***This section of code works***
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
            completionProgress[k] = "Letter+Position"
        elif (correctLetter[k] == True and correctLetterAndPosition[k] == False):
            completionProgress[k] = "Letter"
        else:
            completionProgress[k] = "None"
    #print("This is what you have guessed:")
    print(currentStatus)
    if (bigLoop == 0):
        print("This is what you have guessed:")
        print("Here is your progress with each letter. 'None' means the letter is not in the word,\n'Letter' means the letter is in the word but in the wrong position,\nand 'Letter+Position' means the letter is in the right place.")
    print(completionProgress)
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
