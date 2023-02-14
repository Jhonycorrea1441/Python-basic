import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hagman():
    word = get_valid_word(words)
    word_letters = set(word)  #Letters in the word.
    alphabet =set(string.ascii_uppercase)
    use_letters = set()  #what the user is guessed

    lives= 6
    #getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used
        # ' '.join(['a','b','cd']) --> 'a b cd'

        print('You have ',lives,' lives left and you have used these letters', ' '.join(use_letters))
        # What current word is (ie W - R D)
        word_list =[letter if letter in use_letters else '-' for letter in word]
        print('current word: ',' '.join(word_list))

        use_letters = input('Guessed a Letter: ').upper()
        if use_letters in alphabet - use_letters:
            use_letters.add(use_letters)
            if use_letters in word_letters:
                word_letters.remove(use_letters)
            
            else:
                lives = lives - 1 #take away a life if wrong
                print('Letter is not in the word.')

        elif use_letters in use_letters:
            print("You have already used  that character, please try again ")
        else:
            print("Invalid character, please try again. ")
    
    # gets here when len(word_letters) == 0

    
    if lives ==0:
        print('You died, Sorry. The word was ', word)
    else:
        print('You have guessed the word ',word,'!!')

hagman()

user_input = input('Type something...   .')
print(user_input)
