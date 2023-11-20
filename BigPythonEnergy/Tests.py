import unittest
from Puzzle import puzzle
from DictInterface import *
import pytest

def test_has_7_unique_letters_returns_bool():
    word = "Bromine"
    result = has_7_unique_letters(word)
    assert isinstance(result, bool)

def test_has_7_unique_letters_with_valid_input():
    # Test with valid words that have 7 unique letters
    assert has_7_unique_letters("abcdefg") is True
    assert has_7_unique_letters("bromines") is False
    assert has_7_unique_letters("pythoni") is True

def test_has_7_unique_letters_with_invalid_input():
    # Test with words that do not have 7 unique letters
    assert has_7_unique_letters("hello") is False  # 4 unique letter
    assert has_7_unique_letters("abc") is False  # Less than 7 letters

def test_has_7_unique_letters_with_empty_input():
    # Test with an empty string
    assert has_7_unique_letters("") is False

def test_has_7_unique_letters_with_whitespace_input():
    # Test with a word containing whitespace
    assert has_7_unique_letters("        ") is False

def test_randomWord_returns_string():
    word = randomWord()
    assert isinstance(word, str)

def test_randomWord_returns_7_unique_letter_word():
    word = randomWord()
    assert len(set(word)) >= 7

def test_isValid_returns_bool():
    result = isValid("lump")
    assert isinstance(result, bool)

def test_findValid_returns_set():
    result = findValid('r','bromine' )
    assert isinstance(result, set)

class TestPuzzle(unittest.TestCase):
    
    def setUp(self):
        # Create a puzzle instance for testing.
        self.test_puzzle = puzzle(letters={'a', 'b', 'c', 'd', 'e', 'f', 'g'}, specialLetter='a', currentScore=0)

    def test_initialization(self):
        # Check if the puzzle is initialized correctly.
        self.assertEqual(self.test_puzzle.getLetterList(), ['a', 'b', 'c', 'd', 'e', 'f', 'g'])
        self.assertEqual(self.test_puzzle.getSpecialLetter(), 'a')
        self.assertEqual(self.test_puzzle.getCurrentScore(), 0)
        self.assertGreater(self.test_puzzle.getTotalScore(), 0)

    def test_score_calculation(self):
        # Check if score calculation works as expected.
        self.test_puzzle.addScore(5)
        self.assertEqual(self.test_puzzle.getCurrentScore(), 5)
        self.test_puzzle.addScore(7)
        self.assertEqual(self.test_puzzle.getCurrentScore(), 12)

    def test_found_words(self):
        # Check if found words are added and retrieved correctly.
        self.test_puzzle.addFoundWord("bad")
        self.test_puzzle.addFoundWord("cab")
        self.test_puzzle.addFoundWord("")
        found_words = self.test_puzzle.getFoundWordList()
        self.assertIn("bad", found_words)
        self.assertIn("cab", found_words)
        self.assertNotIn("dog", found_words)
        self.assertNotIn("", found_words)

    def test_puzzle_override(self):
        # Check if a puzzle can be overwritten successfully.
        self.test_puzzle = puzzle(letters={'c', 'd', 'e', 'g', 'r', 'p', 'z'}, specialLetter='r', currentScore=10)
        self.test_puzzle_old = puzzle(letters={'a', 'b', 'c', 'd', 'e', 'f', 'g'}, specialLetter='a', currentScore=0)
        self.assertEqual(self.test_puzzle.getLetterList(), ['c', 'd', 'e', 'g', 'r', 'p', 'z'])
        self.assertEqual(self.test_puzzle.getSpecialLetter(), 'r')
        self.assertEqual(self.test_puzzle.getCurrentScore(), 10)
        self.assertGreater(self.test_puzzle.getTotalScore(), 0)
        self.assertNotEqual(self.test_puzzle.getTotalScore(), self.test_puzzle_old.getTotalScore())

        self.assertIn(self.test_puzzle.getNormalLetters(), 'c')
        self.assertIn(self.test_puzzle.getNormalLetters(), 'd')
        self.assertIn(self.test_puzzle.getNormalLetters(), 'e')
        self.assertIn(self.test_puzzle.getNormalLetters(), 'g')
        self.assertIn(self.test_puzzle.getNormalLetters(), 'p')
        self.assertIn(self.test_puzzle.getNormalLetters(), 'z')
        self.assertNotIn(self.test_puzzle.getNormalLetters(), 'r')
        self.assertNotIn(self.test_puzzle.getNormalLetters(), 'b')

        self.assertIn(self.test_puzzle.letters, 'c')
        self.assertIn(self.test_puzzle.letters, 'd')
        self.assertIn(self.test_puzzle.letters, 'e')
        self.assertIn(self.test_puzzle.letters, 'g')
        self.assertIn(self.test_puzzle.letters, 'p')
        self.assertIn(self.test_puzzle.letters, 'z')
        self.assertNotIn(self.test_puzzle.letters, 'r')
        self.assertNotIn(self.test_puzzle.letters, 'b')

        self.assertEqual(self.test_puzzle.getFoundWordList(), set())

    def test_blank_puzzle(self):
        self.blank_puzzle = puzzle()
        self.assertEqual(self.blank_puzzle.getLetterList(), None)
        self.assertEqual(self.blank_puzzle.getSpecialLetter(), None)
        self.assertEqual(self.blank_puzzle.getCurrentScore(), None)
        self.assertEqual(self.blank_puzzle.getTotalScore(), None)
        self.assertEqual(self.blank_puzzle.getNormalLetters(), None)
        self.assertEqual(self.blank_puzzle.getLetters(), None)
        self.assertEqual(self.blank_puzzle.getFoundWordList(), None)

if __name__ == '__main__':
    unittest.main()
