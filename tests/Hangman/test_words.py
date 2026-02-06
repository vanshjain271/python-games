"""
Tests for Hangman game.
Tests the word list and word selection logic.
"""
import unittest
import sys
import os

# Add Hangman directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'Hangman'))

from words import word_list


class TestWordList(unittest.TestCase):
    """Test cases for word list."""

    def test_word_list_not_empty(self):
        """Test word list contains words."""
        self.assertGreater(len(word_list), 0)

    def test_all_words_are_strings(self):
        """Test all items in word list are strings."""
        for word in word_list:
            self.assertIsInstance(word, str)

    def test_all_words_lowercase(self):
        """Test all words are lowercase."""
        for word in word_list:
            self.assertEqual(word, word.lower(), f"Word '{word}' is not lowercase")

    def test_no_empty_words(self):
        """Test no empty strings in word list."""
        for word in word_list:
            self.assertGreater(len(word), 0)

    def test_no_duplicate_words(self):
        """Test no duplicate words in the list."""
        self.assertEqual(len(word_list), len(set(word_list)))

    def test_words_are_alphabetic(self):
        """Test all words contain only letters."""
        for word in word_list:
            self.assertTrue(word.isalpha(), f"Word '{word}' contains non-alphabetic characters")

    def test_minimum_word_length(self):
        """Test all words have reasonable length (at least 2 chars)."""
        for word in word_list:
            self.assertGreaterEqual(len(word), 2, f"Word '{word}' is too short")


class TestWordSelection(unittest.TestCase):
    """Test word selection logic."""

    def test_random_choice_returns_word(self):
        """Test random selection returns a word from the list."""
        import random
        word = random.choice(word_list)
        self.assertIn(word, word_list)

    def test_multiple_random_selections(self):
        """Test multiple random selections all return valid words."""
        import random
        for _ in range(100):
            word = random.choice(word_list)
            self.assertIn(word, word_list)


if __name__ == "__main__":
    unittest.main()
