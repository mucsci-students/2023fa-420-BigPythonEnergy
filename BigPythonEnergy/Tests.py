import unittest
from Model import Model
from Puzzle import puzzle
from scoreboard import *
import pytest
import pandas as pd
from MainUI import MainUI


class TestModel(unittest.TestCase):

    # Sets up model with full puzzle for each test.
    def setUp(self):
        self.model = Model()
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        self.model.setPuzzle(letters, specialLetter)

    # Tests setting up model with an already created puzzle.
    def test_setup_with_puzzle(self):
        newPuzzle = puzzle({"b", "r", "o", "m", "i", "n", "e"})
        self.model = Model(newPuzzle)
        self.assertEqual(self.model.getPuzzle().getLetters(), {"b", "r", "o", "m", "i", "n", "e"})

    # Tests that a null puzzle returns None with every function except isNotNull(), which returns False
    def test_puzzle_null(self):
        self.model.setPuzzle()
        self.assertTrue(isinstance(self.model.getPuzzle(), puzzle))
        self.assertEqual(self.model.getPuzzle().isNotNull(), False)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), None)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), None)
        self.assertEqual(self.model.getPuzzle().getLetterList(), None)
        self.assertEqual(self.model.getPuzzle().getLetters(), None)
        self.assertEqual(self.model.getPuzzle().getNormalLetters(), None)
        self.assertEqual(self.model.getPuzzle().getSpecialLetter(), None)
        self.assertEqual(self.model.getPuzzle().getTotalScore(), None)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), None)
        self.assertEqual(self.model.getPuzzle().setFoundWord(set()), None)
        self.assertEqual(self.model.getPuzzle().addFoundWord("word"), None)
        self.assertEqual(self.model.getPuzzle().addScore(5), None)
        self.assertEqual(self.model.getPuzzle().setScore(5), None)
        self.assertEqual(self.model.getPuzzle().shuffleLetterList(), None)

    # Tests all aspects of puzzle creation and overwrite in the model.
    def test_puzzle_instantiation(self):
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        currentScore = 5
        foundWords = {"brine"}
        totalWords = {"brine"}

        # Puzzle with only letters and a special letter (created).
        self.model.setPuzzle(letters, specialLetter)
        self.assertEqual(self.model.getPuzzle().isNotNull(), True)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 0)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), set())
        self.assertEqual(set(self.model.getPuzzle().getLetterList()), letters)
        self.assertEqual(self.model.getPuzzle().getLetters(), letters)
        self.assertEqual(self.model.getPuzzle().getNormalLetters(), {"b", "o", "m", "i", "n", "e"})
        self.assertEqual(self.model.getPuzzle().getSpecialLetter(), "r")
        self.assertEqual(self.model.getPuzzle().getTotalScore(), 743)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"})

        # Puzzle with all parameters (loaded).
        self.model.setPuzzle(letters, specialLetter, currentScore, foundWords, totalWords)
        self.assertEqual(self.model.getPuzzle().isNotNull(), True)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 5)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), {"brine"})
        self.assertEqual(set(self.model.getPuzzle().getLetterList()), letters)
        self.assertEqual(self.model.getPuzzle().getLetters(), letters)
        self.assertEqual(self.model.getPuzzle().getNormalLetters(), {"b", "o", "m", "i", "n", "e"})
        self.assertEqual(self.model.getPuzzle().getSpecialLetter(), "r")
        self.assertEqual(self.model.getPuzzle().getTotalScore(), 5)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), {"brine"})

        # Puzzle with only letters (created with no special letter).
        self.model.setPuzzle(letters)
        self.assertTrue(isinstance(self.model.getPuzzle().getSpecialLetter(), str))
        self.model.getPuzzle().setFoundWord({"brine"})
        self.assertIn("brine", self.model.getPuzzle().getFoundWordList())

        # Puzzle overwrite test with original puzzle setup.
        self.model.setPuzzle(letters, specialLetter)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 0)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), set())
        self.assertEqual(self.model.getPuzzle().getTotalScore(), 743)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"})
        
    # Tests if bingo and pangram hints return correctly and in the right format.
    def test_bingo_pangram_hints(self):
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        self.model.setPuzzle(letters, specialLetter)
        bingo = self.model.getBingoHint()
        self.assertTrue(isinstance(bingo, list))
        self.assertEqual(self.model.getPangramNumbers(), [2, 1])

    # Tests each type of string input for having exactly 7 unique letters.
    def test_7_unique_letters(self):
        self.assertEqual(self.model.has_7_unique_letters("bromine"), True)
        self.assertEqual(self.model.has_7_unique_letters("merbromin"), True)
        self.assertEqual(self.model.has_7_unique_letters("dsa"), False)
        self.assertEqual(self.model.has_7_unique_letters(""), False)
        self.assertEqual(self.model.has_7_unique_letters("application"), False)

    # Tests creation of a random word and makes sure it has exactly 7 unique letters.
    def test_random_word(self):
        self.assertEqual(isinstance(self.model.getRandomWord(), str), True)
        self.assertEqual(len(set(self.model.getRandomWord())), 7)

    # Tests that the valid word list can be gotten properly.
    def test_valid_word_list(self):
        self.assertEqual(isinstance(self.model.getValidWordList(), set), True)
        self.assertEqual(self.model.getValidWordList(), {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"})
    
    # Tests each word length for words that should be in the dictionary, as well as word length limits and a word that is not in the dictionary.
    def test_is_valid(self):
        self.assertEqual(self.model.isValid("cats"), True)
        self.assertEqual(self.model.isValid("brine"), True)
        self.assertEqual(self.model.isValid("lovely"), True)
        self.assertEqual(self.model.isValid("bromine"), True)
        self.assertEqual(self.model.isValid("bitrates"), True)
        self.assertEqual(self.model.isValid("merbromin"), True)
        self.assertEqual(self.model.isValid("combusting"), True)
        self.assertEqual(self.model.isValid("contingency"), True)
        self.assertEqual(self.model.isValid("missionaries"), True)
        self.assertEqual(self.model.isValid("instantaneous"), True)
        self.assertEqual(self.model.isValid("parallelograms"), True)
        self.assertEqual(self.model.isValid("pharmacotherapy"), True)
        self.assertEqual(self.model.isValid("cat"), False)
        self.assertEqual(self.model.isValid(""), False)
        self.assertEqual(self.model.isValid("aaaaaa"), False)
        self.assertEqual(self.model.isValid("hippopotomonstrosesquippedaliophobia"), False)

    # Tests "first two letters" hint by checking an already-known puzzle by its exact first two letters and the type returned.
    def test_each_starting_with(self):
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        self.model.setPuzzle(letters, specialLetter)
        self.assertEqual(isinstance(self.model.getEachStartingWith("br"), int), True)
        self.assertEqual(self.model.getEachStartingWith("br"), 22)

    # Tests if letter list gets properly shuffled.
    def test_shuffle_letter_list(self):
        letterList = []
        for i in self.model.getPuzzle().getLetterList():
            letterList.append(i)
        self.model.shuffleLetterList()
        self.assertNotEqual(letterList, self.model.getPuzzle().getLetterList())
        self.assertEqual(set(letterList),set(self.model.getPuzzle().getLetterList()))

    # Tests if a word is added correctly by using a regular string and an empty string, the two different types of input.
    def test_add_found_word(self):
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        self.model.setPuzzle(letters, specialLetter)
        self.model.addFoundWord("boner")
        self.assertIn("boner", self.model.getPuzzle().getFoundWordList())
        self.model.addFoundWord("")
        self.assertNotIn("", self.model.getPuzzle().getFoundWordList())

    # Tests if scores are added correctly.
    def test_add_score(self):
        self.model.getPuzzle().setScore(0)
        self.model.addScore(5)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 5)

    # Tests if the scoreboard returns as a dataframe to string and tests the special return case for a game that has no scoreboard.
    def test_get_scoreboard(self):
        result = self.model.getScoreboard()
        falseResult = getScoreboard("abcdefghijk", "m")
        self.assertEqual(falseResult, "There is no scoreboard for this puzzle yet.")
        self.assertEqual(isinstance(result, (pd.DataFrame, str)), True)

    # Tests adding a player with both a regular name and a name >32 characters. Checks to make sure each was added correctly and that no random additions were made.
    def test_add_player(self):
        self.model.setPuzzle({"a", "b", "c", "d", "e", "f", "g"}, "a", 5, {"badge"}, {"badge"})
        randomName = self.model.getRandomWord()
        result = self.model.addPlayer(randomName)
        extendedRandomName = randomName + randomName + randomName + randomName + randomName
        result2 = self.model.addPlayer(extendedRandomName)
        self.assertTrue(result)
        self.assertTrue(result2)
        self.assertNotEqual(self.model.getScoreboard(), "There is no scoreboard for this puzzle yet.")
        self.assertTrue(inScoreboard("abcdefg", "a", randomName))
        self.assertTrue(inScoreboard("abcdefg", "a", extendedRandomName[0:32]))
        self.assertFalse(inScoreboard("abcdefg", "a", "bob33"))

    # Tests if the encrypted data is returned as bytes, the necessary format.
    def test_encrypted_data(self):
        self.assertTrue(isinstance(self.model.getEncryptedData(), bytes))

    # Tests all elements of the GUI controller.
    def test_gui_controller_elements(self):
        controller = MainUI()
        
        # Tests an empty puzzle.
        controller.model.setPuzzle()
        self.assertEqual(controller.submit("bromine"), "Start a puzzle from the 'new' menu first!")
        self.assertEqual(controller.saved("hi", True), "Please start a new puzzle before attempting to save!")
        self.assertEqual(controller.savedBlank("hi", True), "Please start a new puzzle before attempting to save!")

        # Tests that the random and single word starts work correctly.
        controller.random()
        self.assertTrue(controller.model.getPuzzle().isNotNull())
        controller.start("bromine")
        self.assertEqual(controller.model.getPuzzle().getLetters(), {"b", "r", "o", "m", "i", "n", "e"})

        # Tests that the word and special letter start is correct as well as its stored values.
        controller.start("bromine", "r")
        self.assertTrue(controller.model.getPuzzle().isNotNull())
        self.assertEqual(controller.model.getPuzzle().getSpecialLetter(), "r")
        self.assertEqual(controller.model.getPuzzle().getLetters(), {"b", "r", "o", "m", "i", "n", "e"})

        # Tests submission of words.
        self.assertEqual(controller.submit("brim"), "1")
        self.assertEqual(controller.submit("brine"), "5")
        self.assertEqual(controller.submit("bromine"), "14")
        self.assertEqual(controller.submit("biome"), "Not a valid word.")
        self.assertEqual(controller.submit("cats"), "Not a valid word.")
        
        # Tests valid letter checker for keyboard.
        self.assertFalse(controller.isNotValidLetter("b"))
        self.assertTrue(controller.isNotValidLetter("l"))

        # Tests return strings for saving.
        self.assertEqual(controller.saved("", True), "Not a valid save name.")
        self.assertEqual(controller.saved("H?", False), "Not a valid save name.")
        self.assertEqual(controller.saved("Test", False), "Saved successfully!")
        self.assertEqual(controller.savedBlank("", True), "Not a valid save name.")
        # self.assertEqual(controller.savedBlank("H/", False), "Not a valid save name.")
        self.assertEqual(controller.savedBlank("Test", False), "Saved successfully!")


if __name__ == '__main__':
    unittest.main()