import random
##new hangman game
##create a dictionary of words that the game chooses at random

# Function to display the hangman
def display_hangman(numWrong):
    stages = [
        """
           ___
          |   |
              |
              |
              |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
              |
              |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
          |   |
              |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
         /|   |
              |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
         /|\\  |
              |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
         /|\\  |
         /    |
              |
        _______
        """,
        """
           ___
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        _______
        """
    ]

    return stages[numWrong]


wordDic = ["hello", "umbrella", "dictionary", "words", "guessing", "hangman"]
play = True

chosenWord = random.choice(wordDic)
lenWord = len(chosenWord)
numWrong = 0
guessedLetters = []
status = ["_"]*lenWord

while(play):
    
    print(display_hangman(numWrong))
    print(" ".join(status))

    guess = input("Choose a letter: ").lower()

    
    if guess in guessedLetters:
        print("you've already used this letter, try again")
    elif guess not in chosenWord:
        print("that's incorrect")
        guessedLetters.append(guess)
        numWrong +=1
    else:
        guessedLetters.append(guess)
        for i in range(lenWord):
            if chosenWord[i] == guess:
                status[i] = guess
        print("correct!")

    if numWrong == 7: 
        print("gameover. the correct word was", chosenWord)   
        play = False
    
    if "_" not in status:
        print("you've won!!")
        play = False