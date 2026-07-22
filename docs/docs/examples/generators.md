---
title: Generators
description: Generator function examples
sidebar_label: Generators
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Generators

Examples of generator functions in ArabPy.

## Basic Generators

### Simple Generator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def count_up_to(max):
        count = 1
        while count <= max:
            yield count
            count += 1

    for num in count_up_to(5):
        print(num)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف count_up_to(max):
        count = 1
        بينما count <= max:
            إنتاج count
            count += 1

    لكل num في count_up_to(5):
        طباعة(num)
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
2
3
4
5
```

**Explanation:** Simple generator using `إنتاج` for `yield`.

### Generator Expression

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    squares = (x * x for x in range(5))
    for square in squares:
        print(square)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    squares = (x * x لكل x في مدى(5))
    لكل square في squares:
        طباعة(square)
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
1
4
9
16
```

**Explanation:** Generator expression using parentheses.

## Generator Methods

### Send Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def accumulator():
        total = 0
        while True:
            value = yield total
            if value is not None:
                total += value

    acc = accumulator()
    next(acc)
    print(acc.send(10))
    print(acc.send(20))
    print(acc.send(30))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف accumulator():
        total = 0
        بينما صحيح_قيمة:
            value = إنتاج total
            إذا value ليس هو None:
                total += value

    acc = accumulator()
    التالي(acc)
    طباعة(acc.إرسال(10))
    طباعة(acc.إرسال(20))
    طباعة(acc.إرسال(30))
    ```
  </TabItem>
</Tabs>

**Output:**
```
10
30
60
```

**Explanation:** Generator with send method using `إرسال` for `send`.

### Throw Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def my_generator():
        try:
            yield 1
            yield 2
        except ValueError:
            yield "Error caught"

    gen = my_generator()
    print(next(gen))
    print(gen.throw(ValueError))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف my_generator():
        جرب:
            إنتاج 1
            إنتاج 2
        باستثناء ValueError:
            إنتاج "Error caught"

    gen = my_generator()
    طباعة(التالي(gen))
    طباعة(gen.رمي(ValueError))
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
Error caught
```

**Explanation:** Generator with throw method using `رمي` for `throw`.

### Close Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def my_generator():
        try:
            yield 1
            yield 2
            yield 3
        finally:
            print("Generator closed")

    gen = my_generator()
    print(next(gen))
    gen.close()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف my_generator():
        جرب:
            إنتاج 1
            إنتاج 2
            إنتاج 3
        أخيرا:
            طباعة("Generator closed")

    gen = my_generator()
    طباعة(التالي(gen))
    gen.إغلاق()
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
Generator closed
```

**Explanation:** Generator with close method using `إغلاق` for `close`.

## Practical Generators

### Infinite Generator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def infinite_counter():
        count = 0
        while True:
            yield count
            count += 1

    counter = infinite_counter()
    for i in range(5):
        print(next(counter))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف infinite_counter():
        count = 0
        بينما صحيح_قيمة:
            إنتاج count
            count += 1

    counter = infinite_counter()
    لكل i في مدى(5):
        طباعة(التالي(counter))
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

**Explanation:** Infinite generator with manual termination.

### File Line Generator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def read_lines(filename):
        with open(filename, "r") as f:
            for line in f:
                yield line.strip()

    # Usage
    for line in read_lines("example.txt"):
        print(line)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف read_lines(filename):
        مع open(filename, "r") كـ f:
            لكل line في f:
                إنتاج line.strip()

    # Usage
    لكل line في read_lines("example.txt"):
        طباعة(line)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Line 1
Line 2
Line 3
```

**Explanation:** Generator for reading file lines lazily.

### Fibonacci Generator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def fibonacci():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b

    fib = fibonacci()
    for i in range(10):
        print(next(fib))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف fibonacci():
        a, b = 0, 1
        بينما صحيح_قيمة:
            إنتاج a
            a, b = b, a + b

    fib = fibonacci()
    لكل i في مدى(10):
        طباعة(التالي(fib))
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
1
1
2
3
5
8
13
21
34
```

**Explanation:** Fibonacci sequence generator.

## Generator Pipelines

### Chaining Generators

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def numbers():
        for i in range(10):
            yield i

    def squares(gen):
        for num in gen:
            yield num * num

    def evens(gen):
        for num in gen:
            if num % 2 == 0:
                yield num

    result = evens(squares(numbers()))
    for num in result:
        print(num)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف numbers():
        لكل i في مدى(10):
            إنتاج i

    تعريف squares(gen):
        لكل num في gen:
            إنتاج num * num

    تعريف evens(gen):
        لكل num في gen:
            إذا num % 2 == 0:
                إنتاج num

    result = evens(squares(numbers()))
    لكل num في result:
        طباعة(num)
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
4
16
36
64
```

**Explanation:** Chaining multiple generators together.

## Next Steps

- [Context Managers](/docs/examples/context-managers) - With statements
- [Async/Await](/docs/examples/async-await) - Asynchronous programming
- [Dataclasses](/docs/examples/dataclasses) - Data class usage
