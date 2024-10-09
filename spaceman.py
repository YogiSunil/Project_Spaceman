import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word.

    Returns: 
        string: The secret word to be used in the spaceman guessing game
    '''
    with open('C:/Users/naths/Documents/projects/words.txt', 'r') as f:
        words_list = f.readlines()
        
    words_list = words_list[0].split(' ')  # Comment out this line if your file has one word per line.
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    Checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): The word the user is trying to guess.
        letters_guessed (list of strings): List of letters that have been guessed so far.

    Returns: 
        bool: True if all letters of secret_word are in letters_guessed, False otherwise.
    '''
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    '''
    Displays the secret word with guessed letters and underscores for remaining letters.

    Args:
        secret_word (string): The word the user is trying to guess.
        letters_guessed (list of strings): List of guessed letters.

    Returns: 
        string: Guessed word with letters and underscores.
    '''
    return ' '.join(letter if letter in letters_guessed else '_' for letter in secret_word)

def is_guess_in_word(guess, secret_word):
    '''
    Checks if the guessed letter is in the secret word.

    Args:
        guess (string): The letter guessed this round.
        secret_word (string): The word the user is trying to guess.

    Returns:
        bool: True if the guess is in the secret_word, False otherwise.
    '''
    return guess in secret_word

def draw_spaceman(attempts):
    ''' a spaceman based on the number of incorrect guesses.'''
    stages = [
        '''
           ----- 
           |   | 
           |   O 
           |  /|\\ 
           |  / \\ 
           | 
        ''',
        '''
           ----- 
           |   | 
           |   O 
           |  /|\\ 
           |  / 
           | 
        ''',
        '''
           ----- 
           |   | 
           |   O 
           |  /| 
           | 
           | 
        ''',
        '''
           ----- 
           |   | 
           |   O 
           |   
           | 
           | 
        ''',
        '''
           ----- 
           |   | 
           |   
           |   
           | 
           | 
        ''',
        '''
           ----- 
           |   
           |   
           |   
           | 
           | 
        ''',
        '''
               

           |   
           |   
           |   
           | 
           | 
        '''
    ]
    # Ensure attempts is always between 0 and 7
    print(stages[min(attempts, len(stages) - 1)])

def spaceman():
    '''The function that controls the spaceman game. It handles the game flow.'''
    play_again = True

    while play_again:
        secret_word = load_word()
        letters_guessed = []
        attempts_left = 7  # number of stages

        print("Welcome to Spaceman!")
        print(f"The secret word contains {len(secret_word)} letters.")

        while attempts_left > 0 and not is_word_guessed(secret_word, letters_guessed):
            print(f"\nYou have {attempts_left} incorrect guesses left.")
            draw_spaceman(attempts_left)
            print("Current word:", get_guessed_word(secret_word, letters_guessed))
            
            guess = input("Please guess a letter: ").lower()

            # Ensure that only one letter is guessed
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            # Check if the letter was already guessed
            if guess in letters_guessed:
                print("You've already guessed that letter. Try again.")
                continue
            
            # Add guess to the list of guessed letters
            letters_guessed.append(guess)

            if is_guess_in_word(guess, secret_word):
                print(f"Good guess! {guess} is in the word.")
            else:
                attempts_left -= 1
                print(f"Oops! {guess} is not in the word.")

        # Check if the user has won or lost
        if is_word_guessed(secret_word, letters_guessed):
            print(f"\nCongratulations! You've guessed the word: {secret_word}")
        else:
            print(f"\nGame over! You've run out of attempts. The word was: {secret_word}")

        # Ask if the user wants to play again
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        play_again = play_again_input == 'yes'

# Start the game
spaceman()
