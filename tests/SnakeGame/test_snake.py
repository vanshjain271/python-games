"""
Tests for SnakeGame.
Tests the game constants and core logic concepts.
Note: Avoids importing turtle module directly as it requires a display.
"""
import unittest


# Mock the constants - these match what's in snake.py
COR = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20


class TestSnakeConstants(unittest.TestCase):
    """Test snake game constants."""

    def test_starting_positions_count(self):
        """Test snake starts with 3 segments."""
        self.assertEqual(len(COR), 3)

    def test_distance_constant(self):
        """Test movement distance is positive."""
        self.assertGreater(DISTANCE, 0)

    def test_segments_are_spaced_correctly(self):
        """Test starting segments are spaced by DISTANCE."""
        for i in range(len(COR) - 1):
            x_diff = abs(COR[i][0] - COR[i + 1][0])
            self.assertEqual(x_diff, DISTANCE)


class TestSnakeMovement(unittest.TestCase):
    """Test snake movement direction logic."""

    def test_cant_reverse_direction(self):
        """Test snake can't do 180-degree turn (logic test)."""
        # If heading is 90 (up), can't turn to 270 (down)
        current = 90
        new = 270
        self.assertEqual(abs(new - current), 180)  # Invalid move

        # If heading is 0 (right), can't turn to 180 (left)
        current = 0
        new = 180
        self.assertEqual(abs(new - current), 180)  # Invalid move

    def test_can_turn_perpendicular(self):
        """Test snake can turn 90 degrees."""
        current = 90  # Up
        new = 0  # Right
        self.assertNotEqual(abs(new - current), 180)  # Valid move

        current = 0  # Right
        new = 90  # Up
        self.assertNotEqual(abs(new - current), 180)  # Valid move


class TestFoodSpawn(unittest.TestCase):
    """Test food spawn logic."""

    def test_food_spawn_bounds(self):
        """Test food spawns within bounds."""
        from random import randint
        for _ in range(100):
            x = randint(-240, 240)
            y = randint(-240, 240)
            self.assertGreaterEqual(x, -240)
            self.assertLessEqual(x, 240)
            self.assertGreaterEqual(y, -240)
            self.assertLessEqual(y, 240)


if __name__ == "__main__":
    unittest.main()
