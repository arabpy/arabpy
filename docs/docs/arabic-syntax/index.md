---
title: Arabic Syntax
description: Learn Arabic Python syntax
sidebar_label: Arabic Syntax
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Arabic Syntax

Learn the Arabic syntax for Python programming constructs.

## Overview

ArabPy translates Python keywords and built-in functions to their Arabic equivalents while preserving your variable names, strings, and comments. This means you can write Python code using familiar Arabic terminology.

## Basic Syntax

### Variables

Variable names remain in English (or any language you prefer), only Python keywords are translated:

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    name = "ArabPy"
    version = 1.0
    is_active = True
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    name = "ArabPy"
    version = 1.0
    is_active = صحيح_قيمة
    ```
  </TabItem>
</Tabs>

### Functions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet(name):
        return f"Hello, {name}!"
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet(name):
        إرجاع f"Hello, {name}!"
    ```
  </TabItem>
</Tabs>

### Control Flow

#### If Statements

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    if x > 0:
        print("Positive")
    elif x < 0:
        print("Negative")
    else:
        print("Zero")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    إذا x > 0:
        طباعة("Positive")
    وإلا_إذا x < 0:
        طباعة("Negative")
    وإلا:
        طباعة("Zero")
    ```
  </TabItem>
</Tabs>

#### For Loops

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

#### While Loops

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    while x < 10:
        x += 1
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    بينما x < 10:
        x += 1
    ```
  </TabItem>
</Tabs>

### Classes

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            return f"Hello, {self.name}!"
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Person:
        تعريف __init__(self, name):
            self.name = name
        
        تعريف greet(self):
            إرجاع f"Hello, {self.name}!"
    ```
  </TabItem>
</Tabs>

### Exception Handling

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Cleanup")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء ZeroDivisionError:
        طباعة("Cannot divide by zero")
    أخيرا:
        طباعة("Cleanup")
    ```
  </TabItem>
</Tabs>

### Context Managers

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("file.txt", "r") as f:
        content = f.read()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("file.txt", "r") كـ f:
        content = f.read()
    ```
  </TabItem>
</Tabs>

## Built-in Functions

### Common Functions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    print("Hello")
    len([1, 2, 3])
    range(5)
    type(x)
    str(123)
    int("123")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    طباعة("Hello")
    طول([1, 2, 3])
    مدى(5)
    نوع(x)
    سلسلة(123)
    عدد_صحيح("123")
    ```
  </TabItem>
</Tabs>

## Operators

### Logical Operators

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    and
    or
    not
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    و
    أو
    ليس
    ```
  </TabItem>
</Tabs>

### Comparison Operators

Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) remain the same in both Python and Arabic code.

## Data Structures

### Lists

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [1, 2, 3]
    numbers.append(4)
    numbers.pop()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [1, 2, 3]
    numbers.إضافة(4)
    numbers.إزالة()
    ```
  </TabItem>
</Tabs>

### Dictionaries

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    data = {"key": "value"}
    data.get("key")
    data.keys()
    data.values()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    data = {"key": "value"}
    data.الحصول("key")
    data.المفاتيح()
    data.القيم()
    ```
  </TabItem>
</Tabs>

## Advanced Features

### Lambda Functions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    square = lambda x: x * 2
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    square = لامبدا x: x * 2
    ```
  </TabItem>
</Tabs>

### List Comprehensions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    squares = [x * 2 for x in range(5)]
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    squares = [x * 2 لكل x في مدى(5)]
    ```
  </TabItem>
</Tabs>

### Decorators

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    @decorator
    def function():
        pass
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    @مزخرف
    تعريف function():
        مرور
    ```
  </TabItem>
</Tabs>

## Best Practices

1. **Keep variable names in English** - Only Python keywords are translated
2. **Use comments in any language** - Comments are preserved during translation
3. **Test your code** - Always test translated code to ensure correctness
4. **Use consistent naming** - Follow Python naming conventions
5. **Document your code** - Add docstrings in your preferred language

## Next Steps

- [Arabic Keywords](/docs/arabic-syntax/keywords) - Complete keyword reference
- [Built-in Functions](/docs/arabic-syntax/built-in-functions) - All built-in functions
- [Modules](/docs/arabic-syntax/modules) - Standard library modules
- [Examples](/docs/examples/index) - Practical code examples
