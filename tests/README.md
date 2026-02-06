# Tests Directory

This directory contains unit tests for all games in the repository.

## Running Tests

```bash
# Install pytest (if not already installed)
pip install pytest

# Run all tests
python -m pytest tests/

# Run tests for a specific game
python -m pytest tests/BlackJack/

# Run with verbose output
python -m pytest tests/ -v
```

## Test Structure

Each game has its own subdirectory with test files:
```
tests/
├── BlackJack/
│   └── test_game_logic.py
├── SnakeGame/
│   └── test_snake.py
├── Hangman/
│   └── test_words.py
...
```
