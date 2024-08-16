import random

def choose_word(): #chooses a random word from a list of words
    words = ["python", "hangman", "challenge", "programming", "development"]
    return random.choice(words)

def display_hangman(tries): # displays the hangman based on the number of tries left
    stages = [
        """
           -----
           |   |
           |   O
           |  /|\\
           |  / \\
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|\\
           |  /
           -
        """,
        """
           -----
           |   |
           |   O
           |  /|
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |   |
           |
           -
        """,
        """
           -----
           |   |
           |   O
           |
           |
           -
        """,
        """
           -----
           |   |
           |
           |
           |
           -
        """,
        """
           -----
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def play(): # plays the game
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    tries = 6


    print("Welcome to Hangman!")
   
    while tries > 0 and word_letters != guessed_letters: #loop until the word is guessed or the player runs out of tries
        print(display_hangman(tries))
        print("Guessed letters:", " ".join(guessed_letters))
       
        # Display the current state of the word
        word_display = [letter if letter in guessed_letters else '_' for letter in word]
        print("Current word:", " ".join(word_display))


        guess = input("Guess a letter: ").lower()
       
        if guess in guessed_letters: # Decidess if the letter has already been guessed
            print("You already guessed that letter.")
        elif guess in word_letters: # Decides if the letter is in the word
            guessed_letters.add(guess)
            print("Good guess!")
        else: # Decides if the letter is not in the word
            guessed_letters.add(guess)
            tries -= 1
            print("Wrong guess. Tries left:", tries)


    if word_letters == guessed_letters: # Decides if the player won or lost
        print("Congratulations! You've guessed the word:", word)
    else:
        print(display_hangman(tries)) # Decides if the player lost
        print("Sorry, you lost. The word was:", word)


if __name__ == "__main__": # Runs the game
    play()