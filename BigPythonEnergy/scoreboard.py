import pandas as pd
import os
import platform

scoreboard = pd.read_json("scoreboard.json")

# Gets the scoreboard based on the current game's letters and special letter.
def getScoreboard(letters, rletter):
    scoreboard = pd.read_json("scoreboard.json")
    sorted = scoreboard.sort_values(by='score', ascending=False)
    firstresult = sorted.loc[sorted['letters'] == letters]
    secondresult = firstresult.loc[firstresult['special letter'] == rletter]
    if secondresult.empty:
        return "There is no scoreboard for this puzzle yet."
    return secondresult.head(10).to_string(index=False)

# Adds a player to the scoreboard with a name and score for specifically the current puzzle.
def addScore(name, score, letters, rletter):
    if len(name) > 32:
        name = name[0:32]
    scoreboard = pd.read_json("scoreboard.json")
    new_row = pd.DataFrame({'name': [name], 'score': [score], 'letters': [letters], 'special letter': [rletter]})
    # Concatenate the new DataFrame with the existing DataFrame
    scoreboard = pd.concat([scoreboard, new_row], ignore_index=True)
    scoreboard.to_json("scoreboard.json")
    return True

# Checks if a particular name is in the scoreboard for a puzzle, specifically for testing purposes.
def inScoreboard(letters, rletter, name):
    scoreboard = pd.read_json("scoreboard.json")
    sorted = scoreboard.sort_values(by='score', ascending=False)
    firstresult = sorted.loc[sorted['letters'] == letters]
    secondresult = firstresult.loc[firstresult['special letter'] == rletter]
    thirdresult = secondresult.loc[secondresult['name'] == name]
    if thirdresult.empty:
        return False
    return True