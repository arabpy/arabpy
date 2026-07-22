---
title: Conditions
description: Conditional statement examples
sidebar_label: Conditions
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Conditions

Examples of conditional statements in ArabPy.

## If Statements

### Basic If Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    if x > 5:
        print("x is greater than 5")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    إذا x > 5:
        طباعة("x is greater than 5")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x is greater than 5
```

**Explanation:** Basic if statement using `إذا` for `if`.

### If-Else Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 3
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is less than or equal to 5")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 3
    إذا x > 5:
        طباعة("x is greater than 5")
    وإلا:
        طباعة("x is less than or equal to 5")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x is less than or equal to 5
```

**Explanation:** If-else statement using `وإلا` for `else`.

### If-Elif-Else Statement

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 75
    if x >= 90:
        grade = "A"
    elif x >= 80:
        grade = "B"
    elif x >= 70:
        grade = "C"
    else:
        grade = "F"
    print(f"Grade: {grade}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 75
    إذا x >= 90:
        grade = "A"
    وإلا_إذا x >= 80:
        grade = "B"
    وإلا_إذا x >= 70:
        grade = "C"
    وإلا:
        grade = "F"
    طباعة(f"Grade: {grade}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Grade: C
```

**Explanation:** If-elif-else chain using `وإلا_إذا` for `elif`.

## Comparison Operators

### Greater Than

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    a = 10
    b = 5
    if a > b:
        print("a is greater than b")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    a = 10
    b = 5
    إذا a > b:
        طباعة("a is greater than b")
    ```
  </TabItem>
</Tabs>

**Output:**
```
a is greater than b
```

**Explanation:** Greater than comparison.

### Less Than

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    a = 5
    b = 10
    if a < b:
        print("a is less than b")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    a = 5
    b = 10
    إذا a < b:
        طباعة("a is less than b")
    ```
  </TabItem>
</Tabs>

**Output:**
```
a is less than b
```

**Explanation:** Less than comparison.

### Equal To

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    a = 10
    b = 10
    if a == b:
        print("a equals b")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    a = 10
    b = 10
    إذا a == b:
        طباعة("a equals b")
    ```
  </TabItem>
</Tabs>

**Output:**
```
a equals b
```

**Explanation:** Equality comparison.

### Not Equal To

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    a = 10
    b = 5
    if a != b:
        print("a does not equal b")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    a = 10
    b = 5
    إذا a != b:
        طباعة("a does not equal b")
    ```
  </TabItem>
</Tabs>

**Output:**
```
a does not equal b
```

**Explanation:** Inequality comparison.

## Logical Operators

### AND Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    y = 20
    if x > 5 and y > 15:
        print("Both conditions are true")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    y = 20
    إذا x > 5 و y > 15:
        طباعة("Both conditions are true")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Both conditions are true
```

**Explanation:** Logical AND using `و` for `and`.

### OR Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 5
    y = 3
    if x > 10 or y > 2:
        print("At least one condition is true")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 5
    y = 3
    إذا x > 10 أو y > 2:
        طباعة("At least one condition is true")
    ```
  </TabItem>
</Tabs>

**Output:**
```
At least one condition is true
```

**Explanation:** Logical OR using `أو` for `or`.

### NOT Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = False
    if not x:
        print("x is False")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = خطأ
    إذا ليس x:
        طباعة("x is False")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x is False
```

**Explanation:** Logical NOT using `ليس` for `not`.

## Membership Operators

### In Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    if "apple" in fruits:
        print("apple is in the list")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    إذا "apple" في fruits:
        طباعة("apple is in the list")
    ```
  </TabItem>
</Tabs>

**Output:**
```
apple is in the list
```

**Explanation:** Membership test using `في` for `in`.

### Not In Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    fruits = ["apple", "banana", "cherry"]
    if "orange" not in fruits:
        print("orange is not in the list")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    fruits = ["apple", "banana", "cherry"]
    إذا "orange" ليس في fruits:
        طباعة("orange is not in the list")
    ```
  </TabItem>
</Tabs>

**Output:**
```
orange is not in the list
```

**Explanation:** Negative membership test.

## Identity Operators

### Is Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = None
    if x is None:
        print("x is None")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = لاشيء
    إذا x هو لاشيء:
        طباعة("x is None")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x is None
```

**Explanation:** Identity test using `هو` for `is`.

### Is Not Operator

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    y = 20
    if x is not y:
        print("x and y are different objects")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    y = 20
    إذا x ليس هو y:
        طباعة("x and y are different objects")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x and y are different objects
```

**Explanation:** Negative identity test.

## Nested Conditions

### Nested If Statements

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    y = 20
    if x > 5:
        if y > 15:
            print("Both conditions are true")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    y = 20
    إذا x > 5:
        إذا y > 15:
            طباعة("Both conditions are true")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Both conditions are true
```

**Explanation:** Nested conditional statements.

## Ternary Operator

### Conditional Expression

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    x = 10
    result = "even" if x % 2 == 0 else "odd"
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    x = 10
    result = "even" إذا x % 2 == 0 وإلا "odd"
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
even
```

**Explanation:** Ternary conditional expression.

## Next Steps

- [Lists](/docs/examples/lists) - Explore list operations
- [Dictionaries](/docs/examples/dictionaries) - Learn dictionary usage
- [Exceptions](/docs/examples/exceptions) - Exception handling patterns
