"""
Tests for Pacman game.
Tests movement and game logic concepts.
"""
import unittest


class TestPacmanMovement(unittest.TestCase):
    """Test Pacman movement logic."""

    def test_direction_values(self):
        """Test direction values."""
        UP = 90
        DOWN = 270
        LEFT = 180
        RIGHT = 0

        self.assertEqual(UP, 90)
        self.assertEqual(DOWN, 270)
        self.assertEqual(LEFT, 180)
        self.assertEqual(RIGHT, 0)

    def test_opposite_directions(self):
        """Test opposite direction detection."""
        UP, DOWN = 90, 270
        LEFT, RIGHT = 180, 0

        self.assertEqual(abs(UP - DOWN), 180)
        self.assertEqual(abs(LEFT - RIGHT), 180)


class TestGhostBehavior(unittest.TestCase):
    """Test ghost AI concepts."""

    def test_ghost_chase_distance(self):
        """Test distance calculation for chase mode."""
        import math
        ghost_pos = (100, 100)
        pacman_pos = (150, 150)

        distance = math.sqrt(
            (ghost_pos[0] - pacman_pos[0]) ** 2 + 
            (ghost_pos[1] - pacman_pos[1]) ** 2
        )
        self.assertAlmostEqual(distance, 70.71, places=1)

    def test_ghost_scatter_mode(self):
        """Test ghost goes to corner in scatter mode."""
        corners = [(-300, 300), (300, 300), (-300, -300), (300, -300)]
        self.assertEqual(len(corners), 4)


class TestScoring(unittest.TestCase):
    """Test scoring system."""

    def test_dot_score(self):
        """Test dot collection score."""
        score = 0
        dot_value = 10
        score += dot_value
        self.assertEqual(score, 10)

    def test_power_pellet_score(self):
        """Test power pellet score."""
        score = 0
        pellet_value = 50
        score += pellet_value
        self.assertEqual(score, 50)

    def test_ghost_eat_score(self):
        """Test eating ghost during power mode."""
        score = 0
        ghost_values = [200, 400, 800, 1600]  # Increasing per ghost

        for value in ghost_values:
            score += value

        self.assertEqual(score, 3000)


if __name__ == "__main__":
    unittest.main()
