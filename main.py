
'''
Import module random which will allow us to pick a random value from a list
Import a set of english words in all lowercase letters
'''

import random
from english_words import english_words_lower_set


# Introduce the game + rules

print("Hello player! \nWelcome to the word guessing game! \n-----------------------------------\nThe objective is to determine the hidden word by guessing letters. \nBe careful, you can only guess up to 10 incorrect letters before you lose!")

# Create a function to request the user to select a difficulty - normal/hard.

def get_difficulty():
  global mode # Declare a global variable 'mode' 
  mode = input("\nPlease enter 'Normal' or 'Hard' to select difficulty: ").lower() # Request user input for the difficulty, and use the .lower() method in order to accept values such as "Normal" and "normal" equally

'''
if the user selected the normal mode, pick a random word from a predetermined list of easy to guess words.

else if the user selected the hard mode, pick a random word from the imported list of english words.

set the chosen word to be the 'secret' word the user has to guess! And store it in a seperate variable as a list, so we can iterate through the characters later!
'''

get_difficulty() # Call function 'get_difficulty'
difficulty_selected = False # Declare variable 'difficulty_selected' as False

while not difficulty_selected: # While the difficulty has not been selected:
  if mode == "normal": # If the input for 'mode' was 'normal':
    normal_word_list = ["apple", "picture", "bottle", "apartment", "igloo", "fan", "work", "python", "pencil", "school", "dice", "bandage"] # Create list of easy to guess words for the normal difficulty
    secret_word = random.choice(normal_word_list) # Pick a random word from the list and store in the variable 'secret_word'
    secret_word_in_list = list(secret_word) # Convert the secret_word from a string into a list and save in a new variable
    difficulty_selected = True # Break the loop by setting difficulty_selected to True

  elif mode == "hard": # Else if the input for 'mode' was 'hard':
    hard_word_list = list(english_words_lower_set) # Create a list out of the large set of imported words
    secret_word = random.choice(hard_word_list) # Pick a random word from the list and store in var 'secret_word'
    secret_word_in_list = list(secret_word) # Convert the secret_word from a string to a list and save in a new variable
    difficulty_selected = True # Break the loop by setting difficulty_selected to True

  else: # Else, if all the above conditions are not met:
    print("\nYou can only enter normal or hard.") # Remind the user they can only enter 'normal' or 'hard'
    get_difficulty() # Call the function 'get_difficulty' again
  
print("\n") # printing a new line for aesthetic purposes

'''
Create a function to run the process of the game, where the user's guess is requested and then checked to see if it is correct or not, and issue an appropiate message + variable changes.
'''

def guess(): 
  
  # DECLARING LOCAL VARIABLES

  # Let the user know how long the word is, declare variables and define the number of guesses.

  print(f"The word is {len(secret_word)} letters long. Good luck!") # Print the length of the word in letters with a starting message using an f-string
  dashes_as_string = '-' * len(secret_word) # Declare variable 'dashes_as_string' as a string of '-' the same length as the secret_word
  dashes = list(dashes_as_string) # Convert the data-type of the variable 'dashes_as_string' from string to list and store in a new variable
  guessed = False # Declare variable 'guessed' as False
  letters_attempted = [] # Declare variable 'letters_attempted' as an empty list
  guesses = 10 # Declare variable 'guesses' as 10 
  i = 0 # Declare variable i as 0

  '''
  Run a while loop under the conditions that the word has not yet been guessed AND the user has not run out of guesses.
  '''

  while not guessed and guesses > 0:
    
    print(f"You have {guesses} guesses remaining!") # Print the remaining number of guesses
    guess = input("Guess: ") # Request an input (guess via letter) from the user

    '''
    Set up if statements to determine if the user's input is invalid (ex. a number) and keep requesting input until a valid letter is guessed.
    '''

    if len(guess) > 1: # If the length of the user's guess is greater than 1 character
      print("\nYour guess must have exactly 1 character!") # Print a message to remind them that they must input only 1 letter
    
    elif not guess.isalpha(): # Else, if the guess is not a letter
      print("\nYour guess must be a letter!") # Print a message reminding the user their guess must be a letter
    
    elif guess.isupper(): # Else, if the guess is uppercase
        print("\nYour guess must be lowercase!") # Print a message reminding the user that their guess must be lowercase

    else: # If none of the above conditions are met, then their guess must be 1 lowercase letter, so move onto the rest of the code:

      if guess in letters_attempted: # If the guess is identical to a guess already stored in the list letters_attempted[]
        print(f"\nThe letter {guess} has already been guessed, try again!") # Print a message reminding the user that they have already guessed that letter 
      
      elif guess not in secret_word: # Else if the letter guessed is not in the secret word
        print(f"\nThe letter {guess} is not in the word!") # Print a message informing the user their guess was incorrect 
        guesses -= 1 # Take away a guess 
        letters_attempted.append(guess) # Add the guessed letter into the list letters_attempted[]
    
      else: # If none of the above conditions are met, then we know they guessed a correct letter, so move on to the rest of the code:

        print(f"\nThe letter {guess} is in the word! Great work!") # Print a message informing the user on the correct guess
        letters_attempted.append(guess) # Add the guessed letter into the list letters_attempted[]

        '''
        Create a for loop to iterate through the list containing the letters of the secret word to check if the guessed letter is one of them and if it is, replace the appropiate '-' with the letter.
        '''

        for x in secret_word_in_list:
          i += 1
          if x == guess:
            dashes[i-1] = guess
        i = 0
        dashes_as_string = "".join(dashes) # Set the value of the string containing the dashes to be the same as every item in the list 'dashes' combined with no spaces to seperate them. This essentially allows us to go from the list [a,-,-,l,e] to the string 'a--le', which is more user-friendly when printing. 
  
    if "-" not in dashes: # If there are no dashes left in the list of dashes
      guessed = True # Then all the letters have been guessed, and the word has been successfully guessed, so set guessed to True to end the While() loop
    
    print(f"Word: {dashes_as_string} \n__________________________________________ \n") # print the dashes with any replaced letters at the end of every iteration of the While() loop.

  if guessed: # After the While() loop ends, if the variable 'guessed' is True
    print(f"Congratulations! \nYou have guessed the secret word ({secret_word}) and won!") # Then the user has ended the loop by successfully guessing the letter and we print a congratulatory message as well as letting them know what the secret word they guessed was.

  else: # If the While() loop ended without the variable 'guessed' being set to True
    print(f" \nUnfortunately, you have no more tries left and lose. \nThe secret word was {secret_word}.") # Then that means the user ran out of guesses before they could successfully guess the word, so we print a message letting them know they lost and what the secret word they were trying to guess was.

guess() # Run the function guess()