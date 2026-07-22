---
title: Variables
description: Variable assignment and type examples
sidebar_label: Variables
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Variables

Examples of variable assignment and different data types in ArabPy.

## Basic Assignment

### Integer Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    y = 20
    z = x + y
    print(z)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    y = 20
    z = x + y
    طباعة(z)
    ```
  </TabItem>
</Tabs>

**Output:**
```
30
```

**Explanation:** Basic integer arithmetic. Variable names remain in English, only keywords are translated.

### Float Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    price = 19.99
    tax = 0.08
    total = price * (1 + tax)
    print(f"Total: ${total:.2f}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    price = 19.99
    tax = 0.08
    total = price * (1 + tax)
    طباعة(f"Total: ${total:.2f}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Total: $21.59
```

**Explanation:** Floating-point arithmetic with formatted output.

### String Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    name = "ArabPy"
    version = "1.0.0"
    message = f"{name} version {version}"
    print(message)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    name = "ArabPy"
    version = "1.0.0"
    message = f"{name} version {version}"
    طباعة(message)
    ```
  </TabItem>
</Tabs>

**Output:**
```
ArabPy version 1.0.0
```

**Explanation:** String variables with f-string formatting.

### Boolean Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    is_active = True
    is_admin = False
    print(f"Active: {is_active}")
    print(f"Admin: {is_admin}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    is_active = صحيح_قيمة
    is_admin = خطأ
    طباعة(f"Active: {is_active}")
    طباعة(f"Admin: {is_admin}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Active: True
Admin: False
```

**Explanation:** Boolean values using `صحيح_قيمة` for `True` and `خطأ` for `False`.

### None Value

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    result = None
    if result is None:
        print("No result")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    result = لاشيء
    إذا result هو لاشيء:
        طباعة("No result")
    ```
  </TabItem>
</Tabs>

**Output:**
```
No result
```

**Explanation:** None value using `لاشيء` for `None`.

## Type Conversion

### String to Integer

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    num_str = "42"
    num = int(num_str)
    print(f"Number: {num}")
    print(f"Type: {type(num)}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    num_str = "42"
    num = عدد_صحيح(num_str)
    طباعة(f"Number: {num}")
    طباعة(f"Type: {نوع(num)}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Number: 42
Type: <class 'int'>
```

**Explanation:** Converting string to integer using `عدد_صحيح` for `int`.

### String to Float

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    pi_str = "3.14159"
    pi = float(pi_str)
    print(f"Pi: {pi}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    pi_str = "3.14159"
    pi = عدد_عشري(pi_str)
    طباعة(f"Pi: {pi}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Pi: 3.14159
```

**Explanation:** Converting string to float using `عدد_عشري` for `float`.

### Number to String

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    age = 25
    age_str = str(age)
    message = "Age: " + age_str
    print(message)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    age = 25
    age_str = سلسلة(age)
    message = "Age: " + age_str
    طباعة(message)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Age: 25
```

**Explanation:** Converting number to string using `سلسلة` for `str`.

## Multiple Assignment

### Tuple Unpacking

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x, y, z = 1, 2, 3
    print(f"x={x}, y={y}, z={z}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x, y, z = 1, 2, 3
    طباعة(f"x={x}, y={y}, z={z}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x=1, y=2, z=3
```

**Explanation:** Multiple variable assignment using tuple unpacking.

### Swap Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    a = 5
    b = 10
    a, b = b, a
    print(f"a={a}, b={b}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    a = 5
    b = 10
    a, b = b, a
    طباعة(f"a={a}, b={b}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
a=10, b=5
```

**Explanation:** Swapping variables using tuple unpacking.

## Complex Variables

### List Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [1, 2, 3, 4, 5]
    print(f"List: {numbers}")
    print(f"Length: {len(numbers)}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [1, 2, 3, 4, 5]
    طباعة(f"List: {numbers}")
    طباعة(f"Length: {طول(numbers)}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
List: [1, 2, 3, 4, 5]
Length: 5
```

**Explanation:** List variable with length check using `طول` for `len`.

### Dictionary Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    طباعة(f"Name: {person['name']}")
    طباعة(f"Age: {person['age']}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Name: Ahmed
Age: 30
```

**Explanation:** Dictionary variable with key access.

## Variable Operations

### Increment

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    counter = 0
    counter += 1
    print(f"Counter: {counter}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    counter = 0
    counter += 1
    طباعة(f"Counter: {counter}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Counter: 1
```

**Explanation:** Incrementing a variable using augmented assignment.

### String Concatenation

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    first = "Hello"
    second = "World"
    greeting = first + " " + second
    print(greeting)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    first = "Hello"
    second = "World"
    greeting = first + " " + second
    طباعة(greeting)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello World
```

**Explanation:** String concatenation using the `+` operator.

## Type Checking

### Check Variable Type

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 42
    if isinstance(x, int):
        print("x is an integer")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 42
    إذا هو_مثيل(x, int):
        طباعة("x is an integer")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x is an integer
```

**Explanation:** Type checking using `هو_مثيل` for `isinstance`.

## Next Steps

- [Functions](/docs/examples/functions) - Learn about function definitions
- [Lists](/docs/examples/lists) - Explore list operations
- [Dictionaries](/docs/examples/dictionaries) - Learn dictionary usage
