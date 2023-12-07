import unittest
from Model import Model
from Puzzle import puzzle
from scoreboard import *
import pytest
import pandas as pd

model = Model()

def test_puzzle_null():
    assert isinstance(model.getPuzzle(), puzzle)
    assert model.getPuzzle().isNotNull() == False
    assert model.getPuzzle().getCurrentScore() == None
    assert model.getPuzzle().getFoundWordList() == None
    assert model.getPuzzle().getLetterList() == None
    assert model.getPuzzle().getLetters() == None
    assert model.getPuzzle().getNormalLetters() == None
    assert model.getPuzzle().getSpecialLetter() == None
    assert model.getPuzzle().getTotalScore() == None
    assert model.getPuzzle().getTotalWordList() == None
    assert model.getPuzzle().setFoundWord() == None
    assert model.getPuzzle().addFoundWord() == None
    assert model.getPuzzle().addScore() == None
    assert model.getPuzzle().setScore() == None
    assert model.getPuzzle().shuffleLetterList() == None

def test_puzzle_instantiation():
    letters = {"b", "r", "o", "m", "i", "n", "e"}
    specialLetter = "r"
    currentScore = 5
    foundWords = {"brine"}
    totalWords = {"brine"}
    model.setPuzzle(letters, specialLetter)
    assert model.getPuzzle().isNotNull()
    assert model.getPuzzle().getCurrentScore() == 0
    assert model.getPuzzle().getFoundWordList() == set()
    assert set(model.getPuzzle().getLetterList()) == letters
    assert model.getPuzzle().getLetters() == letters
    assert model.getPuzzle().getNormalLetters() == {"b", "o", "m", "i", "n", "e"}
    assert model.getPuzzle().getSpecialLetter() == "r"
    assert model.getPuzzle().getTotalScore() == 743
    assert model.getPuzzle().getTotalWordList() == {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"}
    model.setPuzzle(letters, specialLetter, currentScore, foundWords, totalWords)
    assert model.getPuzzle().isNotNull()
    assert model.getPuzzle().getCurrentScore() == 5
    assert model.getPuzzle().getFoundWordList() == {"brine"}
    assert set(model.getPuzzle().getLetterList()) == letters
    assert model.getPuzzle().getLetters() == letters
    assert model.getPuzzle().getNormalLetters() == {"b", "o", "m", "i", "n", "e"}
    assert model.getPuzzle().getSpecialLetter() == "r"
    assert model.getPuzzle().getTotalScore() == 5
    assert model.getPuzzle().getTotalWordList() == {"brine"}
    model.setPuzzle(letters, specialLetter)
    assert model.getPuzzle().getCurrentScore() == 0
    assert model.getPuzzle().getFoundWordList() == set()
    assert model.getPuzzle().getTotalScore() == 743
    assert model.getPuzzle().getTotalWordList() == {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"}

def test_bingo_pangram_hints():
    bingo = model.getBingoHint()
    assert isinstance(bingo, str)
    assert model.getPangramNumbers() == [2, 1]

def test_7_unique_letters():
    assert model.has_7_unique_letters("bromine")
    assert model.has_7_unique_letters("merbromin")
    assert model.has_7_unique_letters("dsa") is False
    assert model.has_7_unique_letters("") is False
    assert model.has_7_unique_letters("application") is False

def test_random_word():
    assert isinstance(model.getRandomWord(), str)
    assert len(set(model.getRandomWord())) == 7

def test_valid_word_list():
    assert isinstance(model.getValidWordList(), set)
    assert model.getValidWordList() == {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"}
    
def test_is_valid():
    assert model.isValid("bromine")
    assert model.isValid("cats")
    assert model.isValid("merbromin")
    assert model.isValid("lovely")
    assert model.isValid("cat") is False
    assert model.isValid("") is False
    assert model.isValid("aaaaaa") is False
    assert model.isValid("hippopotomonstrosesquippedaliophobia") is False

def test_each_starting_with():
    assert isinstance(model.getEachStartingWith("br"), int)
    assert model.getEachStartingWith("br") == 22

def test_shuffle_letter_list():
    letterList = model.getPuzzle().getLetterList()
    model.shuffleLetterList()
    assert letterList != model.getPuzzle().getLetterList()
    assert set(letterList) == set(model.getPuzzle().getLetterList())

def test_add_found_word():
    model.addFoundWord("boner")
    assert "boner" in model.getPuzzle().getFoundWordList()
    model.addFoundWord("")
    assert "" not in model.getPuzzle().getFoundWordList()

def test_add_score():
    model.getPuzzle().setScore(0)
    model.addScore(5)
    assert model.getPuzzle().getCurrentScore() == 5

def test_get_scoreboard():
    result = model.getScoreboard()
    falseResult = getScoreboard("abcdefghijk", "m")
    assert falseResult == "There is no scoreboard for this puzzle yet."
    assert isinstance(result, (pd.DataFrame, str))

def test_add_player():
    model.setPuzzle({"a", "b", "c", "d", "e", "f", "g"}, "a", 5, {"badge"}, {"badge"})
    randomName = model.getRandomWord()
    result = model.addPlayer(randomName)
    extendedRandomName = randomName + randomName + randomName + randomName + randomName
    result2 = model.addPlayer(extendedRandomName)
    assert result
    assert result2
    assert model.getScoreboard() != "There is no scoreboard for this puzzle yet."
    assert inScoreboard({"a", "b", "c", "d", "e", "f", "g"}, "a", randomName)
    assert inScoreboard({"a", "b", "c", "d", "e", "f", "g"}, "a", extendedRandomName[0:32])

def test_encrypted_data():
    assert isinstance(model.getEncryptedData, bytes)