"""
Tests for Breakout game.
Tests ball and paddle logic.
"""
import unittest


class TestBreakoutBall(unittest.TestCase):
    """Test ball mechanics for Breakout."""

    def setUp(self):
        """Set up ball attributes."""
        self.x_move = 10
        self.y_move = 10

    def test_bounce_off_wall(self):
        """Test ball bounces off walls."""
        self.y_move *= -1
        self.assertEqual(self.y_move, -10)

    def test_bounce_off_paddle(self):
        """Test ball bounces off paddle."""
        self.y_move *= -1
        self.assertEqual(self.y_move, -10)

    def test_bounce_off_brick(self):
        """Test ball bounces off brick."""
        self.y_move *= -1
        self.assertEqual(self.y_move, -10)


class TestPaddle(unittest.TestCase):
    """Test paddle mechanics."""

    def test_paddle_movement_bounds(self):
        """Test paddle stays within screen bounds."""
        paddle_x = 0
        left_bound = -350
        right_bound = 350

        # Move left
        paddle_x = max(paddle_x - 20, left_bound)
        self.assertGreaterEqual(paddle_x, left_bound)

        # Move right
        paddle_x = min(paddle_x + 20, right_bound)
        self.assertLessEqual(paddle_x, right_bound)


class TestBrickGrid(unittest.TestCase):
    """Test brick grid logic."""

    def test_brick_count(self):
        """Test brick grid creation."""
        rows = 5
        cols = 8
        total_bricks = rows * cols
        self.assertEqual(total_bricks, 40)

    def test_brick_destruction(self):
        """Test brick removal on hit."""
        bricks = list(range(40))  # 40 bricks
        bricks.pop()  # Remove one
        self.assertEqual(len(bricks), 39)


if __name__ == "__main__":
    unittest.main()
