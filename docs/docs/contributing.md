---
title: Contributing
description: How to contribute to ArabPy
sidebar_label: Contributing
---

# Contributing

Thank you for your interest in contributing to ArabPy!

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of Python
- Understanding of Arabic language (for translations)

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/arabpy/arabpy.git
cd arabpy

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_translator.py

# Run with coverage
python -m pytest --cov=arabpy tests/
```

## Ways to Contribute

### Adding Translations

The most valuable contribution is expanding the translation dictionary.

#### Adding Single Translations

Edit `arabpy/dictionary.py`:

```python
ARABIC_TRANSLATIONS = {
    # ... existing translations
    "new_python_term": "new_arabic_term",
}
```

#### Adding Bidirectional Translations

Ensure both directions are added:

```python
ARABIC_TRANSLATIONS = {
    "python_term": "arabic_term",
    "arabic_term": "python_term",  # For reverse translation
}
```

#### Translation Guidelines

- Use standard Arabic terminology
- Keep translations concise
- Ensure consistency with existing translations
- Test translations with actual code
- Follow Python naming conventions for Arabic terms

### Reporting Bugs

When reporting bugs, please include:

1. **Clear description** of the problem
2. **Minimal code** to reproduce the issue
3. **Expected vs actual** behavior
4. **Python version** and ArabPy version
5. **Operating system**

Example bug report:

```markdown
**Issue**: Translation of `lambda` not working in list comprehension

**Code**:
```python
from arabpy import ArabPyTranslator
translator = ArabPyTranslator()
code = "[x * 2 for x in range(5)]"
print(translator.to_arabic(code))
```

**Expected**: `[x * 2 لكل x في مدى(5)]`
**Actual**: `[x * 2 for x in مدى(5)]`

**Versions**: Python 3.10, ArabPy 1.0.0
```

### Suggesting Features

We welcome feature suggestions! When suggesting:

1. Check if it's already requested in issues
2. Explain the use case clearly
3. Provide examples if possible
4. Consider implementation complexity

### Improving Documentation

Documentation improvements are always appreciated:

- Fix typos and grammar
- Add more examples
- Improve explanations
- Translate documentation to Arabic
- Add diagrams and visuals

### Code Contributions

#### Pull Request Process

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Ensure all tests pass
6. Submit a pull request

#### Branch Naming

Use descriptive branch names:

- `feature/add-numpy-translations`
- `fix/lambda-translation`
- `docs/improve-examples`
- `test/add-edge-cases`

#### Commit Messages

Follow conventional commits:

```
feat: add numpy module translations
fix: correct lambda translation in comprehensions
docs: improve quick start guide
test: add tests for async functions
```

## Development Guidelines

### Code Style

Follow PEP 8 style guidelines:

```bash
# Check code style
flake8 arabpy/

# Auto-format code
black arabpy/
```

### Testing

Write tests for all new features:

```python
import unittest
from arabpy import ArabPyTranslator

class TestNewFeature(unittest.TestCase):
    def test_translation(self):
        translator = ArabPyTranslator()
        result = translator.to_arabic("your code here")
        self.assertEqual(result, "expected translation")
```

### Documentation

Add docstrings to all public functions:

```python
def new_function(param: str) -> str:
    """
    Brief description of the function.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
        
    Example:
        >>> new_function("test")
        'result'
    """
    pass
```

## Project Structure

```
arabpy/
├── arabpy/
│   ├── __init__.py          # Package initialization
│   ├── translator.py        # Main translation engine
│   ├── runner.py           # Code execution
│   ├── dictionary.py       # Translation dictionary
│   └── dictionary_expanded.py  # Extended dictionary
├── tests/
│   ├── test_translator.py   # Translator tests
│   └── test_arabic_code_runner.py  # Runner tests
├── docs/                   # Documentation
├── examples/               # Example code
└── scripts/                # Utility scripts
```

## Translation Categories

### Priority Areas

We're prioritizing translations for:

1. **Data Science Libraries**
   - numpy, pandas, matplotlib
   - scikit-learn, tensorflow

2. **Web Frameworks**
   - django, flask, fastapi
   - requests, beautifulsoup

3. **Common Utilities**
   - datetime, json, re
   - os, pathlib, sys

### Adding Module Translations

For module-level translations:

```python
ARABIC_TRANSLATIONS = {
    "numpy": "نومباي",
    "numpy.array": "نومباي.مصفوفة",
    "numpy.zeros": "نومباي.أصفار",
}
```

## Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Assume good intentions

### Communication

- Use clear, professional language
- Be patient with language barriers
- Provide helpful feedback
- Acknowledge contributions

## Getting Help

### Questions?

- Check existing documentation
- Search GitHub issues
- Ask in discussions
- Contact maintainers

### Resources

- [Documentation](/docs/introduction)
- [API Reference](/docs/api/index)
- [Examples](/docs/examples/index)
- [GitHub Issues](https://github.com/arabpy/arabpy/issues)

## Recognition

Contributors will be acknowledged in:
- CONTRIBUTORS.md file
- Release notes
- Documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Thank You

Every contribution helps make ArabPy better for Arabic-speaking developers worldwide. Thank you for your support!
