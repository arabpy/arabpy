---
title: arabic_code_runner
description: arabic_code_runner function API reference
sidebar_label: Runner
---

# arabic_code_runner

Execute Python code written in Arabic directly from a string.

## Function Definition

```python
from arabpy import arabic_code_runner

namespace = arabic_code_runner(source: str) -> Dict[str, Any]
```

## Parameters

- `source` (str): Arabic source code to execute

## Returns

- `Dict[str, Any]`: Execution namespace (globals dictionary) containing all variables and functions defined in the executed code

## Raises

- `TypeError`: If source is not a string
- `SyntaxError`: If translated code has syntax errors
- `RuntimeError`: If translation fails
- Exception: Any runtime errors during execution (with preserved traceback)

## Description

The `arabic_code_runner` function allows you to execute Python code written in Arabic directly. It:

1. Validates the input is a string
2. Translates Arabic code to Python using the translation engine
3. Compiles the translated Python code
4. Executes the compiled code
5. Returns the globals dictionary with all defined variables and functions

## Examples

### Basic Execution

```python
from arabpy import arabic_code_runner

code = '''
تعريف greet(name):
    إرجاع f"Hello, {name}!"

result = greet("ArabPy")
'''

namespace = arabic_code_runner(code)
print(namespace['result'])  # Output: Hello, ArabPy!
```

### Variable Assignment

```python
from arabpy import arabic_code_runner

code = '''
x = 10
y = 20
z = x + y
'''

namespace = arabic_code_runner(code)
print(namespace['z'])  # Output: 30
```

### Function Definition and Call

```python
from arabpy import arabic_code_runner

code = '''
تعريف factorial(n):
    إذا n <= 1:
        إرجاع 1
    وإلا:
        إرجاع n * factorial(n - 1)

result = factorial(5)
'''

namespace = arabic_code_runner(code)
print(namespace['result'])  # Output: 120
```

### Control Flow

```python
from arabpy import arabic_code_runner

code = '''
total = 0
لكل i في مدى(5):
    total = total + i
'''

namespace = arabic_code_runner(code)
print(namespace['total'])  # Output: 10
```

### Class Definition

```python
from arabpy import arabic_code_runner

code = '''
فئة Calculator:
    تعريف __init__(self):
        self.value = 0
    
    تعريف add(self, x):
        self.value = self.value + x
        إرجاع self.value

calc = Calculator()
result = calc.add(5)
'''

namespace = arabic_code_runner(code)
print(namespace['result'])  # Output: 5
```

## Error Handling

### Type Validation

```python
from arabpy import arabic_code_runner

try:
    arabic_code_runner(123)  # Not a string
except TypeError as e:
    print(f"Error: {e}")
```

### Syntax Errors

```python
from arabpy import arabic_code_runner

try:
    arabic_code_runner('تعريف func(:')  # Invalid syntax
except SyntaxError as e:
    print(f"Syntax error: {e}")
```

### Runtime Errors

```python
from arabpy import arabic_code_runner

try:
    arabic_code_runner('x = 1 / 0')  # Division by zero
except ZeroDivisionError as e:
    print(f"Runtime error: {e}")
```

## Features

### Input Validation

The function validates that the input is a string:

```python
from arabpy import arabic_code_runner

# This will raise TypeError
arabic_code_runner(123)
arabic_code_runner(None)
arabic_code_runner([])
```

### Traceback Preservation

Runtime errors preserve the original traceback for debugging:

```python
from arabpy import arabic_code_runner

code = '''
تعريف divide(a, b):
    إرجاع a / b

result = divide(10, 0)
'''

try:
    arabic_code_runner(code)
except ZeroDivisionError as e:
    # Full traceback is preserved
    print(e)
```

### UTF-8 Support

Full UTF-8 support for Arabic and Unicode strings:

```python
from arabpy import arabic_code_runner

code = '''
message = "مرحبا بالعالم"
name = "ArabPy"
'''

namespace = arabic_code_runner(code)
print(namespace['message'])  # Output: مرحبا بالعالم
```

### Indentation Preservation

Indentation is preserved exactly as written:

```python
from arabpy import arabic_code_runner

code = '''
تعريف nested():
    x = 1
        y = 2  # This will cause IndentationError
    إرجاع x
'''

# This will raise IndentationError with preserved context
```

### String and Comment Preservation

Strings and comments are not modified during translation:

```python
from arabpy import arabic_code_runner

code = '''
# This is a comment
x = "def"  # String with keyword
y = "if"
'''

namespace = arabic_code_runner(code)
print(namespace['x'])  # Output: def (not translated)
```

## Usage Patterns

### Simple Scripts

```python
from arabpy import arabic_code_runner

script = '''
# Calculate sum
total = 0
لكل i في مدى(10):
    total = total + i
طباعة(total)
'''

arabic_code_runner(script)
```

### Data Processing

```python
from arabpy import arabic_code_runner

code = '''
data = [1, 2, 3, 4, 5]
squared = [x * x لكل x في data]
'''

namespace = arabic_code_runner(code)
print(namespace['squared'])  # Output: [1, 4, 9, 16, 25]
```

### Multiple Functions

```python
from arabpy import arabic_code_runner

code = '''
تعريف add(a, b):
    إرجاع a + b

تعريف multiply(a, b):
    إرجاع a * b

result1 = add(5, 3)
result2 = multiply(5, 3)
'''

namespace = arabic_code_runner(code)
print(namespace['result1'])  # Output: 8
print(namespace['result2'])  # Output: 15
```

## Best Practices

1. **Always use strings** - The function only accepts string input
2. **Handle errors** - Wrap execution in try-except blocks
3. **Validate output** - Check the returned namespace for expected variables
4. **Test translations** - Verify code works before execution
5. **Use proper indentation** - Ensure consistent indentation in Arabic code

## Comparison with ArabPyTranslator

| Feature | arabic_code_runner | ArabPyTranslator |
|---------|-------------------|------------------|
| Execution | Yes | Optional |
| Returns | Namespace dictionary | Translated code string |
| Use Case | Running Arabic code | Translating code |
| Translation | Automatic | Manual |

## See Also

- [ArabPyTranslator](/docs/api/translator) - Translation engine
- [ARABIC_TRANSLATIONS](/docs/api/dictionary) - Translation dictionary
- [Examples](/docs/examples/index) - Code examples
