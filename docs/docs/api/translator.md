---
title: ArabPyTranslator
description: ArabPyTranslator class API reference
sidebar_label: Translator
---

# ArabPyTranslator

The main translation engine for bidirectional Python-Arabic code translation.

## Class Definition

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()
```

## Methods

### to_arabic(source: str) -> str

Translate Python code to Arabic.

**Parameters:**
- `source` (str): Python source code to translate

**Returns:**
- str: Translated Arabic code

**Raises:**
- `RuntimeError`: If translation fails

**Example:**

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

python_code = """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")
"""

arabic_code = translator.to_arabic(python_code)
print(arabic_code)
```

**Output:**
```python
تعريف greet(name):
    إذا name:
        طباعة(f"Hello, {name}!")
    وإلا:
        طباعة("Hello, World!")
```

### to_python(source: str) -> str

Translate Arabic code to Python.

**Parameters:**
- `source` (str): Arabic source code to translate

**Returns:**
- str: Translated Python code

**Raises:**
- `RuntimeError`: If translation fails

**Example:**

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

arabic_code = """
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)
"""

python_code = translator.to_python(arabic_code)
print(python_code)
```

**Output:**
```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```

### translate_file(input_path: str, output_path: str, to_arabic: bool = True) -> None

Translate a file from Python to Arabic or vice versa.

**Parameters:**
- `input_path` (str): Path to input file
- `output_path` (str): Path to output file
- `to_arabic` (bool): If True, translate Python to Arabic; if False, translate Arabic to Python

**Raises:**
- `FileNotFoundError`: If input file doesn't exist
- `RuntimeError`: If translation fails

**Example:**

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Python to Arabic
translator.translate_file('script.py', 'script_arabic.py', to_arabic=True)

# Arabic to Python
translator.translate_file('script_arabic.py', 'script_restored.py', to_arabic=False)
```

### translate_and_execute(source: str, to_arabic: bool = True) -> Dict[str, Any]

Translate and execute code, returning the execution namespace.

**Parameters:**
- `source` (str): Source code to translate and execute
- `to_arabic` (bool): If True, source is Python; if False, source is Arabic

**Returns:**
- Dict[str, Any]: Execution namespace (globals dictionary)

**Raises:**
- `RuntimeError`: If translation fails
- `SyntaxError`: If translated code has syntax errors
- Exception: Any runtime errors during execution

**Example:**

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

code = """
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)

طباعة(factorial(5))
"""

namespace = translator.translate_and_execute(code, to_arabic=False)
print(namespace)
```

### get_translation_stats(source: str, to_arabic: bool = True) -> Dict[str, Any]

Get translation statistics for the given source code.

**Parameters:**
- `source` (str): Source code to analyze
- `to_arabic` (bool): Translation direction

**Returns:**
- Dict[str, Any]: Statistics including:
  - `total_tokens`: Total number of tokens
  - `translated_count`: Number of translated tokens
  - `translation_percentage`: Percentage of tokens translated

**Example:**

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

code = """
def calculate(x, y):
    return x + y
"""

stats = translator.get_translation_stats(code, to_arabic=True)
print(f"Total tokens: {stats['total_tokens']}")
print(f"Translated: {stats['translated_count']}")
print(f"Percentage: {stats['translation_percentage']:.1f}%")
```

## Attributes

### ARABIC_TO_PYTHON: Dict[str, str]

Dictionary mapping Arabic keywords to Python keywords.

### PYTHON_TO_ARABIC: Dict[str, str]

Dictionary mapping Python keywords to Arabic keywords.

## Usage Patterns

### Basic Translation

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Python to Arabic
arabic = translator.to_arabic("def func(): pass")

# Arabic to Python
python = translator.to_python("تعريف func(): مرور")
```

### Batch Translation

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

files = ['file1.py', 'file2.py', 'file3.py']

for file in files:
    output = file.replace('.py', '_arabic.py')
    translator.translate_file(file, output, to_arabic=True)
```

### Translation with Validation

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

original = "def test(): return 42"
arabic = translator.to_arabic(original)
restored = translator.to_python(arabic)

# Verify round-trip
assert original == restored
```

## Notes

- The translator uses Python's tokenizer for accurate parsing
- Strings and comments are preserved during translation
- User-defined names (variables, functions, classes) are not translated
- Translation is bidirectional and reversible for most code

## See Also

- [arabic_code_runner](/docs/api/runner) - Direct code execution
- [ARABIC_TRANSLATIONS](/docs/api/dictionary) - Translation dictionary
