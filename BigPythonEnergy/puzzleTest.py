import puzzle
import DictInterface
import string

class puzzleTest:
    score = 5

    def test_current_score(self):
        puzzle.setScore(self.score)
        assert puzzle.getCurrentScore() == 5

    def test_added_score():
        puzzle.addScore(6)
        assert puzzle.getCurrentScore() == 11

    # TODO: Initialize a value for total score and current
    #       score such that I can write tests to assert
    #       the appropriate english words pop up for the
    #       score percentage.

    testLetterList = []
    testLetterList.append("Foo")
    testLetterList.append("Bar")

    def test_initial_found_word_list(self):
        puzzle.setFoundWord(self.testLetterList)
        assert puzzle.getFoundWordList() == ["Foo", "Bar"]

    def test_added_to_found_word_list(self):
        puzzle.addFoundWord("Baz")
        assert puzzle.getFoundWordList() == ["Foo", "Bar", "Baz"]
