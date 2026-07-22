---
title: Decorators
description: Function decorator examples
sidebar_label: Decorators
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Decorators

Examples of function decorators in ArabPy.

## Basic Decorators

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

### Decorator with Arguments

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned {result}")
            return result
        return wrapper

    @decorator
    def add(a, b):
        return a + b

    add(5, 3)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف decorator(func):
        تعريف wrapper(*args, **kwargs):
            طباعة(f"Calling {func.__name__}")
            result = func(*args, **kwargs)
            طباعة(f"{func.__name__} returned {result}")
            إرجاع result
        إرجاع wrapper

    @مزخرف
    تعريف add(a, b):
        إرجاع a + b

    add(5, 3)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Calling add
add returned 8
```

**Explanation:** Decorator that handles function arguments.

## Practical Decorators

### Timing Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import time

    def timer(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__} took {end - start:.4f} seconds")
            return result
        return wrapper

    @timer
    def slow_function():
        time.sleep(1)
        return "Done"

    slow_function()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد time

    تعريف timer(func):
        تعريف wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            طباعة(f"{func.__name__} took {end - start:.4f} seconds")
            إرجاع result
        إرجاع wrapper

    @timer
    تعريف slow_function():
        time.sleep(1)
        إرجاع "Done"

    slow_function()
    ```
  </TabItem>
</Tabs>

**Output:**
```
slow_function took 1.0000 seconds
```

**Explanation:** Decorator that measures function execution time.

### Logging Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def logger(func):
        def wrapper(*args, **kwargs):
            print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        return wrapper

    @logger
    def greet(name):
        return f"Hello, {name}!"

    greet("World")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف logger(func):
        تعريف wrapper(*args, **kwargs):
            طباعة(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            result = func(*args, **kwargs)
            طباعة(f"{func.__name__} returned: {result}")
            إرجاع result
        إرجاع wrapper

    @logger
    تعريف greet(name):
        إرجاع f"Hello, {name}!"

    greet("World")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Calling greet with args: ('World',), kwargs: {}
greet returned: Hello, World!
```

**Explanation:** Decorator that logs function calls.

## Decorators with Parameters

### Decorator Factory

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def repeat(times):
        def decorator(func):
            def wrapper(*args, **kwargs):
                for _ in range(times):
                    result = func(*args, **kwargs)
                return result
            return wrapper
        return decorator

    @repeat(3)
    def greet(name):
        print(f"Hello, {name}!")

    greet("World")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف repeat(times):
        تعريف decorator(func):
            تعريف wrapper(*args, **kwargs):
                لكل _ في مدى(times):
                    result = func(*args, **kwargs)
                إرجاع result
            إرجاع wrapper
        إرجاع decorator

    @repeat(3)
    تعريف greet(name):
        طباعة(f"Hello, {name}!")

    greet("World")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, World!
Hello, World!
Hello, World!
```

**Explanation:** Decorator factory that accepts parameters.

## Class Decorators

### Class as Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class CountCalls:
        def __init__(self, func):
            self.func = func
            self.count = 0
        
        def __call__(self, *args, **kwargs):
            self.count += 1
            print(f"Call {self.count} of {self.func.__name__}")
            return self.func(*args, **kwargs)

    @CountCalls
    def greet():
        print("Hello!")

    greet()
    greet()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة CountCalls:
        تعريف __init__(self, func):
            self.func = func
            self.count = 0
        
        تعريف __call__(self, *args, **kwargs):
            self.count += 1
            طباعة(f"Call {self.count} of {self.func.__name__}")
            إرجاع self.func(*args, **kwargs)

    @CountCalls
    تعريف greet():
        طباعة("Hello!")

    greet()
    greet()
    ```
  </TabItem>
</Tabs>

**Output:**
```
Call 1 of greet
Hello!
Call 2 of greet
Hello!
```

**Explanation:** Class-based decorator with state.

## Method Decorators

### Decorating Methods

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def method_decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"Method {func.__name__} called")
            return func(self, *args, **kwargs)
        return wrapper

    class MyClass:
        @method_decorator
        def my_method(self):
            return "Method executed"

    obj = MyClass()
    obj.my_method()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف method_decorator(func):
        تعريف wrapper(self, *args, **kwargs):
            طباعة(f"Method {func.__name__} called")
            إرجاع func(self, *args, **kwargs)
        إرجاع wrapper

    فئة MyClass:
        @method_decorator
        تعريف my_method(self):
            إرجاع "Method executed"

    obj = MyClass()
    obj.my_method()
    ```
  </TabItem>
</Tabs>

**Output:**
```
Method my_method called
```

**Explanation:** Decorator for instance methods.

## Built-in Decorators

### Property Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Circle:
        def __init__(self, radius):
            self._radius = radius
        
        @property
        def radius(self):
            return self._radius
        
        @radius.setter
        def radius(self, value):
            if value > 0:
                self._radius = value
        
        @property
        def area(self):
            return 3.14 * self._radius ** 2

    circle = Circle(5)
    print(f"Area: {circle.area}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Circle:
        تعريف __init__(self, radius):
            self._radius = radius
        
        @خاصية
        تعريف radius(self):
            إرجاع self._radius
        
        @radius.setter
        تعريف radius(self, value):
            إذا value > 0:
                self._radius = value
        
        @خاصية
        تعريف area(self):
            إرجاع 3.14 * self._radius ** 2

    circle = Circle(5)
    طباعة(f"Area: {circle.area}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Area: 78.5
```

**Explanation:** Built-in property decorator using `@خاصية` for `@property`.

### Static Method Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Math:
        @staticmethod
        def add(a, b):
            return a + b

    result = Math.add(5, 3)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Math:
        @طريقة_ثابتة
        تعريف add(a, b):
            إرجاع a + b

    result = Math.add(5, 3)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
8
```

**Explanation:** Static method decorator using `@طريقة_ثابتة` for `@staticmethod`.

### Class Method Decorator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Counter:
        count = 0
        
        @classmethod
        def get_count(cls):
            return cls.count
        
        @classmethod
        def increment(cls):
            cls.count += 1

    Counter.increment()
    print(Counter.get_count())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Counter:
        count = 0
        
        @طريقة_فئة
        تعريف get_count(cls):
            إرجاع cls.count
        
        @طريقة_فئة
        تعريف increment(cls):
            cls.count += 1

    Counter.increment()
    طباعة(Counter.get_count())
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
```

**Explanation:** Class method decorator using `@طريقة_فئة` for `@classmethod`.

## Next Steps

- [Generators](/docs/examples/generators) - Generator functions
- [Context Managers](/docs/examples/context-managers) - With statements
- [Async/Await](/docs/examples/async-await) - Asynchronous programming
