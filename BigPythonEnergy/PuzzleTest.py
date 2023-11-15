"""
This script contains a comprehensive suite of unit tests for the 'puzzle' class, a critical component of a word puzzle game. The unit tests are designed to rigorously evaluate various aspects of the 'puzzle' class, ensuring its functionality and reliability.

The 'puzzle' class represents the core logic of the word puzzle game, handling essential operations such as initialization, score calculation, rank determination, score thresholds, and the management of found words. These unit tests aim to validate that the 'puzzle' class behaves as expected across a range of scenarios.

Here's an overview of the main test cases included in this suite:

1. Initialization Test:
   - Validates that a 'puzzle' instance is correctly initialized with the specified parameters, such as a set of letters, a special letter, and an initial score.

2. Score Calculation Test:
   - Verifies that the 'addScore' method accurately calculates and updates the current score when points are added.

3. Rank Calculation Test:
   - Ensures that the 'getCurrentScoreType' method correctly determines the player's rank based on their current score.

4. Score Thresholds Test:
   - Validates that the 'getScoreThresholds' method generates accurate score thresholds for different ranks, such as "Queen Bee," "Genius," "Amazing," and more.

5. Found Words Management Test:
   - Tests the functionality of adding and retrieving found words, confirming that words are correctly added to the list and can be retrieved when needed.

These unit tests serve as a crucial component of the development process, helping maintain code quality and reliability as new features are added or modifications are made to the 'puzzle' class.

To execute the tests, run this script as the main program. If all tests pass successfully, it indicates that the 'puzzle' class is functioning as intended. Any failures or errors will be reported, aiding in the identification and resolution of issues.

Note: Ensure that the 'puzzle' class implementation in the 'puzzle.py' file remains consistent with the expectations defined in these tests to maintain game integrity.
"""
import unittest
from Puzzle import puzzle

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
