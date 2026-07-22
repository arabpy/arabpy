---
title: Functions
description: Function definition and usage examples
sidebar_label: Functions
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Functions

Examples of function definitions and usage in ArabPy.

## Basic Functions

### Simple Function

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet():
        return "Hello, World!"

    message = greet()
    print(message)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet():
        إرجاع "Hello, World!"

    message = greet()
    طباعة(message)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, World!
```

**Explanation:** Simple function with no parameters using `تعريف` for `def` and `إرجاع` for `return`.

### Function with Parameters

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet(name):
        return f"Hello, {name}!"

    message = greet("ArabPy")
    print(message)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet(name):
        إرجاع f"Hello, {name}!"

    message = greet("ArabPy")
    طباعة(message)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, ArabPy!
```

**Explanation:** Function with a single parameter.

### Function with Multiple Parameters

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def add(a, b):
        return a + b

    result = add(10, 20)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف add(a, b):
        إرجاع a + b

    result = add(10, 20)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
30
```

**Explanation:** Function with multiple parameters performing addition.

### Function with Default Parameters

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    print(greet("World"))
    print(greet("World", "Hi"))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف greet(name, greeting="Hello"):
        إرجاع f"{greeting}, {name}!"

    طباعة(greet("World"))
    طباعة(greet("World", "Hi"))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, World!
Hi, World!
```

**Explanation:** Function with default parameter values.

## Advanced Functions

### Function with Return Types

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def calculate(x: int, y: int) -> int:
        return x * y

    result = calculate(5, 3)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف calculate(x: int, y: int) -> int:
        إرجاع x * y

    result = calculate(5, 3)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
15
```

**Explanation:** Function with type hints for parameters and return value.

### Recursive Function

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف factorial(n):
        إذا n <= 1:
            إرجاع 1
        وإلا:
            إرجاع n * factorial(n - 1)

    طباعة(factorial(5))
    ```
  </TabItem>
</Tabs>

**Output:**
```
120
```

**Explanation:** Recursive function to calculate factorial using `إذا` for `if` and `وإلا` for `else`.

### Function with Multiple Returns

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "F"

    print(get_grade(85))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف get_grade(score):
        إذا score >= 90:
            إرجاع "A"
        وإلا_إذا score >= 80:
            إرجاع "B"
        وإلا_إذا score >= 70:
            إرجاع "C"
        وإلا:
            إرجاع "F"

    طباعة(get_grade(85))
    ```
  </TabItem>
</Tabs>

**Output:**
```
B
```

**Explanation:** Function with multiple return statements using `وإلا_إذا` for `elif`.

### Function with Variable Arguments

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def sum_all(*args):
        return sum(args)

    result = sum_all(1, 2, 3, 4, 5)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف sum_all(*args):
        إرجاع مجموع(args)

    result = sum_all(1, 2, 3, 4, 5)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
15
```

**Explanation:** Function accepting variable number of arguments using `مجموع` for `sum`.

### Function with Keyword Arguments

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def create_person(name, age, city="Unknown"):
        return {"name": name, "age": age, "city": city}

    person = create_person("Ahmed", 30, "Cairo")
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف create_person(name, age, city="Unknown"):
        إرجاع {"name": name, "age": age, "city": city}

    person = create_person("Ahmed", 30, "Cairo")
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30, 'city': 'Cairo'}
```

**Explanation:** Function with keyword arguments returning a dictionary.

## Lambda Functions

### Simple Lambda

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    square = lambda x: x * 2
    print(square(5))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    square = لامبدا x: x * 2
    طباعة(square(5))
    ```
  </TabItem>
</Tabs>

**Output:**
```
10
```

**Explanation:** Lambda function using `لامبدا` for `lambda`.

### Lambda with Multiple Parameters

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    add = lambda a, b: a + b
    print(add(3, 4))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    add = لامبدا a, b: a + b
    طباعة(add(3, 4))
    ```
  </TabItem>
</Tabs>

**Output:**
```
7
```

**Explanation:** Lambda function with multiple parameters.

## Higher-Order Functions

### Function as Parameter

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def apply_operation(x, operation):
        return operation(x)

    result = apply_operation(5, lambda x: x * 2)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف apply_operation(x, operation):
        إرجاع operation(x)

    result = apply_operation(5, لامبدا x: x * 2)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
10
```

**Explanation:** Function accepting another function as parameter.

### Function Returning Function

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def make_multiplier(n):
        return lambda x: x * n

    double = make_multiplier(2)
    print(double(5))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف make_multiplier(n):
        إرجاع لامبدا x: x * n

    double = make_multiplier(2)
    طباعة(double(5))
    ```
  </TabItem>
</Tabs>

**Output:**
```
10
```

**Explanation:** Function that returns another function (closure).

## Function Decorators

### Simple Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def decorator(func):
        def wrapper():
            print("Before function")
            func()
            print("After function")
        return wrapper

    @decorator
    def say_hello():
        print("Hello!")

    say_hello()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف decorator(func):
        تعريف wrapper():
            طباعة("Before function")
            func()
            طباعة("After function")
        إرجاع wrapper

    @مزخرف
    تعريف say_hello():
        طباعة("Hello!")

    say_hello()
    ```
  </TabItem>
</Tabs>

**Output:**
```
Before function
Hello!
After function
```

**Explanation:** Simple decorator using `@مزخرف` for `@decorator`.

## Next Steps

- [Classes](/docs/examples/classes) - Learn about class definitions
- [Loops](/docs/examples/loops) - Explore iteration patterns
- [Decorators](/docs/examples/decorators) - Advanced decorator patterns
