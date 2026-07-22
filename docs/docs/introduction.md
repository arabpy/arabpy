---
title: Introduction
description: ArabPy - Write Python in Arabic
sidebar_label: Introduction
slug: /
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Welcome to ArabPy

<div class="hero">
  <h1 class="hero__title">Write Python in Arabic</h1>
  <p class="hero__subtitle">A powerful Python library that enables writing Python code using Arabic keywords and syntax</p>
  <div class="hero__buttons">
    <a href="/docs/installation" class="hero__button hero__button--primary">Get Started</a>
    <a href="/docs/examples/index" class="hero__button hero__button--secondary">View Examples</a>
  </div>
</div>

## What is ArabPy?

ArabPy is a Python library that allows you to write Python code using Arabic keywords and syntax. It provides bidirectional translation between Python and Arabic, making programming more accessible to Arabic-speaking developers.

## Key Features

### 🔄 Bidirectional Translation
- Translate Python code to Arabic
- Translate Arabic code back to Python
- Perfect round-trip translation

### 📚 Comprehensive Dictionary
- 3,200+ Arabic translations for Python keywords
- Built-in functions, operators, and exceptions
- Standard library modules

### 🚀 Easy to Use
- Simple API for translation
- Direct code execution
- File translation support

### 🎯 Accurate Translation
- Tokenizer-based approach
- Preserves strings and comments
- Maintains code structure

## Quick Example

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet(name):
        if name:
            print(f"Hello, {name}!")
        else:
            print("Hello, World!")

    for i in range(5):
        greet(f"User {i}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet(name):
        إذا name:
            طباعة(f"Hello, {name}!")
        وإلا:
            طباعة("Hello, World!")

    لكل i في مدى(5):
        greet(f"User {i}")
    ```
  </TabItem>
</Tabs>

## Installation via PyPI

```bash
pip install arabpy
```

## Installation via GitHub

```bash
git clone https://github.com/arabpy/arabpy.git
cd arabpy
pip install -e .
```

## Basic Usage

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Python to Arabic
python_code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
"""

arabic_code = translator.to_arabic(python_code)
print(arabic_code)
```

## Why ArabPy?

### Accessibility
Makes programming accessible to millions of Arabic speakers who may find English keywords challenging.

### Education
Perfect for teaching programming in Arabic-speaking schools and universities.

### Localization
Enables full localization of Python applications for Arabic markets.

### Innovation
Pioneers Arabic programming language support in the Python ecosystem.

## Project Status

- **Version**: 1.0.0
- **License**: MIT
- **Python**: 3.8+
- **Status**: Stable and Production-Ready

## Badges

[![PyPI Version](https://img.shields.io/pypi/v/arabpy)](https://pypi.org/project/arabpy/)
[![Python Version](https://img.shields.io/pypi/pyversions/arabpy)](https://pypi.org/project/arabpy/)
[![License](https://img.shields.io/pypi/l/arabpy)](https://github.com/arabpy/arabpy/blob/main/LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/arabpy/arabpy)](https://github.com/arabpy/arabpy)

## Next Steps

- [Installation Guide](/docs/installation) - Get ArabPy installed on your system
- [Quick Start](/docs/quick-start) - Start using ArabPy in minutes
- [Examples](/docs/examples/index) - Explore code examples
- [API Reference](/docs/api/index) - Detailed API documentation

## Community

- [GitHub Repository](https://github.com/arabpy/arabpy)
- [Issues](https://github.com/arabpy/arabpy/issues)
- [Contributing](/docs/contributing)

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/arabpy/arabpy/issues) on GitHub.
