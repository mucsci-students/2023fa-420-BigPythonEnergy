import pandas as pd
import random
import os


df = pd.read_json("words.json")

def has_7_unique_letters(word):
    return len(set(word)) == 7

def randomWord():
    validColumns = df[['sevens', 'eights', 'nines', 'tens', 'elevens', 'twelves', 'thirteens', 'fourteens', 'fifteens']]
    eligibleWords = []

    for column in validColumns.columns:
        words = df[column].dropna()
        for word in words:
            if has_7_unique_letters(word):
                eligibleWords.append(word)
    
    selected = random.choice(eligibleWords)
    return selected

def findValid(required, letters):
    validWords = set()
    for column in  df.columns:
        words = df[column].dropna()
        for word in words:
            if required in word and all(letter in letters or letter == required for letter in word):
                validWords.append(word)
    return validWords


def isValid(guess):
    # switch case operating based on the length of the entered word
    match(len(guess)):
        case 4:
            fours = df['fours'].dropna()
            if guess in fours.values():
                return True
        case 5:
            fives = df['fives'].dropna()
            if guess in fives.values():
                return True
        case 6:
            sixes = df['sixes'].dropna()
            if guess in sixes.values():
                return True
        case 7:
            sevens = df['sevens'].dropna()
            if guess in sevens.values():
                return True
        case 8:
            eights = df['eights'].dropna()
            if guess in eights.values():
                return True
        case 9:
            nines = df['nines'].dropna()
            if guess in nines.values():
                return True
        case 10:
            tens = df['tens'].dropna()
            if guess in tens.values():
                return True
        case 11:
            elevens = df['elevens'].dropna()
            if guess in elevens.values():
                return True
        case 12:
            twelves = df['twelves'].dropna()
            if guess in twelves.values():
                return True
        case 13:
            thirteens = df['thirteens'].dropna()
            if guess in thirteens.values():
                return True
        case 14:
            fourteens = df['fourteens'].dropna()
            if guess in fourteens.values():
                return True
        case 15:
            fifteens = df['fifteens'].dropna()
            if guess in fifteens.values():
                return True
        case _:
            os.system('cls')
            print("The word you entered is not in the dictionary")
            return False