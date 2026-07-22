---
title: Lists
description: List operation examples
sidebar_label: Lists
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Lists

Examples of list operations in ArabPy.

## Creating Lists

### Empty List

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    empty_list = []
    print(empty_list)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    empty_list = []
    طباعة(empty_list)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[]
```

**Explanation:** Creating an empty list.

### List with Elements

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    طباعة(fruits)
    ```
  </TabItem>
</Tabs>

**Output:**
```
['apple', 'banana', 'cherry']
```

**Explanation:** Creating a list with elements.

### List with Mixed Types

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    mixed = [1, "hello", 3.14, True]
    print(mixed)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    mixed = [1, "hello", 3.14, صحيح_قيمة]
    طباعة(mixed)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[1, 'hello', 3.14, True]
```

**Explanation:** List with mixed data types.

## Accessing Elements

### Index Access

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0])
    print(fruits[1])
    print(fruits[2])
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    طباعة(fruits[0])
    طباعة(fruits[1])
    طباعة(fruits[2])
    ```
  </TabItem>
</Tabs>

**Output:**
```
apple
banana
cherry
```

**Explanation:** Accessing elements by index.

### Negative Indexing

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits[-1])
    print(fruits[-2])
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    طباعة(fruits[-1])
    طباعة(fruits[-2])
    ```
  </TabItem>
</Tabs>

**Output:**
```
cherry
banana
```

**Explanation:** Accessing elements from the end.

### Slicing

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [0, 1, 2, 3, 4, 5]
    print(numbers[1:4])
    print(numbers[:3])
    print(numbers[3:])
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [0, 1, 2, 3, 4, 5]
    طباعة(numbers[1:4])
    طباعة(numbers[:3])
    طباعة(numbers[3:])
    ```
  </TabItem>
</Tabs>

**Output:**
```
[1, 2, 3]
[0, 1, 2]
[3, 4, 5]
```

**Explanation:** List slicing operations.

## Modifying Lists

### Append Element

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana"]
    fruits.append("cherry")
    print(fruits)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana"]
    fruits.إضافة("cherry")
    طباعة(fruits)
    ```
  </TabItem>
</Tabs>

**Output:**
```
['apple', 'banana', 'cherry']
```

**Explanation:** Adding element to end using `إضافة` for `append`.

### Insert Element

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "cherry"]
    fruits.insert(1, "banana")
    print(fruits)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "cherry"]
    fruits.إدراج(1, "banana")
    طباعة(fruits)
    ```
  </TabItem>
</Tabs>

**Output:**
```
['apple', 'banana', 'cherry']
```

**Explanation:** Inserting element at specific position using `إدراج` for `insert`.

### Remove Element

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.remove("banana")
    print(fruits)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits.إزالة("banana")
    طباعة(fruits)
    ```
  </TabItem>
</Tabs>

**Output:**
```
['apple', 'cherry']
```

**Explanation:** Removing element by value using `إزالة` for `remove`.

### Pop Element

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    last = fruits.pop()
    print(f"Removed: {last}")
    print(fruits)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    last = fruits.إزالة_الأخير()
    طباعة(f"Removed: {last}")
    طباعة(fruits)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Removed: cherry
['apple', 'banana']
```

**Explanation:** Removing last element using `إزالة_الأخير` for `pop`.

## List Operations

### Concatenation

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    print(combined)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    combined = list1 + list2
    طباعة(combined)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[1, 2, 3, 4, 5, 6]
```

**Explanation:** Concatenating two lists.

### Repetition

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    repeated = [1, 2] * 3
    print(repeated)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    repeated = [1, 2] * 3
    طباعة(repeated)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[1, 2, 1, 2, 1, 2]
```

**Explanation:** Repeating list elements.

### Length

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(len(fruits))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    طباعة(طول(fruits))
    ```
  </TabItem>
</Tabs>

**Output:**
```
3
```

**Explanation:** Getting list length using `طول` for `len`.

### Sorting

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    sorted_numbers = مرتب(numbers)
    طباعة(sorted_numbers)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[1, 1, 2, 3, 4, 5, 6, 9]
```

**Explanation:** Sorting list using `مرتب` for `sorted`.

### Reversing

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = list(reversed(numbers))
    print(reversed_numbers)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [1, 2, 3, 4, 5]
    reversed_numbers = قائمة(معكوس(numbers))
    طباعة(reversed_numbers)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[5, 4, 3, 2, 1]
```

**Explanation:** Reversing list using `معكوس` for `reversed`.

## Searching Lists

### Index of Element

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    index = fruits.index("banana")
    print(index)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    index = fruits.فهرس("banana")
    طباعة(index)
    ```
  </TabItem>
</Tabs>

**Output:**
```
1
```

**Explanation:** Finding index of element using `فهرس` for `index`.

### Count Occurrences

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    numbers = [1, 2, 2, 3, 3, 3]
    count = numbers.count(3)
    print(count)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    numbers = [1, 2, 2, 3, 3, 3]
    count = numbers.عد(3)
    طباعة(count)
    ```
  </TabItem>
</Tabs>

**Output:**
```
3
```

**Explanation:** Counting element occurrences using `عد` for `count`.

### Check Membership

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    if "banana" in fruits:
        print("banana is in the list")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    إذا "banana" في fruits:
        طباعة("banana is in the list")
    ```
  </TabItem>
</Tabs>

**Output:**
```
banana is in the list
```

**Explanation:** Checking if element exists in list.

## List Comprehensions

### Basic Comprehension

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

**Explanation:** Basic list comprehension.

### With Condition

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

**Explanation:** List comprehension with condition.

## Next Steps

- [Dictionaries](/docs/examples/dictionaries) - Learn dictionary operations
- [Tuples](/docs/examples/tuples) - Explore tuple usage
- [Sets](/docs/examples/sets) - Learn about sets
