---
title: FAQ
description: Frequently asked questions about ArabPy
sidebar_label: FAQ
---

# FAQ

Frequently asked questions about ArabPy.

## General Questions

### What is ArabPy?

ArabPy is a Python library that allows you to write Python code using Arabic keywords and syntax. It provides bidirectional translation between Python and Arabic, making programming more accessible to Arabic-speaking developers.

### Why use ArabPy?

ArabPy makes programming accessible to millions of Arabic speakers who may find English keywords challenging. It's perfect for:
- Teaching programming in Arabic
- Localizing applications for Arabic markets
- Preserving Arabic in technology
- Making code more readable for Arabic developers

### Is ArabPy production-ready?

Yes, ArabPy is stable and production-ready. It has comprehensive test coverage and is used in various educational and commercial projects.

## Installation and Setup

### How do I install ArabPy?

```bash
pip install arabpy
```

Or from source:

```bash
git clone https://github.com/arabpy/arabpy.git
cd arabpy
pip install -e .
```

### What are the requirements?

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

### Can I use ArabPy with other Python libraries?

Yes, ArabPy translates only Python keywords and built-in functions. It works seamlessly with all third-party libraries like numpy, pandas, django, etc.

## Usage

### How do I translate Python to Arabic?

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()
arabic_code = translator.to_arabic(python_code)
```

### How do I translate Arabic to Python?

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()
python_code = translator.to_python(arabic_code)
```

### How do I execute Arabic code directly?

```python
from arabpy import arabic_code_runner

namespace = arabic_code_runner(arabic_code)
```

### Are variable names translated?

No, only Python keywords and built-in functions are translated. Your variable names, function names, and class names remain unchanged.

### Are strings and comments preserved?

Yes, strings and comments are preserved exactly as written during translation.

## Translation

### What gets translated?

ArabPy translates:
- Python keywords (if, for, def, class, etc.)
- Built-in functions (print, len, range, etc.)
- Operators (and, or, not, in, is)
- Boolean values (True, False, None)
- Exception types
- Standard library modules

### What doesn't get translated?

ArabPy does not translate:
- User-defined variable names
- User-defined function names
- User-defined class names
- String literals
- Comments
- Third-party library names

### Is the translation reversible?

Yes, ArabPy provides bidirectional translation. You can translate Python to Arabic and back to Python with perfect round-trip capability for most code.

### How accurate is the translation?

ArabPy uses Python's tokenizer for accurate parsing, ensuring high translation accuracy. The translation preserves code structure, indentation, and logic.

## Features

### Does ArabPy support all Python features?

ArabPy supports most Python 3.8+ features including:
- Control flow (if, for, while)
- Functions and classes
- Exception handling
- Context managers
- Async/await
- List/dict comprehensions
- Type hints

Some advanced features may have limited support.

### Can I use ArabPy with Jupyter notebooks?

Yes, you can use ArabPy in Jupyter notebooks. Just import and use the translator or runner functions in your notebook cells.

### Does ArabPy work with Python 2?

No, ArabPy only supports Python 3.8 and above.

## Performance

### Is ArabPy fast?

ArabPy is optimized for performance. Translation operations are fast due to efficient dictionary lookups. For large files, the translation time is typically negligible compared to the overall development workflow.

### Does ArabPy affect runtime performance?

No, ArabPy only translates code. Once translated, the code runs at normal Python speed. There's no runtime overhead.

## Troubleshooting

### Translation fails with SyntaxError

This usually happens when the source code has syntax errors. Check your code syntax before translation.

### Arabic comma (،) causes errors

ArabPy automatically handles Arabic commas. If you encounter issues, ensure you're using the latest version.

### Variable names are being translated

This shouldn't happen. If it does, please report it as a bug. ArabPy only translates Python keywords and built-ins.

### Indentation is not preserved

ArabPy preserves indentation exactly. If you're seeing indentation issues, check your source code formatting.

## Contributing

### How can I contribute?

You can contribute by:
- Adding new translations to the dictionary
- Reporting bugs
- Improving documentation
- Submitting pull requests
- Sharing your use cases

See [Contributing](/docs/contributing) for more details.

### How do I add new translations?

Edit `arabpy/dictionary.py` and add entries in the format `{"python_term": "arabic_term"}`. Ensure bidirectional consistency.

### How do I report bugs?

Open an issue on GitHub with:
- A clear description of the problem
- Minimal code to reproduce
- Expected vs actual behavior
- Python version and ArabPy version

## License

### What license does ArabPy use?

ArabPy is released under the MIT License. See [License](/docs/license) for details.

### Can I use ArabPy commercially?

Yes, ArabPy is free for commercial use under the MIT License.

## Support

### Where can I get help?

- [GitHub Issues](https://github.com/arabpy/arabpy/issues)
- [Documentation](/docs/introduction)
- [Examples](/docs/examples/index)

### Is there a community forum?

Currently, we use GitHub Issues for discussions. Join the conversation there!

## Future

### What's planned for future versions?

See our [Roadmap](/docs/roadmap) for planned features and improvements.

### Will there be IDE support?

We're working on VS Code and PyCharm extensions for Arabic syntax highlighting and auto-completion.

### Will there be more library support?

We're expanding the dictionary to cover more third-party libraries. Contributions are welcome!

## Other

### Can I use ArabPy for teaching?

Absolutely! ArabPy is perfect for teaching programming in Arabic-speaking schools and universities.

### Is ArabPy suitable for beginners?

Yes, ArabPy makes Python more accessible to beginners who speak Arabic, reducing the language barrier to learning programming.

### Where can I find examples?

Check out our [Examples](/docs/examples/index) section for comprehensive code examples.

## Still have questions?

If your question isn't answered here, please:
1. Check the [Documentation](/docs/introduction)
2. Search [GitHub Issues](https://github.com/arabpy/arabpy/issues)
3. Open a new issue if needed
