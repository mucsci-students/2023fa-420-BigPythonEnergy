import pandas as pd
import os
import platform

def clearScreen():
    system_platform = platform.system()
    if system_platform == "Windows":
        os.system("cls")  # Clear screen on Windows
    else:
        os.system("clear")  # Clear screen on macOS and Linux

scoreboard = pd.read_json("scoreboard.json")

def getScoreboard(letters, rletter):
    scoreboard = pd.read_json("scoreboard.json")
    sorted = scoreboard.sort_values(by='score', ascending=False)
    firstresult = sorted.loc[sorted['letters'] == letters]
    secondresult = firstresult.loc[firstresult['special letter'] == rletter]
    if secondresult.empty:
        return "There is no scoreboard for this puzzle yet."
    return secondresult.head(10)

def addScore(name, score, letters, rletter):
    scoreboard = pd.read_json("scoreboard.json")
    new_row = pd.DataFrame({'name': [name], 'score': [score], 'letters': [letters], 'special letter': [rletter]})
    # Concatenate the new DataFrame with the existing DataFrame
    scoreboard = pd.concat([scoreboard, new_row], ignore_index=True)
    scoreboard.to_json("scoreboard.json")