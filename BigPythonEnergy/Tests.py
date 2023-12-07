import unittest
from Model import Model
from Puzzle import puzzle
from scoreboard import *
import pytest
import pandas as pd


class TestPuzzle(unittest.TestCase):

    model = None

    def setUp(self):
        self.model = Model()

    def test_puzzle_null(self):
        assert isinstance(self.model.getPuzzle(), puzzle)
        self.assertEqual(self.model.getPuzzle().isNotNull(), False)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), None)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), None)
        self.assertEqual(self.model.getPuzzle().getLetterList(), None)
        self.assertEqual(self.model.getPuzzle().getLetters(), None)
        self.assertEqual(self.model.getPuzzle().getNormalLetters(), None)
        self.assertEqual(self.model.getPuzzle().getSpecialLetter(), None)
        self.assertEqual(self.model.getPuzzle().getTotalScore(), None)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), None)
        self.assertEqual(self.model.getPuzzle().setFoundWord(), None)
        self.assertEqual(self.model.getPuzzle().addFoundWord(), None)
        self.assertEqual(self.model.getPuzzle().addScore(), None)
        self.assertEqual(self.model.getPuzzle().setScore(), None)
        self.assertEqual(self.model.getPuzzle().shuffleLetterList(), None)

    def test_puzzle_instantiation(self):
        letters = {"b", "r", "o", "m", "i", "n", "e"}
        specialLetter = "r"
        currentScore = 5
        foundWords = {"brine"}
        totalWords = {"brine"}
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
        self.model.setPuzzle(letters, specialLetter)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 0)
        self.assertEqual(self.model.getPuzzle().getFoundWordList(), set())
        self.assertEqual(self.model.getPuzzle().getTotalScore(), 743)
        self.assertEqual(self.model.getPuzzle().getTotalWordList(), {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"})
        
    def test_bingo_pangram_hints(self):
        bingo = self.model.getBingoHint()
        self.assertEqual(isinstance(bingo, str), True)
        self.assertEqual(self.model.getPangramNumbers(), [2, 1])

    def test_7_unique_letters(self):
        self.assertEqual(self.model.has_7_unique_letters("bromine"), True)
        self.assertEqual(self.model.has_7_unique_letters("merbromin"), True)
        self.assertEqual(self.model.has_7_unique_letters("dsa"), False)
        self.assertEqual(self.model.has_7_unique_letters(""), False)
        self.assertEqual(self.model.has_7_unique_letters("application"), False)

    def test_random_word(self):
        self.assertEqual(isinstance(self.model.getRandomWord(), str), True)
        self.assertEqual(len(set(self.model.getRandomWord())), 7)

    def test_valid_word_list(self):
        self.assertEqual(isinstance(self.model.getValidWordList(), set), True)
        self.assertEqual(self.model.getValidWordList(), {"moorier", "onerier", "romeo", "ribbie", "imbiber", "bireme", "brin", "reno", "boomier", "rimmer", "brinier", "birr", "roomier", "ronin", "bomber", "boron", "robbin", "miner", "renin", "emir", "bromo", "merrier", "ronion", "brrr", "bren", "nooner", "noniron", "borer", "erne", "niner", "remember", "robin", "ornerier", "ironer", "mooner", "brim", "broom", "emmer", "enrobe", "bier", "bonnier", "ribbier", "briber", "mere", "merino", "broo", "omber", "reborn", "berme", "bribe", "nobbier", "bore", "bree", "beer", "oorie", "berberin", "ionomer", "inner", "enorm", "brio", "merer", "brome", "bonier", "norm", "briner", "moonier", "iron", "brie", "berber", "mirier", "eerie", "miri", "morn", "moor", "moire", "monomer", "nori", "berberine", "mirin", "more", "brier", "rebore", "enrober", "morro", "ironmen", "broomier", "rimier", "ermine", "berm", "roomer", "minor", "brine", "inborn", "orbier", "omer", "ember", "inro", "boor", "noir", "irone", "bemire", "ribber", "bobber", "moron", "borne", "bibber", "renminbi", "robber", "beriberi", "merbromin", "bromin", "brimmer", "emeer", "ormer", "biner", "rebbe", "berime", "nonmember", "rein", "rime", "boomer", "mimer", "mobber", "bribee", "morrion", "mire", "mirror", "ribier", "beerier", "rimer", "robe", "morion", "born", "oribi", "boreen", "ribbon", "memoir", "roomie", "mermen", "error", "rennin", "ombre", "room", "eerier", "bromine", "member", "moreen", "rememberer", "boner"})
        
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

    def test_each_starting_with(self):
        self.assertEqual(isinstance(self.model.getEachStartingWith("br"), int), True)
        self.assertEqual(self.model.getEachStartingWith("br"), 22)

    def test_shuffle_letter_list(self):
        letterList = self.model.getPuzzle().getLetterList()
        self.model.shuffleLetterList()
        self.assertNotEqual(letterList, self.model.getPuzzle().getLetterList())
        self.assertEqual(set(letterList),set(self.model.getPuzzle().getLetterList()))

    def test_add_found_word(self):
        self.model.addFoundWord("boner")
        self.assertIn("boner", self.model.getPuzzle().getFoundWordList())
        self.model.addFoundWord("")
        self.assertNotIn("", self.model.getPuzzle().getFoundWordList())

    def test_add_score(self):
        self.model.getPuzzle().setScore(0)
        self.model.addScore(5)
        self.assertEqual(self.model.getPuzzle().getCurrentScore(), 5)

    def test_get_scoreboard(self):
        result = self.model.getScoreboard()
        falseResult = getScoreboard("abcdefghijk", "m")
        self.assertEqual(falseResult, "There is no scoreboard for this puzzle yet.")
        self.assertEqual(isinstance(result, (pd.DataFrame, str)), True)

    def test_add_player(self):
        self.model.setPuzzle({"a", "b", "c", "d", "e", "f", "g"}, "a", 5, {"badge"}, {"badge"})
        randomName = self.model.getRandomWord()
        result = self.model.addPlayer(randomName)
        extendedRandomName = randomName + randomName + randomName + randomName + randomName
        result2 = self.model.addPlayer(extendedRandomName)
        self.assertTrue(result)
        self.assertTrue(result2)
        self.assertNotEqual(self.model.getScoreboard(), "There is no scoreboard for this puzzle yet.")
        self.assertTrue(inScoreboard({"a", "b", "c", "d", "e", "f", "g"}, "a", randomName))
        self.assertTrue(inScoreboard({"a", "b", "c", "d", "e", "f", "g"}, "a", extendedRandomName[0:32]))

    def test_encrypted_data(self):
        self.assertTrue(isinstance(self.model.getEncryptedData, bytes))

if __name__ == '__main__':
    unittest.main()