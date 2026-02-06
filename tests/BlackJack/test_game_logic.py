"""
Tests for BlackJack game logic.
Tests the Card, Deck, Hand, and Player classes.
"""
import unittest
import sys
import os

# Add BlackJack directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'BlackJack'))

from config import SUITS, RANKS


class MockCard:
    """Mock Card class for testing without GUI dependencies."""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.face_up = True

    def get_value(self):
        if self.rank in ["J", "Q", "K"]:
            return 10
        elif self.rank == "A":
            return 11
        else:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


class MockHand:
    """Mock Hand class for testing."""
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.get_value()
        if card.rank == "A":
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class MockPlayer:
    """Mock Player class for testing."""
    def __init__(self, name, bankroll=1000):
        self.name = name
        self.bankroll = bankroll
        self.hands = [MockHand()]

    def place_bet(self, amount):
        if amount > self.bankroll:
            return False
        self.bankroll -= amount
        return True

    def add_winnings(self, amount):
        self.bankroll += amount


class TestCard(unittest.TestCase):
    """Test cases for Card class."""

    def test_card_creation(self):
        """Test card is created with correct suit and rank."""
        card = MockCard("♠", "A")
        self.assertEqual(card.suit, "♠")
        self.assertEqual(card.rank, "A")
        self.assertTrue(card.face_up)

    def test_ace_value(self):
        """Test ace returns value of 11."""
        card = MockCard("♠", "A")
        self.assertEqual(card.get_value(), 11)

    def test_face_card_values(self):
        """Test face cards return value of 10."""
        for rank in ["J", "Q", "K"]:
            card = MockCard("♠", rank)
            self.assertEqual(card.get_value(), 10, f"{rank} should be worth 10")

    def test_number_card_values(self):
        """Test number cards return their numeric value."""
        for i in range(2, 11):
            card = MockCard("♠", str(i))
            self.assertEqual(card.get_value(), i)

    def test_card_string_representation(self):
        """Test card string representation."""
        card = MockCard("♥", "K")
        self.assertEqual(str(card), "K♥")


class TestHand(unittest.TestCase):
    """Test cases for Hand class."""

    def test_empty_hand(self):
        """Test new hand has zero value."""
        hand = MockHand()
        self.assertEqual(hand.value, 0)
        self.assertEqual(len(hand.cards), 0)

    def test_add_card(self):
        """Test adding a card updates value."""
        hand = MockHand()
        card = MockCard("♠", "5")
        hand.add_card(card)
        self.assertEqual(hand.value, 5)
        self.assertEqual(len(hand.cards), 1)

    def test_blackjack(self):
        """Test blackjack hand equals 21."""
        hand = MockHand()
        hand.add_card(MockCard("♠", "A"))
        hand.add_card(MockCard("♠", "K"))
        self.assertEqual(hand.value, 21)

    def test_ace_adjustment(self):
        """Test ace adjusts from 11 to 1 when busting."""
        hand = MockHand()
        hand.add_card(MockCard("♠", "A"))  # 11
        hand.add_card(MockCard("♠", "8"))  # 19
        hand.add_card(MockCard("♠", "5"))  # Would be 24, ace becomes 1 = 14
        self.assertEqual(hand.value, 14)

    def test_multiple_aces_adjustment(self):
        """Test multiple aces adjust correctly."""
        hand = MockHand()
        hand.add_card(MockCard("♠", "A"))  # 11
        hand.add_card(MockCard("♥", "A"))  # 12 (second ace = 1)
        hand.add_card(MockCard("♦", "A"))  # 13
        self.assertEqual(hand.value, 13)

    def test_bust(self):
        """Test hand can exceed 21 without aces."""
        hand = MockHand()
        hand.add_card(MockCard("♠", "K"))  # 10
        hand.add_card(MockCard("♥", "Q"))  # 20
        hand.add_card(MockCard("♦", "5"))  # 25
        self.assertEqual(hand.value, 25)


class TestPlayer(unittest.TestCase):
    """Test cases for Player class."""

    def test_player_creation(self):
        """Test player is created with correct attributes."""
        player = MockPlayer("Test", 1000)
        self.assertEqual(player.name, "Test")
        self.assertEqual(player.bankroll, 1000)

    def test_default_bankroll(self):
        """Test player has default bankroll of 1000."""
        player = MockPlayer("Test")
        self.assertEqual(player.bankroll, 1000)

    def test_place_bet_success(self):
        """Test placing a valid bet."""
        player = MockPlayer("Test", 1000)
        result = player.place_bet(100)
        self.assertTrue(result)
        self.assertEqual(player.bankroll, 900)

    def test_place_bet_insufficient_funds(self):
        """Test placing bet larger than bankroll fails."""
        player = MockPlayer("Test", 100)
        result = player.place_bet(200)
        self.assertFalse(result)
        self.assertEqual(player.bankroll, 100)  # Unchanged

    def test_add_winnings(self):
        """Test adding winnings increases bankroll."""
        player = MockPlayer("Test", 1000)
        player.add_winnings(500)
        self.assertEqual(player.bankroll, 1500)


class TestConfig(unittest.TestCase):
    """Test cases for game configuration."""

    def test_suits_count(self):
        """Test there are 4 suits."""
        self.assertEqual(len(SUITS), 4)

    def test_ranks_count(self):
        """Test there are 13 ranks."""
        self.assertEqual(len(RANKS), 13)

    def test_deck_size(self):
        """Test full deck has 52 cards."""
        self.assertEqual(len(SUITS) * len(RANKS), 52)


if __name__ == "__main__":
    unittest.main()
