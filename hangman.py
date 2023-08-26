import random
##new hangman game
##create a dictionary of words that the game chooses at random

wordDic = ["hello", "umbrella", "dictionary", "words", "guessing", "hangman"]
play = True

chosenWord = random.choice(wordDic)
lenWord = len(chosenWord)
numWrong = 0
guessedLetters = []
status = ""

while(play):
    
    if numWrong == 0:
        print("   ___    ")
        print("   |  |   ")
        print("      |   ")
        print("      |   ")
        print("      |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 1:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("      |   ")
        print("      |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 2:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("    \ |   ")
        print("      |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 3:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  / \ |   ")
        print("      |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 4:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("      |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 5:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 6:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("  /   |   ")
        print("   _______")
    elif numWrong == 7:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("  / \ |   ")
        print("   _______")


    for char in chosenWord:
        status += ("_ ")
    print(status)

    guess = input("Choose a letter: ")

    
    if guess in guessedLetters:
        print("you've already used this letter, try again")
    elif guess not in chosenWord:
        print("that's incorrect")
        guessedLetters.append(guess)
        numWrong +=1
    elif guess in chosenWord:
        guessedLetters.append(guess)
        print("correct!")

        

    if numWrong == 8:
        print("game over")
        play = False
