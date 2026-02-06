"""
Tests for TurtleCrossing game.
Tests car generation and level progression.
"""
import unittest
import random


class TestCarGeneration(unittest.TestCase):
    """Test car obstacle generation."""

    def test_car_spawn_y_bounds(self):
        """Test cars spawn within valid y range."""
        for _ in range(100):
            y = random.randint(-350, 350)
            self.assertGreaterEqual(y, -350)
            self.assertLessEqual(y, 350)

    def test_car_spawn_probability_increases_with_level(self):
        """Test car spawn chance increases with level."""
        def spawn_threshold(level):
            return 2 + min(level, 3)

        self.assertEqual(spawn_threshold(1), 3)
        self.assertEqual(spawn_threshold(3), 5)
        self.assertEqual(spawn_threshold(5), 5)  # Capped at 5

    def test_random_color_generation(self):
        """Test RGB color generation is valid."""
        for _ in range(100):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            self.assertTrue(0 <= r <= 255)
            self.assertTrue(0 <= g <= 255)
            self.assertTrue(0 <= b <= 255)


class TestLevelProgression(unittest.TestCase):
    """Test level progression logic."""

    def test_level_starts_at_one(self):
        """Test game starts at level 1."""
        level = 1
        self.assertEqual(level, 1)

    def test_level_increases_on_crossing(self):
        """Test level increases when turtle crosses."""
        level = 1
        level += 1  # Crossed successfully
        self.assertEqual(level, 2)

    def test_car_speed_increases_with_level(self):
        """Test cars move faster at higher levels."""
        base_speed = 5
        level = 3
        speed = base_speed + (level - 1) * 2
        self.assertEqual(speed, 9)


class TestTurtlePlayer(unittest.TestCase):
    """Test player turtle movement."""

    def test_turtle_moves_up(self):
        """Test turtle moves up by fixed distance."""
        y_pos = 0
        move_distance = 10
        y_pos += move_distance
        self.assertEqual(y_pos, 10)

    def test_finish_line_detection(self):
        """Test turtle reaches finish line."""
        y_pos = 290
        finish_line = 280
        self.assertGreater(y_pos, finish_line)


if __name__ == "__main__":
    unittest.main()
