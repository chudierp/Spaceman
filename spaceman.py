import random



def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in letters_guessed
    
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True
           
        
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    display = ""
    for letter in secret_word:
        if letter in letters_guessed :
            display += (letter+ " ")
        else: 
            display += "_ "

    return display            



def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    if guess in secret_word: 
        print ('Great! That is correct')
        is_guess_in_word = True
    else: 
        print ('That is WRONG! try again')
        is_guess_in_word = False       
    return is_guess_in_word





def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    
    letters_guessed = list()
    numberofguess = 7
    #TODO: show the player information about the game according to the project spec
    
    
    print((f'Welcome to Spaceman! I am thinking of a word that is {len(secret_word)} letters long.'))
    #print('_ _ _ _ _ _ _')
    
    
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    running = True
    while running:
        print(f'You have {numberofguess} guesses left')
        print(get_guessed_word(secret_word, letters_guessed))
        guess=(input('Please guess a letter: '))
        #allowing word detection regardless of casing
        guess = guess.lower()
        #catching already guessed letters and telling the user to guess a new letter
        
        if guess in letters_guessed:
            print('Letter has already been guessed, guess a new letter')
        else:     
            if is_guess_in_word(guess,secret_word) is False: #Have to place the parenthesis anytime you're calling a function
                numberofguess -= 1
                print('result came back false')
            else:
            
                print('result came back true')
        print(numberofguess)
        letters_guessed.append(guess)
    
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        
        #TODO: show the guessed word so far
    

        #TODO: check if the game has been won or lost


        is_guess_in_word(guess, secret_word)
        print (get_guessed_word(secret_word,letters_guessed))
        
        result = is_word_guessed(secret_word, letters_guessed)
        if result == True:
            print('YOU WON!')
            break #exit out of the loop
        if numberofguess == 0:
            print('GAME OVER!The word was', secret_word)
            break
            
def play_again():
    guess=(input('Play Again?(Y/N'))
    guess = guess.lower()
    if guess == 'y':
        return True
    else:
        return False


# secret_word = load_word()
# print(secret_word)
# spaceman(secret_word)

# while play_again():
# #These function calls that will start the game
#     secret_word = load_word()
#     print(secret_word)
#     spaceman(secret_word)

if  __name__== '__main__':
    secret_word = load_word()
    print(secret_word)
    spaceman(secret_word)

    while play_again():
    #These function calls that will start the game
        secret_word = load_word()
        print(secret_word)
        spaceman(secret_word)

     