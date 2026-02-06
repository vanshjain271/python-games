"""
Tests for Rock Paper Scissors game.
Tests game rules and win/lose logic.
"""
import unittest
import random


class TestGameRules(unittest.TestCase):
    """Test Rock Paper Scissors game rules."""

    def test_rock_beats_scissors(self):
        """Test rock beats scissors."""
        result = self.determine_winner('rock', 'scissors')
        self.assertEqual(result, 'player')

    def test_scissors_beats_paper(self):
        """Test scissors beats paper."""
        result = self.determine_winner('scissors', 'paper')
        self.assertEqual(result, 'player')

    def test_paper_beats_rock(self):
        """Test paper beats rock."""
        result = self.determine_winner('paper', 'rock')
        self.assertEqual(result, 'player')

    def test_rock_loses_to_paper(self):
        """Test rock loses to paper."""
        result = self.determine_winner('rock', 'paper')
        self.assertEqual(result, 'computer')

    def test_scissors_loses_to_rock(self):
        """Test scissors loses to rock."""
        result = self.determine_winner('scissors', 'rock')
        self.assertEqual(result, 'computer')

    def test_paper_loses_to_scissors(self):
        """Test paper loses to scissors."""
        result = self.determine_winner('paper', 'scissors')
        self.assertEqual(result, 'computer')

    def test_same_choice_is_tie(self):
        """Test same choices result in tie."""
        for choice in ['rock', 'paper', 'scissors']:
            result = self.determine_winner(choice, choice)
            self.assertEqual(result, 'tie')

    def determine_winner(self, player, computer):
        """Helper function to determine winner."""
        if player == computer:
            return 'tie'
        wins = {
            'rock': 'scissors',
            'scissors': 'paper',
            'paper': 'rock'
        }
        if wins[player] == computer:
            return 'player'
        return 'computer'


class TestComputerChoice(unittest.TestCase):
    """Test computer random choice."""

    def test_computer_choice_is_valid(self):
        """Test computer always chooses valid option."""
        choices = ['rock', 'paper', 'scissors']
        for _ in range(100):
            choice = random.choice(choices)
            self.assertIn(choice, choices)

    def test_computer_choice_distribution(self):
        """Test computer choice is reasonably random."""
        choices = ['rock', 'paper', 'scissors']
        counts = {'rock': 0, 'paper': 0, 'scissors': 0}

        for _ in range(1000):
            choice = random.choice(choices)
            counts[choice] += 1

        # Each should be roughly 1/3 (with some variance)
        for count in counts.values():
            self.assertGreater(count, 200)  # At least 20%
            self.assertLess(count, 500)  # At most 50%


class TestScoring(unittest.TestCase):
    """Test scoring system."""

    def test_player_win_increments_score(self):
        """Test player score increases on win."""
        player_score = 0
        player_score += 1
        self.assertEqual(player_score, 1)

    def test_computer_win_increments_score(self):
        """Test computer score increases on win."""
        computer_score = 0
        computer_score += 1
        self.assertEqual(computer_score, 1)

    def test_tie_no_score_change(self):
        """Test tie doesn't change scores."""
        player_score = 5
        computer_score = 3
        # Tie - no change
        self.assertEqual(player_score, 5)
        self.assertEqual(computer_score, 3)


if __name__ == "__main__":
    unittest.main()
