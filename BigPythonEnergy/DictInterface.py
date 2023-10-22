"""
This script provides a set of functions and utilities for working with English words and dictionaries.

- `clearScreen()`: A helper function to clear the command-line interface (CLI) screen based on the operating system.

- `df`: A Pandas DataFrame containing words from a JSON file.

- `has_7_unique_letters(word)`: A function that checks if a word has at least 7 unique characters.

- `randomWord()`: A function that selects a random word from the dictionary that meets the 7 unique character criteria.

- `findValid(required, letters)`: A function that finds words composed of the required letter and 6 other acceptable letters.

- `isValid(guess)`: A function that checks if a guessed word is a valid English word of varying lengths (4 to 15 letters).

The script is intended for word-related tasks and games, including word guessing games, word selection, and word validation.
"""


import pandas as pd
import random
import os
import platform

# Helper function for clearing the CLI Screen.
def clearScreen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")  # Clear screen on Windows
    else:
        os.system("clear")  # Clear screen on macOS and Linux

df = pd.read_json("words.json")

# Simple helper function to ensure 7 unique characters
def has_7_unique_letters(word):
    return len(set(word)) >= 7

# Function to choose a random word for the user
def randomWord():
    # valid columns is a dataframe containing only the columns with words long enough to have 7 unique characters
    # elgible words accumulates the words that contain only 7 unique characters
    validColumns = df[['sevens', 'eights', 'nines', 'tens', 'elevens', 'twelves', 'thirteens', 'fourteens', 'fifteens']]
    eligibleWords = []

    # Go column by column checking each word for 7 unique characters
    # All eligble words are appended to the eligbleWords list
    for column in validColumns.columns:
        words = df[column].dropna()
        for word in words:
            if has_7_unique_letters(word):
                eligibleWords.append(word)
    
    # Selelct random eligble word
    selected = random.choice(eligibleWords)
    return selected

# Function find all words made up of the required letter and the 6 other acceptable letters
def findValid(required, letters):
    # validWords accumulates the acceptable words with no duplicates
    validWords = set()

    # Search through each column
    for column in  df.columns:
        words = df[column].dropna()

        # Search through each word in every column
        for word in words:

            # Ensure the word contains the required letter and only the other 6 acceptable letters
            if required in word and all(letter in letters or letter == required for letter in word):
                validWords.add(word)
    return validWords

# Function to check that the guess entered is a valid english word
# Required letter and acceptable letter checking is done in the calle function
def isValid(guess):
    # switch case operating based on the length of the entered word
    match(len(guess)):

        # if the guess is 4 letters
        case 4:
            # Select column of 4 letter words
            fours = df['fours'].dropna()
            # search through the column to see if the guess is present
            if guess in fours.values:
                return True
            
        # if the guess is 5 letters
        case 5:
            fives = df['fives'].dropna()
            if guess in fives.values:
                return True
            
        # if the guess is 6 letters
        case 6:
            sixes = df['sixes'].dropna()
            if guess in sixes.values:
                return True
        
        # if the guess is 7 letters            
        case 7:
            sevens = df['sevens'].dropna()
            if guess in sevens.values:
                return True

        # if the guess is 8 letters
        case 8:
            eights = df['eights'].dropna()
            if guess in eights.values:
                return True
        
        # if the guess is 9 letters
        case 9:
            nines = df['nines'].dropna()
            if guess in nines.values:
                return True
            
        # if the guess is 10 letters
        case 10:
            tens = df['tens'].dropna()
            if guess in tens.values:
                return True
            
        # if the guess is 11 letters
        case 11:
            elevens = df['elevens'].dropna()
            if guess in elevens.values:
                return True
            
        # if the guess is 12 letters
        case 12:
            twelves = df['twelves'].dropna()
            if guess in twelves.values:
                return True
            
        # if the guess is 13 letters
        case 13:
            thirteens = df['thirteens'].dropna()
            if guess in thirteens.values():
                return True
            
        # if the guess is 14 letters
        case 14:
            fourteens = df['fourteens'].dropna()
            if guess in fourteens.values:
                return True
            

        # if the guess is 15 letters
        case 15:
            fifteens = df['fifteens'].dropna()
            if guess in fifteens.values:
                return True
            
        # Default case: the word was too long or too short, or was not found
        case _:
            clearScreen()
            print("The word you entered is not in the dictionary")
            return False
        

# tup is the starting letters we want to look for
# letters are the valid letters for the puzzle
# required is the required letter for the puzzle
def findStartingWith(tup, letters, required):    
    validWords = set()

    # check each column
    for column in  df.columns:
        words = df[column].dropna()

        # Search through each word in every column
        for word in words:

            # Ensure the word contains the required letter, starts with tup, and contains only the other 6 acceptable letters
            if required in word and word[:2] == tup and all(letter in letters or letter == required for letter in word):
                validWords.add(word)

    return validWords     
