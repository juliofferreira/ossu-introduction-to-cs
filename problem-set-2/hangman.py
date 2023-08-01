# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    print('\n')
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings).
    
    Returns a word from wordlist at random.
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase.
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase.
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise.
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing.
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    guessed_word = ''

    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += letter
    
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = string.ascii_lowercase

    for letter in letters_guessed:
        if letter in available_letters:
            available_letters = available_letters.replace(letter, '')

    return available_letters



def is_letter_correct(secret_word, letter_guessed):
    '''
    secret_word: string, the word the user is guessing
    letter: string, the letter the user guessed
    returns: boolean, True if the letter guessed is in secret_word;
      False otherwise
    '''
    return letter_guessed in secret_word



def is_guess_valid(letter, letters_guessed):
    '''
    letter: string, the letter the user guessed
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: (boolean, string), True if the letter guessed is valid;
      False otherwise; string with error type
    '''
    if letter in letters_guessed:
        return (False, 'already guessed')
    
    if letter.isalpha():
        return (True, '')
    else:
        return (False, 'not alpha')
    

    
def calculate_points(secret_word, guesses_remaining):
    '''
    secret_word: string, the word the user is guessing
    guesses_remaining: number, the guesses remaining
    returns: number, user's score
    '''
    number_unique_letters = len(set(secret_word))

    return guesses_remaining * number_unique_letters



def print_initial_message(secret_word):
    '''
    secret_word: string, the word the user is guessing
    '''
    secret_word_length = len(secret_word)

    print('Welcome to the Hangman game!')
    print(f'I am thinking of a word that is {secret_word_length} letters long.')
    print('-------------')



def finalize_game(state, secret_word):
    '''
    secret_word: string, the word the user is guessing
    state: the state of the game
    '''
    if state['player_has_won']:
        print('  Congratulations, you won!')
        print(f'  Your total score for this game is: {calculate_points(secret_word, state["number_of_guesses"])}')
    elif state["number_of_guesses"] == 0:
        print('  You lost!')
        print(f'  The word was: {secret_word}')



def handle_invalid_letter(state, error_type, secret_word):
    '''
    state: the state of the game
    error_type: string, the error type; 'not alpha' or 'already guessed'
    secret_word: string, the word the user is guessing
    '''
    if error_type == 'not alpha':
        if state['number_of_warnings'] != 0:
            state['number_of_warnings'] -= 1
            print(f'  Oops! That is not a valid letter. You now have {state["number_of_warnings"]} warnings left: {get_guessed_word(secret_word, state["letters_guessed"])}')
            print('  ------------')
        else:
            print(f'  Oops! That is not a valid letter. You lose one guess: {get_guessed_word(secret_word, state["letters_guessed"])}')
            print('  ------------')
            state["number_of_guesses"] -= 1
    elif error_type == 'already guessed':
        if state["number_of_warnings"] != 0:
            state["number_of_warnings"] -= 1
            print(f"  Oops! You've already guessed that letter. You now have {state['number_of_warnings']} warnings left: {get_guessed_word(secret_word, state['letters_guessed'])}")
            print('  ------------')
        else:
            print(f"  Oops! You've already guessed that letter. You lose one guess: {get_guessed_word(secret_word, state['letters_guessed'])}")
            print('  ------------')
            state["number_of_guesses"] -= 1



def print_turn_message(state):
    '''
    state: the state of the game
    '''
    print(f'  You have {state["number_of_guesses"]} guesses left.')

    available_letters = get_available_letters(state['letters_guessed'])
    print(f'  Available letters: {available_letters}')



def handle_finish_turn_message(state, guessed_letter, secret_word):
    '''
    state: the state of the game
    guessed_letter: string, the letter guessed by the player 
    secret_word: string, the word the user is guessing
    '''
    is_guessed_letter_correct = is_letter_correct(secret_word, guessed_letter)

    if is_guessed_letter_correct:
        print('  Good guess: ', get_guessed_word(secret_word, state['letters_guessed']))
    else:
        print('  Oops! That letter is not in my word: ', get_guessed_word(secret_word, state['letters_guessed']))
        if guessed_letter in ['a', 'e', 'i', 'o', 'u']:
            state["number_of_guesses"] -= 2
        else:
            state["number_of_guesses"] -= 1

    print('  ------------')



def check_if_player_won(state, secret_word):
    '''
    state: the state of the game
    '''
    if is_word_guessed(secret_word, state['letters_guessed']):
        state['player_has_won'] = True
        


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    state = {
        'number_of_guesses': 6, 
        'number_of_warnings': 3, 
        'letters_guessed': [], 
        'player_has_won': False
    }

    print_initial_message(secret_word)

    while not state['player_has_won'] and state['number_of_guesses'] != 0:
      
      print_turn_message(state)

      guessed_letter = input('  Please guess a letter: ').lower()
      (is_valid, error_type) = is_guess_valid(guessed_letter, state['letters_guessed'])
      if not is_valid:
          handle_invalid_letter(state, error_type, secret_word)
          continue

      state['letters_guessed'].append(guessed_letter)

      handle_finish_turn_message(state, guessed_letter, secret_word)

      check_if_player_won(state, secret_word)

    finalize_game(state, secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word = my_word.replace(' ', '')

    if len(my_word) != len(other_word):
        return False

    index = 0
    for letter in my_word:
        
        index += 1
        if letter == '_':
            if other_word[index-1] in my_word:
                return False
            continue
        if letter != other_word[index-1]:
            return False
        
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: string, returns every word in wordlist that matches my_word, separated by ' '
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''

    matched_words = ''

    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words += word + ' '

    if matched_words == '':
        print('No matches found')
        return

    return matched_words



def is_guess_valid_with_hints(letter, letters_guessed):
    '''
    letter: string, the letter the user guessed
    letters_guessed: list (of letters), which letters have been guessed so far.
    returns: (boolean, string), True if the letter guessed is valid;
      False otherwise; string with error type
    '''
    if letter in letters_guessed:
        return (False, 'already guessed')
    
    if letter.isalpha() or letter == '*':
        return (True, '')
    else:
        return (False, 'not alpha')
    


def handle_hint(secret_word, state):
    '''
    state: the state of the game
    guessed_letter: string, the letter guessed by the player 
    secret_word: string, the word the user is guessing
    '''

    my_word = get_guessed_word(secret_word, state['letters_guessed'])
    print(f'  Possible matches are: {show_possible_matches(my_word)}')
    print('  ------------')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    state = {
        'number_of_guesses': 6, 
        'number_of_warnings': 3, 
        'letters_guessed': [], 
        'player_has_won': False
    }

    print_initial_message(secret_word)

    while not state['player_has_won'] and state['number_of_guesses'] != 0:
      
        print_turn_message(state)

        guessed_letter = input('  Please guess a letter: ').lower()
        (is_valid, error_type) = is_guess_valid_with_hints(guessed_letter, state['letters_guessed'])
        if not is_valid:
            handle_invalid_letter(state, error_type, secret_word)
            continue

        if guessed_letter == '*':
            handle_hint(secret_word, state)
            continue
        
        state['letters_guessed'].append(guessed_letter)

        handle_finish_turn_message(state, guessed_letter, secret_word)

        check_if_player_won(state, secret_word)

    finalize_game(state, secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
