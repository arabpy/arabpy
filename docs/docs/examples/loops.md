---
title: Loops
description: Loop iteration examples
sidebar_label: Loops
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Loops

Examples of loop iteration in ArabPy.

## For Loops

### Basic For Loop

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

**Explanation:** Basic for loop using `لكل` for `for` and `مدى` for `range`.

### For Loop with List

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    لكل fruit في fruits:
        طباعة(fruit)
    ```
  </TabItem>
</Tabs>

**Output:**
```
apple
banana
cherry
```

**Explanation:** Iterating over a list.

### For Loop with Range Steps

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(0, 10, 2):
        print(i)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(0, 10, 2):
        طباعة(i)
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
2
4
6
8
```

**Explanation:** For loop with step parameter.

### For Loop with Enumerate

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    لكل index, fruit في تعداد(fruits):
        طباعة(f"{index}: {fruit}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
0: apple
1: banana
2: cherry
```

**Explanation:** For loop with index using `تعداد` for `enumerate`.

### Nested For Loops

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(3):
        for j in range(2):
            print(f"i={i}, j={j}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(3):
        لكل j في مدى(2):
            طباعة(f"i={i}, j={j}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
i=0, j=0
i=0, j=1
i=1, j=0
i=1, j=1
i=2, j=0
i=2, j=1
```

**Explanation:** Nested for loops.

## While Loops

### Basic While Loop

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    count = 0
    بينما count < 5:
        طباعة(count)
        count += 1
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

**Explanation:** Basic while loop using `بينما` for `while`.

### While Loop with Break

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    count = 0
    while True:
        print(count)
        count += 1
        if count >= 5:
            break
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    count = 0
    بينما صحيح_قيمة:
        طباعة(count)
        count += 1
        إذا count >= 5:
            كسر
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

**Explanation:** While loop with break using `كسر` for `break`.

### While Loop with Continue

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue
        print(count)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    count = 0
    بينما count < 5:
        count += 1
        إذا count == 3:
            متابعة
        طباعة(count)
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
2
4
5
```

**Explanation:** While loop with continue using `متابعة` for `continue`.

## Loop Control

### Break Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(10):
        إذا i == 5:
            كسر
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

**Explanation:** Breaking out of a loop early.

### Continue Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(5):
        if i == 2:
            continue
        print(i)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(5):
        إذا i == 2:
            متابعة
        طباعة(i)
    ```
  </TabItem>
</Tabs>

**Output:**
```
0
1
3
4
```

**Explanation:** Skipping iterations with continue.

### Else Clause in Loops

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    for i in range(5):
        print(i)
    else:
        print("Loop completed")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    لكل i في مدى(5):
        طباعة(i)
    وإلا:
        طباعة("Loop completed")
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
Loop completed
```

**Explanation:** Else clause executes when loop completes normally.

## Advanced Loops

### List Comprehension

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    squares = [x * 2 for x in range(5)]
    print(squares)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    squares = [x * 2 لكل x في مدى(5)]
    طباعة(squares)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[0, 2, 4, 6, 8]
```

**Explanation:** List comprehension using `لكل` for `for`.

### List Comprehension with Condition

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    evens = [x لكل x في مدى(10) إذا x % 2 == 0]
    طباعة(evens)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[0, 2, 4, 6, 8]
```

**Explanation:** List comprehension with conditional filter.

### Dictionary Comprehension

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    squares = {x: x * x for x in range(5)}
    print(squares)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    squares = {x: x * x لكل x في مدى(5)}
    طباعة(squares)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

**Explanation:** Dictionary comprehension.

### Zip Iteration

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    لكل name, age في ضغط(names, ages):
        طباعة(f"{name} is {age}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Alice is 25
Bob is 30
Charlie is 35
```

**Explanation:** Iterating over multiple sequences using `ضغط` for `zip`.

## Next Steps

- [Conditions](/docs/examples/conditions) - Learn about conditional logic
- [Lists](/docs/examples/lists) - Explore list operations
- [Generators](/docs/examples/generators) - Learn about generators
