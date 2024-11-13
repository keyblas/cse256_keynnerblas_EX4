# CIS256
# Keynner Blas
# Fall 2024
# EX4

import random

'''
Write the Code for the Game(20 marks):
Write a Python script named guess_the_word.py that implements the following:
The program selects a random word from a predefined list.
The user guesses one letter at a time.
If the guessed letter is in the word, it is revealed; otherwise, the program indicates the guess is incorrect.
The game continues until the user correctly guesses the entire word or runs out of attempts.
Display a congratulatory message when the word is guessed.
'''
# List of animal names to be selected randomly 
predefined_word_list = ["Alligator", "Alpaca", "Anaconda", "Ant", "Armadillo", 
                        "Elephant", "Eagle", "Eel", "Elk", "Impala", "Ibis",
                        "Iguana", "Ibex", "Indri", "Otter", "Octopus", "Orangutan", 
                        "Orca", "Owl", "Oyster", "Ostrich", "Oriole", "Utonagan", "Unau", 
                        "Urutu", "Umbrellabird", "Urchin"]

# Function will be used to select an animal from predefined_word_list randomly and return it
def select_random_animal():
    return random.choice(predefined_word_list).upper()


# variable rand_selected_animal will be used to stored randomly selected animal by calling Function select_random_animal()
rand_selected_animal = select_random_animal()
animal_selected_list = list(rand_selected_animal)

# We will store the length of random animal selected to show user how many letters animal to be guessed
# contains
animal_length = len(rand_selected_animal)
animal_display = ['_'] * animal_length

print(animal_display)

print(rand_selected_animal)

# We will ask user first to enter a vowel since the game is limited to only animals that start 
# with a vowel
user_input = str(input("Hello! Welcome to 'Guess the Animal Word Game' \n"
                       "Please select a vowel to see if it is included in the animal's name!\n"
                       )).upper()

# Since we want user to first enter a Vowel we will limit this to a set 
vowels = {'A', 'E', 'I', 'O', 'U'}

# we will also need to keep the number of attempts 
attempts = 0

# vowel_guessed will start as False and once it finds a match will be turn to True
vowel_guessed = False

# While loop to first check for Vowel only 
while not vowel_guessed:
    # to keep avoiding user from entering correct vowel but either lowercase or upper case we will convert input
    # to uppercase
    user_input = input("Please select a vowel to see if it is included in the animal's name!\n").upper()
    
    # IF user enters another letter that it is not a vowel, we will ask to enter a valid vowel and continue
    if user_input not in vowels:
        print("Please enter a valid vowel (A, E, I, O, U).")
        continue

    # IF vowel entered is included in animal stored in variable rand_selected_animal
    if user_input in rand_selected_animal:
        print(f"Good start! The vowel '{user_input}' is in the animal's name.")
        # For loop will be used to identify in which index vowel is located and also based on index it will be added to 
        # animal_display list to give user partial information of animal to be guessed
        for count in range(animal_length):
            if user_input == animal_selected_list[count]:
                animal_display[count] = user_input
        # Once a vowel that is included in animal is found we will exit this while loop and proceed with next one        
        vowel_guessed = True  
    else:
        # IF vowel is not included in animal to be guessed then we will inform user
        print(f"Sorry! The vowel '{user_input}' is not in the animal's name.")
    
    # This will be use to display partially animal's name by also having updated animal_display list 
    print("Current Display:", " ".join(animal_display))

# After user has entered a vowel included in animal to be guessed we will notify that he/she has 3 tries to complete 
# the animal's name
print("You now have 3 more tries to guess to complete animal's name.")

# While loop will be based on attempts which will run if its less then 3 and if animal_display still has _ instead of letter
while attempts < 3 and '_' in animal_display:
    # we are keeping everything in Uppercase to avoid errors if user enters the letter but in lowercase
    user_input = input("Guess another letter: ").upper()
    
    # IF letter entered by user is in animal to be guessed then we will inform user
    if user_input in rand_selected_animal:
        print(f"Good guess! '{user_input}' is in the animal's name.")
        
        # Same for loop as in first while loop - we will iterate and enter the letter in index where it is originally
        for count in range(animal_length):
            if user_input == animal_selected_list[count]:
                animal_display[count] = user_input
    # IF letter is not included in animal to be guessed then we are notifiying user and increment attempts by 1             
    else:
        print(f"Sorry! '{user_input}' is not in the animal's name.")
        attempts += 1
    
    # This show current animal to be guessed - with letters guessed and still _ remaining
    print("Current Display:", " ".join(animal_display))

# This will check if user has won or lose 
if '_' not in animal_display:
    print("Congratulations! You've guessed the animal:", rand_selected_animal)
else:
    print("Out of attempts! The animal was:", rand_selected_animal)
