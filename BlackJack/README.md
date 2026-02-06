# 🃏 BlackJack

A classic casino Blackjack game with a modern GUI built with Tkinter.

## 🎮 How to Run

```bash
cd BlackJack
python main.py
```

## 🕹️ How to Play

1. Click **Deal** to start a new round
2. Enter your bet amount
3. Try to get as close to 21 as possible without going over
4. Choose your action:
   - **Hit** - Take another card
   - **Stand** - End your turn
   - **Double Down** - Double your bet and take exactly one more card
   - **Split** - If you have two cards of the same rank, split into two hands

## 📏 Rules

- Face cards (J, Q, K) are worth 10
- Aces are worth 11 or 1 (automatically adjusted)
- Blackjack (Ace + 10-value card) pays 3:2
- Dealer must hit until 17 or higher
- Going over 21 = Bust (you lose)

## 📁 Files

- `main.py` - Main game logic and GUI
- `accessories.py` - Card, Deck, Hand, and Player classes
- `config.py` - Colors and constants

Enjoy! 🎰
