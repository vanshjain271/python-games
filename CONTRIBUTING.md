# Contributing to Python Games

Thank you for your interest in contributing! This guide will help you get started.

## 📋 How to Contribute

### Adding a New Game

1. **Fork** the repository
2. **Create a new folder** with your game name (PascalCase, e.g., `MyNewGame/`)
3. **Structure your game** like this:
   ```
   MyNewGame/
   ├── main.py           # Entry point (required)
   ├── README.md         # Game instructions (required)
   └── other_modules.py  # Supporting files (optional)
   ```
4. **Add a README.md** in your game folder with:
   - Game description
   - How to run
   - Controls/gameplay instructions
   - Screenshots (optional but encouraged)
5. **Test your game** thoroughly
6. **Submit a Pull Request**

### Improving Existing Games

- Bug fixes are always welcome
- UI/UX improvements
- Performance optimizations
- Adding new features (discuss in an issue first)

### Reporting Bugs

Open an issue with:
- Game name
- What you expected to happen
- What actually happened
- Steps to reproduce
- Python version and OS

## 📝 Code Guidelines

### File Structure

- `main.py` should be the entry point for every game
- Use descriptive module names (e.g., `scoreboard.py`, `player.py`)
- Keep configuration/constants in a separate file (e.g., `config.py`)

### Code Style

- Follow **PEP 8** style guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Use type hints where helpful

### Imports

Use **absolute imports** within game folders:
```python
# ✅ Good - works when running from game folder
from config import COLORS
from player import Player

# ❌ Avoid - relative imports cause issues
from .config import COLORS
```

## 🎮 Game Requirements

- Must run with `python main.py` from the game folder
- Should use only Python standard library OR clearly document dependencies
- Include a `README.md` with instructions
- Should be family-friendly content

## 🧪 Testing Guidelines

All games must include tests to ensure code quality and stability.

### Test Structure

Add tests under the root `tests/` directory, mirroring the game's folder structure:
```
python-games/
├── BlackJack/
│   ├── main.py
│   └── accessories.py
├── tests/
│   └── BlackJack/
│       └── test_accessories.py
```

### Requirements

- New contributions **must include tests** for core game logic
- All tests must pass before a pull request is merged
- Use Python's built-in `unittest` or `pytest`

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run tests for a specific game
python -m pytest tests/BlackJack/
```

## 🚀 Pull Request Process

1. Ensure your code runs without errors
2. **Include tests** for core game logic under `tests/YourGame/`
3. **All tests must pass** - run `python -m pytest tests/`
4. Update the root README.md if adding a new game
5. Add your game's README.md with instructions
6. Submit PR with a clear description of changes

> ⚠️ **Pull requests without test files or with failing tests will not be accepted.**

## 💬 Questions?

Open an issue or start a discussion. We're happy to help!

---

**Happy coding! 🐍**
