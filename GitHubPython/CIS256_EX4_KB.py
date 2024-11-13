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

# Using built in function random we will select a random animal name everytime we run the code 
# and store the animal's name in variable rand_selected_animal
rand_selected_animal = random.choice(predefined_word_list).upper()
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
        for count in range(animal_length):
            if user_input == animal_selected_list[count]:
                animal_display[count] = user_input
        vowel_guessed = True  # Exit loop after correct vowel
    else:
        print(f"Sorry! The vowel '{user_input}' is not in the animal's name.")
    
    print("Current Display:", " ".join(animal_display))

# Allow user to guess other letters
print("You now have 3 more tries to guess to complete animal's name.")
while attempts < 3 and '_' in animal_display:
    user_input = input("Guess another letter: ").upper()
    
    # Check if the guessed letter is in the animal name
    if user_input in rand_selected_animal:
        print(f"Good guess! '{user_input}' is in the animal's name.")
        
        # Reveal the guessed letter's position(s) in the display
        for count in range(animal_length):
            if user_input == animal_selected_list[count]:
                animal_display[count] = user_input
    else:
        print(f"Sorry! '{user_input}' is not in the animal's name.")
        attempts += 1
    
    # Show the updated display
    print("Current Display:", " ".join(animal_display))

# Check if the game was won or lost
if '_' not in animal_display:
    print("Congratulations! You've guessed the animal:", rand_selected_animal)
else:
    print("Out of attempts! The animal was:", rand_selected_animal)
