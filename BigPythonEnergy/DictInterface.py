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

df = pd.read_json("words.json")

# Simple helper function to ensure 7 unique characters
def has_7_unique_letters(word):
    return len(set(word)) == 7

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
    return len(validWords)

# populate function responsible for driving the population of the bingo sheet
# A while loop running on the size of the words
# A switch case to know what column to get into
def populateBingo(bingoSheet, required, letters):
    size = 4
    while size <= 15:
        match(size):

            case 4:
                i = 1
                for letter in letters:
                    bingoSheet[i][1] = popHelper("fours", letter, required, letters)
                    i += 1
                size = 5

            case 5:
                i = 1
                for letter in letters:
                    bingoSheet[i][2] = popHelper("fives", letter, required, letters)
                    i += 1
                size = 6
                
            case 6:
                i = 1
                for letter in letters:
                    bingoSheet[i][3] = popHelper("sixes", letter, required, letters)
                    i += 1
                size = 7
                
            case 7:
                i = 1
                for letter in letters:
                    bingoSheet[i][4] = popHelper("sevens", letter, required, letters)
                    i += 1
                size = 8
                
            case 8:
                i = 1
                for letter in letters:
                    bingoSheet[i][5] = popHelper("eights", letter, required, letters)
                    i += 1
                size = 9

            case 9:
                i = 1
                for letter in letters:
                    bingoSheet[i][6] = popHelper("nines", letter, required, letters)
                    i += 1
                size = 10

            case 10:
                i = 1
                for letter in letters:
                    bingoSheet[i][7] = popHelper("tens", letter, required, letters)
                    i += 1
                size = 11

            case 11:
                i = 1
                for letter in letters:
                    bingoSheet[i][8] = popHelper("elevens", letter, required, letters)
                    i += 1
                size = 12

            case 12:
                i = 1
                for letter in letters:
                    bingoSheet[i][9] = popHelper("twelves", letter, required, letters)
                    i += 1
                size = 13

            case 13:
                i = 1
                for letter in letters:
                    bingoSheet[i][10] = popHelper("thirteens", letter, required, letters)
                    i += 1
                size = 14

            case 14:
                i = 1
                for letter in letters:
                    bingoSheet[i][11] = popHelper("fourteens", letter, required, letters)
                    i += 1
                size = 15

            case 15:
                i = 1
                for letter in letters:
                    bingoSheet[i][12] = popHelper("fifteens", letter, required, letters)
                    i += 1
                size += 1
                
    return bingoSheet



# provide the length, starting letter, required letter, and acceptable letters
# and this function will tell you how many valid words there are of the length
# provided and starting with the letter provided
def popHelper(row, starter, required, letters):
    validWords = set()
    words = df[row].dropna()

    # Search through each word in every column
    for word in words:

        # Ensure the word contains the required letter, starts with tup, and contains only the other 6 acceptable letters
        if required in word and word[:1] == starter and all(letter in letters or letter == required for letter in word):
            validWords.add(word)

    return len(validWords)
        
# This function is responsible for caluculating and placing all sigma values
def populateSigma(bingo):
    # Calculate the sum for each row
    for row in bingo[1:]:
        row[13] = sum(row[1:13])

    # Calculate the sum for each column
    for j in range(1, 8):
        bingo[8][j] = sum(row[j] for row in bingo[1:])
    
    row_sum = sum(row[13] for row in bingo[1:])
    column_sum = sum(bingo[8][j] for j in range(1, 8))
    bingo[8][13] = row_sum
        
    return bingo

# This is the main and only bingo Hint call
# All that is required is the required letter and the acceptable letters
# NOTE: It is important that 'letters' contains no duplicate values
#           otherwise the bingo sheet will not be correct
def bingoHint(required, letters):
    bingoSheet = [[0 for _ in range(14)] for _ in range(9)]
    
    # Initialize the numbers in the first row
    for i in range(13):
        bingoSheet[0][i] = i + 3

    s = 1
    i = 1  # Start at the second row
    while s < 9:
        for letter in letters:
            bingoSheet[i][0] = letter
            s += 1
            i += 1
            if s >= 9:
                break
                
    bingoSheet[0][0] = ''
    sigma_symbol = '\u03A3'
    bingoSheet[0][13] = sigma_symbol
    bingoSheet[8][0] = sigma_symbol
    
    temp = populateBingo(bingoSheet, required, letters)
    bingo = populateSigma(temp)

    return bingo

# helper function to check if a given word is a pangram of the letters passed
def isPangram(word, letters):
    if word is None or letters is None:
        return False
    return set(word).issuperset(set(letters))

# driver function to iterate through valid words, 
# checking if they are pangrams and return the number of pangrams
def countPangram(required, letters):
    count = 0
    validWords = findValid(required, letters)
    for word in validWords:
        if (isPangram(word, letters)):
            count += 1
    
    return count

def countPerfect(required, letters):
    count = 0
    validWords = findValid(required, letters)
    for word in validWords:
        if (isPangram(word, letters) and len(word) == 7):
            count += 1

    return count

def countPangramAndPerfect(required, letters):
    pTypes = []
    pTypes.append(countPangram(required, letters))
    pTypes.append(countPerfect(required, letters))
    return pTypes