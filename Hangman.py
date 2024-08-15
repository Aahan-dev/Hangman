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
    