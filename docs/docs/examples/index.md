---
title: Examples
description: Comprehensive code examples for ArabPy
sidebar_label: Examples
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Examples

Comprehensive code examples demonstrating ArabPy's capabilities.

## Overview

These examples show how to use ArabPy for various Python programming constructs. Each example includes:

- **Arabic code** - Code written using Arabic keywords
- **Python code** - Equivalent Python code
- **Explanation** - What the code does
- **Expected output** - Result of execution

## Categories

- [Variables](/docs/examples/variables) - Variable assignment and types
- [Functions](/docs/examples/functions) - Function definitions and calls
- [Classes](/docs/examples/classes) - Class definitions and OOP
- [Loops](/docs/examples/loops) - For and while loops
- [Conditions](/docs/examples/conditions) - If statements and conditionals
- [Lists](/docs/examples/lists) - List operations and comprehensions
- [Dictionaries](/docs/examples/dictionaries) - Dictionary operations
- [Exceptions](/docs/examples/exceptions) - Exception handling
- [File Handling](/docs/examples/file-handling) - File I/O operations
- [OOP](/docs/examples/oop) - Object-oriented programming patterns
- [Decorators](/docs/examples/decorators) - Function decorators
- [Generators](/docs/examples/generators) - Generator functions
- [Context Managers](/docs/examples/context-managers) - With statements
- [Async/Await](/docs/examples/async-await) - Asynchronous programming
- [Dataclasses](/docs/examples/dataclasses) - Data class usage
- [Typing](/docs/examples/typing) - Type hints and annotations

## Quick Examples

### Hello World

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    print("Hello, World!")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    طباعة("Hello, World!")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, World!
```

**Explanation:** Basic print statement using Arabic keyword `طباعة` for `print`.

### Simple Function

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet(name):
        return f"Hello, {name}!"

    print(greet("ArabPy"))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet(name):
        إرجاع f"Hello, {name}!"

    طباعة(greet("ArabPy"))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, ArabPy!
```

**Explanation:** Function definition using `تعريف` for `def` and `إرجاع` for `return`.

### For Loop

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

**Output:**
```
0
1
2
3
4
```

**Explanation:** For loop using `لكل` for `for` and `مدى` for `range`.

### If Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    if x > 5:
        print("Greater than 5")
    else:
        print("Less than or equal to 5")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    إذا x > 5:
        طباعة("Greater than 5")
    وإلا:
        طباعة("Less than or equal to 5")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Greater than 5
```

**Explanation:** Conditional statement using `إذا` for `if` and `وإلا` for `else`.

## Running Examples

### Using ArabPyTranslator

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

arabic_code = '''
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)
'''

python_code = translator.to_python(arabic_code)
exec(python_code)
```

### Using arabic_code_runner

```python
from arabpy import arabic_code_runner

arabic_code = '''
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)

result = factorial(5)
'''

namespace = arabic_code_runner(arabic_code)
print(namespace['result'])  # Output: 120
```

## Best Practices

1. **Keep variable names in English** - Only keywords are translated
2. **Test your code** - Always verify translated code works correctly
3. **Use consistent indentation** - Indentation is preserved
4. **Add comments** - Comments are preserved during translation
5. **Check round-trip** - Verify Python → Arabic → Python translation

## Next Steps

Explore specific examples by category:

- [Variables](/docs/examples/variables) - Start with basic variables
- [Functions](/docs/examples/functions) - Learn function definitions
- [Loops](/docs/examples/loops) - Master iteration patterns
