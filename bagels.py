import random
''' task1 : get the sec num of desired length by using shuffle function '''

def randomNum(length):
    number = list(range(10))
    random.shuffle(number)
    secretNum = ''
    for i in range(length):
        secretNum += str(number[i])
    return secretNum

''' task2: to generate clue '''
def generateClue(guess,secretNum):
    if guess == secretNum:
        return('You get it !')

    clue = []
    for i in range (len(guess)):
        if guess[i] == secretNum[i]:
            clue.append('Fermi')
        elif guess[i] in secretNum:
            clue.append('Pico')
    if len(clue) == 0:
        return 'Bagels'
    clue.sort()
    return(' '.join(clue))

''' task3: check if user enter only digits '''
def checkNum(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
    return True

''' task4: check if user wants to play again '''
def playagain():
    print(' Do you want to play again ? yes or no')
    choice = input().lower()
    if 'y' in choice:
        return True
    else:
        return False

''' task5: now put everything together and start the game '''
WORDLENGTH = 3
MAXGUESS = 10
print('I am thinking of a %s-digit number. Try to guess what it is.' % (WORDLENGTH))
print('Here are some clues:')
print('When I say:    That means:')
print('  Pico         One digit is correct but in the wrong position.')
print('  Fermi        One digit is correct and in the right position.')
print('  Bagels       No digit is correct.')

while(True):
    secretNum = randomNum(WORDLENGTH)
    print('I have thought up a number.You have %s gusses to get it.'%(MAXGUESS))
    numGuess = 1
    while numGuess <= MAXGUESS:
        guess = ''
        while len(guess) != WORDLENGTH or not checkNum(guess):
            print('Guess #%s: ' %(numGuess))
            guess = input()
        clue = generateClue(guess,secretNum)
        print(clue)
        numGuess += 1
        if guess == secretNum:
            break
        if numGuess > MAXGUESS:
            print('You run out of guesses')
        
    if not playagain():
        break
        
        
    



