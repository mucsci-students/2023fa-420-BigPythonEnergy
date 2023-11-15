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

def getScoreboard():
    sorted = scoreboard.sort_values(by='score', ascending=False)
    return sorted.head(10)

def addScore(name, score, letters, rletter):
    new_row = pd.DataFrame({'name': [name], 'score': [score], 'letters': [letters], 'special letter': [rletter]})
    # Concatenate the new DataFrame with the existing DataFrame
    scoreboard = pd.concat([scoreboard, new_row], ignore_index=True)
    scoreboard.to_json("scoreboard.json")