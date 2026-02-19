import random

HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''', '''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''', '''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                 """)


words = "ape cat dog baboon elephant giraffe apple coconut monkey rubik mice mouse pineapple android apple house fence python grail zerg protoss terran llama fire policeman mamerto smad zebra lion luffy  universidad".split()

word = random.choice(words)

"""
1. word to guess
2. guess
3. You guessed 'letter', that's not in the word, you lose a life,
4. track life. 
5. You guess 
4. if a letter is guessed in a word, remove it from the word
"""

counter = 0

def display(word):
    word_dash = ""
    for _ in range(len(word)):
        word_dash += "_"

    print(f"Word to guess: {word_dash}")


def hangman(guess, word):
    if guess in word:
        return True
    else:
        return False


while counter < 2:
    display(word)
    counter += 1