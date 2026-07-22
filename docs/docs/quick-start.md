---
title: Quick Start
description: Get started with ArabPy in minutes
sidebar_label: Quick Start
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Quick Start

Get up and running with ArabPy in just a few minutes.

## Basic Translation

### Python to Arabic

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

### Arabic to Python

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

## Direct Code Execution

Execute Arabic code directly using `arabic_code_runner`:

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

namespace = arabic_code_runner(code)
```

## File Translation

Translate entire files:

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Translate Python file to Arabic
translator.translate_file('script.py', 'script_arabic.py', to_arabic=True)

# Translate Arabic file back to Python
translator.translate_file('script_arabic.py', 'script_restored.py', to_arabic=False)
```

## Translation Statistics

Get detailed translation statistics:

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

## Common Patterns

### Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    y = 3.14
    name = "ArabPy"
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    y = 3.14
    name = "ArabPy"
    ```
  </TabItem>
</Tabs>

### Functions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def add(a, b):
        return a + b
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف add(a, b):
        إرجاع a + b
    ```
  </TabItem>
</Tabs>

### Loops

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(5):
        print(i)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(5):
        طباعة(i)
    ```
  </TabItem>
</Tabs>

### Conditions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    if x > 0:
        print("Positive")
    else:
        print("Non-positive")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    إذا x > 0:
        طباعة("Positive")
    وإلا:
        طباعة("Non-positive")
    ```
  </TabItem>
</Tabs>

## Next Steps

- [Arabic Syntax](/docs/arabic-syntax/index) - Learn Arabic syntax in detail
- [Examples](/docs/examples/index) - Explore more code examples
- [API Reference](/docs/api/index) - Detailed API documentation
