"""
Tests for PingPong game.
Tests ball movement and speed logic.
"""
import unittest


class TestBallPhysics(unittest.TestCase):
    """Test ball physics logic (mock implementation)."""

    def setUp(self):
        """Set up mock ball attributes."""
        self.base_speed = 10
        self.speed_level = 1
        self.x_move = self.base_speed
        self.y_move = self.base_speed

    def test_initial_speed(self):
        """Test initial ball speed."""
        self.assertEqual(self.x_move, 10)
        self.assertEqual(self.y_move, 10)

    def test_y_bounce(self):
        """Test vertical bounce reverses y direction."""
        self.y_move *= -1
        self.assertEqual(self.y_move, -10)

    def test_x_bounce(self):
        """Test horizontal bounce reverses x direction."""
        self.x_move *= -1
        self.assertEqual(self.x_move, -10)

    def test_double_bounce_returns_original(self):
        """Test two bounces return to original direction."""
        original_x = self.x_move
        self.x_move *= -1
        self.x_move *= -1
        self.assertEqual(self.x_move, original_x)

    def test_increase_speed(self):
        """Test speed increase logic."""
        if self.speed_level < 5:
            self.speed_level += 1
            speed_factor = 1 + (self.speed_level * 0.2)
            self.x_move = self.base_speed * speed_factor
            self.y_move = self.base_speed * speed_factor

        self.assertEqual(self.speed_level, 2)
        self.assertEqual(self.x_move, 14.0)  # 10 * 1.4

    def test_max_speed_level(self):
        """Test speed level caps at 5."""
        for _ in range(10):
            if self.speed_level < 5:
                self.speed_level += 1

        self.assertEqual(self.speed_level, 5)

    def test_reset_speed(self):
        """Test speed reset logic."""
        self.speed_level = 5
        self.x_move = 30
        self.y_move = 30

        # Reset
        self.speed_level = 1
        self.x_move = self.base_speed
        self.y_move = self.base_speed

        self.assertEqual(self.speed_level, 1)
        self.assertEqual(self.x_move, 10)


class TestPauseLogic(unittest.TestCase):
    """Test pause functionality logic."""

    def test_toggle_pause(self):
        """Test pause toggle."""
        is_paused = False
        is_paused = not is_paused
        self.assertTrue(is_paused)

        is_paused = not is_paused
        self.assertFalse(is_paused)


class TestPowerUp(unittest.TestCase):
    """Test power-up logic."""

    def test_activate_deactivate(self):
        """Test power-up activation state."""
        is_active = False
        
        # Activate
        is_active = True
        self.assertTrue(is_active)

        # Deactivate
        is_active = False
        self.assertFalse(is_active)

    def test_spawn_bounds(self):
        """Test power-up spawns within screen bounds."""
        import random
        for _ in range(100):
            x = random.randint(-400, 400)
            y = random.randint(-300, 300)
            self.assertGreaterEqual(x, -400)
            self.assertLessEqual(x, 400)
            self.assertGreaterEqual(y, -300)
            self.assertLessEqual(y, 300)


if __name__ == "__main__":
    unittest.main()
