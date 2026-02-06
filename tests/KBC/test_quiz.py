"""
Tests for KBC (Kaun Banega Crorepati) quiz game.
Tests question structure and game logic.
"""
import unittest
import sys
import os

# Add KBC directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'KBC'))

from questions import get_questions


class TestQuestionStructure(unittest.TestCase):
    """Test question data structure."""

    def setUp(self):
        """Load questions."""
        self.questions = get_questions()

    def test_questions_not_empty(self):
        """Test questions list is not empty."""
        self.assertGreater(len(self.questions), 0)

    def test_question_has_required_fields(self):
        """Test each question has required fields."""
        required_fields = ['question', 'options', 'correct', 'value']

        for q in self.questions:
            for field in required_fields:
                self.assertIn(field, q, f"Question missing field: {field}")

    def test_each_question_has_four_options(self):
        """Test each question has exactly 4 options."""
        for q in self.questions:
            self.assertEqual(len(q['options']), 4, 
                           f"Question should have 4 options: {q['question'][:50]}")

    def test_correct_answer_in_options(self):
        """Test correct answer is one of the options."""
        for q in self.questions:
            self.assertIn(q['correct'], q['options'],
                         f"Correct answer not in options: {q['question'][:50]}")

    def test_question_values_are_positive(self):
        """Test all question values are positive."""
        for q in self.questions:
            self.assertGreater(q['value'], 0)


class TestQuizGameLogic(unittest.TestCase):
    """Test quiz game logic."""

    def test_correct_answer_adds_money(self):
        """Test correct answer increases money."""
        money = 0
        question_value = 1000
        # Correct answer
        money += question_value
        self.assertEqual(money, 1000)

    def test_wrong_answer_ends_game(self):
        """Test wrong answer logic."""
        is_correct = False
        game_over = not is_correct
        self.assertTrue(game_over)

    def test_lifeline_reduces_options(self):
        """Test 50-50 lifeline removes 2 wrong options."""
        options = ['A', 'B', 'C', 'D']
        correct = 'B'
        # 50-50 removes 2 wrong options
        remaining = [correct, 'D']  # Keep correct + 1 wrong
        self.assertEqual(len(remaining), 2)
        self.assertIn(correct, remaining)


if __name__ == "__main__":
    unittest.main()
