# ArabPy - Write Python in Arabic

A professional Python library that allows writing Python code completely in Arabic while maintaining full compatibility with standard Python.

## Features

- **Comprehensive Translation Dictionary**: 500+ entries covering:
  - Python keywords (if, for, while, class, def, etc.)
  - Built-in functions (print, len, range, etc.)
  - Built-in exceptions (ValueError, TypeError, etc.)
  - Standard library modules (os, sys, math, json, etc.)
  - String, list, dict, set, and tuple methods
  - Math, random, time, and datetime functions
  - Regex, CSV, SQLite, and JSON helpers
  - Async/await syntax
  - Match/case syntax
  - Magic methods (__init__, __str__, etc.)
  - Decorators and context managers
  - And much more!

- **Tokenizer-Based Translation**: Preserves user-defined identifiers, strings, and comments
- **Bidirectional Translation**: Convert Python ↔ Arabic
- **Unicode Support**: Full support for Arabic identifiers
- **Easy to Extend**: Simply add more translations to the dictionary
- **Production Quality**: Clean, maintainable, well-tested code

## Installation

```bash
pip install arabpy
```

## Quick Start

### Translating Python to Arabic

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Python code
python_code = """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

for i in range(5):
    greet(f"User {i}")
"""

# Translate to Arabic
arabic_code = translator.to_arabic(python_code)
print(arabic_code)
```

Output:
```python
تعريف greet(name):
    إذا name:
        طباعة(f"Hello, {name}!")
    وإلا:
        طباعة("Hello, World!")

لكل i في مدى(5):
    greet(f"User {i}")
```

### Translating Arabic to Python

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Arabic code (with user-defined identifiers in Arabic)
arabic_code = """
تعريف جمع(أ، ب):
    إرجاع أ + ب

نتيجة = جمع(10، 20)
طباعة(نتيجة)
"""

# Translate back to Python
python_code = translator.to_python(arabic_code)
print(python_code)
```

Output:
```python
def sum(a, b):
    return a + b

result = sum(10, 20)
print(result)
```

### Executing Arabic Code

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Write and execute Arabic code
arabic_code = """
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)

طباعة(factorial(5))
"""

# Translate and execute
namespace = translator.translate_and_execute(arabic_code, to_arabic=True)
```

### Direct Arabic Code Execution

```python
from arabpy import arabic_code_runner

code = """
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)

طباعة(factorial(5))
"""

# Execute Arabic code directly
namespace = arabic_code_runner(code)
```

### File Translation

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Translate Python file to Arabic
translator.translate_file('script.py', 'script_arabic.py', to_arabic=True)

# Translate Arabic file back to Python
translator.translate_file('script_arabic.py', 'script_restored.py', to_arabic=False)
```

### Translation Statistics

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

stats = translator.get_translation_stats(python_code, to_arabic=True)
print(f"Total tokens: {stats['total_tokens']}")
print(f"Translated: {stats['translated_count']}")
print(f"Percentage: {stats['translation_percentage']:.1f}%")
```

## What Gets Translated

The translator converts Python language constructs and standard library identifiers while preserving:

- **User-defined variable names**: `my_var` stays `my_var`
- **User-defined function names**: `my_function` stays `my_function`
- **User-defined class names**: `MyClass` stays `MyClass`
- **String literals**: `"Hello"` stays `"Hello"`
- **Comments**: `# comment` stays `# comment`

What **does** get translated:
- Keywords: `if` → `إذا`, `for` → `لكل`, `def` → `تعريف`
- Built-in functions: `print` → `طباعة`, `len` → `طول`
- Standard library: `math.sqrt` → `جذر_تربيعي`
- Methods: `list.append` → `إضافة`
- Exceptions: `ValueError` → `خطأ_قيمة`
- Magic methods: `__init__` → `__تهيئة__`
- And 500+ more entries!

## Examples

### Basic Python Constructs

```python
# Python
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Arabic (keywords translated, user identifiers preserved)
إذا x > 0:
    طباعة("Positive")
وإلا_إذا x < 0:
    طباعة("Negative")
وإلا:
    طباعة("Zero")
```

### Loops

```python
# Python
for i in range(10):
    print(i)

while condition:
    do_something()

# Arabic (keywords translated, user identifiers preserved)
لكل i في مدى(10):
    طباعة(i)

بينما condition:
    do_something()
```

### Functions and Classes

```python
# Python
class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        return f"Hello, {self.name}"

# Arabic (keywords and magic methods translated, user identifiers preserved)
فئة Person:
    تعريف __تهيئة__(self, name):
        self.name = name
    
    تعريف greet(self):
        إرجاع f"Hello, {self.name}"
```

### List Operations

```python
# Python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.sort()
total = sum(numbers)

# Arabic (methods translated, user identifiers preserved)
numbers = [1, 2, 3, 4, 5]
numbers.إضافة(6)
numbers.ترتيب()
total = مجموع(numbers)
```

### Exception Handling

```python
# Python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Error: {e}")
finally:
    cleanup()

# Arabic (keywords and exceptions translated, user identifiers preserved)
جرب:
    result = risky_operation()
باستثناء خطأ_قيمة كـ e:
    طباعة(f"Error: {e}")
أخيرا:
    cleanup()
```

### Async/Await

```python
# Python
async def fetch_data():
    data = await api_call()
    return data

async with context:
    await process()

# Arabic (keywords translated, user identifiers preserved)
غير_متزامن تعريف fetch_data():
    data = انتظر api_call()
    إرجاع data

غير_متزامن مع context:
    انتظر process()
```

### Match/Case (Python 3.10+)

```python
# Python
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other")

# Arabic (keywords translated, user identifiers preserved)
طابق value:
    حالة 1:
        طباعة("One")
    حالة 2:
        طباعة("Two")
    حالة _:
        طباعة("Other")
```

## Extending the Dictionary

To add more translations, simply edit `arabpy/dictionary.py`:

```python
ARABIC_TRANSLATIONS = {
    # Add your custom translations here
    "my_function": "دالتي",
    "MyClass": "فئتي",
    # ...
}
```

The reverse mapping is automatically generated.

## How It Works

ArabPy uses Python's built-in tokenizer to:

1. Parse source code into tokens
2. Identify keywords, names, and operators
3. Translate only language constructs and library identifiers
4. Preserve user-defined identifiers, strings, and comments
5. Reconstruct the translated code

This approach ensures accurate translation without breaking user code.

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only Python standard library)

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Areas for improvement:

- Add more translations to the dictionary
- Improve tokenizer accuracy
- Add more test cases
- Enhance documentation
- Support for more Python features

## Acknowledgments

Built with the Python standard library's tokenizer module for accurate parsing and translation.

## Support

- GitHub Issues: https://github.com/arabpy/arabpy/
- Documentation: https://arabpy-docs.vercel.app/
