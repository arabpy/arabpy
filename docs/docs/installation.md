---
title: Installation
description: Install ArabPy on your system
sidebar_label: Installation
---

# Installation

Install ArabPy using pip or from source.

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

## Install via PyPI

The easiest way to install ArabPy is using pip:

```bash
pip install arabpy
```

## Install from GitHub

For the latest development version:

```bash
git clone https://github.com/arabpy/arabpy.git
cd arabpy
pip install -e .
```

## Verify Installation

Verify that ArabPy is installed correctly:

```bash
python -c "from arabpy import ArabPyTranslator; print('ArabPy installed successfully!')"
```

## Upgrade ArabPy

To upgrade to the latest version:

```bash
pip install --upgrade arabpy
```

## Uninstall ArabPy

To uninstall ArabPy:

```bash
pip uninstall arabpy
```

## Development Installation

For development purposes, install in editable mode with development dependencies:

```bash
git clone https://github.com/arabpy/arabpy.git
cd arabpy
pip install -e ".[dev]"
```

## Dependencies

ArabPy has no external dependencies and uses only the Python standard library:

- `tokenize` - For code tokenization
- `keyword` - For Python keyword detection
- `typing` - For type hints

## Platform Support

ArabPy supports:

- Windows
- macOS
- Linux
- Any platform with Python 3.8+

## Next Steps

After installation, proceed to the [Quick Start](/docs/quick-start) guide to begin using ArabPy.
