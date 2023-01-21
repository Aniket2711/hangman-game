import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    print(word)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 6

    while len(word_letter) > 0 and lives > 0:

        print('You have', lives ,' lives left and You have used this letter: ',' '.join(used_letters))

        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))

        user_letter = input("\nIput a Letter : ").upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives = lives - 1
                print("letter not in the word")


        elif user_letter in used_letters:
            print("Already used the character . try Again ")

        else:
            print("Invalid character")
    
    if lives == 0:
        print("You died, sorry the word was ",word)
    else:
        print("You have gussed correctly",word)
hangman()
