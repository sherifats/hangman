import random
##new hangman game
##create a dictionary of words that the game chooses at random

wordDic = ["hello", "umbrella", "dictionary", "words", "guessing", "hangman"]
play = True

chosenWord = random.choice(wordDic)
numWrong = 0

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
    elif numWrong == 5:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("      |   ")
        print("   _______")
    elif numWrong == 5:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("  /   |   ")
        print("   _______")
    elif numWrong == 5:
        print("   ___    ")
        print("   |  |   ")
        print("   0  |   ")
        print("  /|\ |   ")
        print("   |  |   ")
        print("  / \ |   ")
        print("   _______")


    for char in chosenWord:
        print("_", end=" ")

    guess = input("Choose a letter: ")
    if guess not in chosenWord:
        print("that's incorrect")
        numWrong += 1
    else:
        print("good work!")
    


    play = False