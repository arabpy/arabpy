---
title: Dictionaries
description: Dictionary operation examples
sidebar_label: Dictionaries
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dictionaries

Examples of dictionary operations in ArabPy.

## Creating Dictionaries

### Empty Dictionary

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    empty_dict = {}
    print(empty_dict)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    empty_dict = {}
    طباعة(empty_dict)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{}
```

**Explanation:** Creating an empty dictionary.

### Dictionary with Elements

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30}
```

**Explanation:** Creating a dictionary with key-value pairs.

### Dictionary with dict() Constructor

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = dict(name="Ahmed", age=30)
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = قاموس(name="Ahmed", age=30)
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30}
```

**Explanation:** Creating dictionary using constructor with `قاموس` for `dict`.

## Accessing Elements

### Access by Key

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    print(person["name"])
    print(person["age"])
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    طباعة(person["name"])
    طباعة(person["age"])
    ```
  </TabItem>
</Tabs>

**Output:**
```
Ahmed
30
```

**Explanation:** Accessing values by key.

### Get Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    name = person.get("name")
    print(name)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    name = person.الحصول("name")
    طباعة(name)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Ahmed
```

**Explanation:** Accessing value using get method with `الحصول` for `get`.

### Get with Default

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    city = person.get("city", "Unknown")
    print(city)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    city = person.الحصول("city", "Unknown")
    طباعة(city)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Unknown
```

**Explanation:** Getting value with default if key doesn't exist.

## Modifying Dictionaries

### Add or Update Key

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed"}
    person["age"] = 30
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed"}
    person["age"] = 30
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30}
```

**Explanation:** Adding or updating a key-value pair.

### Update Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed"}
    person.update({"age": 30, "city": "Cairo"})
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed"}
    person.تحديث({"age": 30, "city": "Cairo"})
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30, 'city': 'Cairo'}
```

**Explanation:** Updating dictionary with another using `تحديث` for `update`.

### Remove Key

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    del person["age"]
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    حذف person["age"]
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed'}
```

**Explanation:** Removing a key using `حذف` for `del`.

### Pop Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    age = person.pop("age")
    print(f"Removed: {age}")
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    age = person.إزالة("age")
    طباعة(f"Removed: {age}")
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Removed: 30
{'name': 'Ahmed'}
```

**Explanation:** Removing and returning value using `إزالة` for `pop`.

## Dictionary Operations

### Get Keys

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    keys = person.keys()
    print(list(keys))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    keys = person.المفاتيح()
    طباعة(قائمة(keys))
    ```
  </TabItem>
</Tabs>

**Output:**
```
['name', 'age']
```

**Explanation:** Getting all keys using `المفاتيح` for `keys`.

### Get Values

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    values = person.values()
    print(list(values))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    values = person.القيم()
    طباعة(قائمة(values))
    ```
  </TabItem>
</Tabs>

**Output:**
```
['Ahmed', 30]
```

**Explanation:** Getting all values using `القيم` for `values`.

### Get Items

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    items = person.items()
    print(list(items))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    items = person.العناصر()
    طباعة(قائمة(items))
    ```
  </TabItem>
</Tabs>

**Output:**
```
[('name', 'Ahmed'), ('age', 30)]
```

**Explanation:** Getting all key-value pairs using `العناصر` for `items`.

### Length

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    print(len(person))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    طباعة(طول(person))
    ```
  </TabItem>
</Tabs>

**Output:**
```
2
```

**Explanation:** Getting dictionary length using `طول` for `len`.

## Searching Dictionaries

### Check Key Exists

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    if "name" in person:
        print("name key exists")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    إذا "name" في person:
        طباعة("name key exists")
    ```
  </TabItem>
</Tabs>

**Output:**
```
name key exists
```

**Explanation:** Checking if key exists in dictionary.

### Check Value Exists

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    person = {"name": "Ahmed", "age": 30}
    if "Ahmed" in person.values():
        print("Ahmed is a value")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    person = {"name": "Ahmed", "age": 30}
    إذا "Ahmed" في person.القيم():
        طباعة("Ahmed is a value")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Ahmed is a value
```

**Explanation:** Checking if value exists in dictionary.

## Dictionary Comprehensions

### Basic Comprehension

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

### With Condition

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    evens = {x: x * x for x in range(10) if x % 2 == 0}
    print(evens)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    evens = {x: x * x لكل x في مدى(10) إذا x % 2 == 0}
    طباعة(evens)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

**Explanation:** Dictionary comprehension with condition.

## Nested Dictionaries

### Creating Nested Dictionary

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    data = {
        "person": {
            "name": "Ahmed",
            "age": 30
        },
        "location": {
            "city": "Cairo",
            "country": "Egypt"
        }
    }
    print(data)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    data = {
        "person": {
            "name": "Ahmed",
            "age": 30
        },
        "location": {
            "city": "Cairo",
            "country": "Egypt"
        }
    }
    طباعة(data)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'person': {'name': 'Ahmed', 'age': 30}, 'location': {'city': 'Cairo', 'country': 'Egypt'}}
```

**Explanation:** Nested dictionary structure.

### Accessing Nested Values

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    data = {"person": {"name": "Ahmed", "age": 30}}
    name = data["person"]["name"]
    print(name)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    data = {"person": {"name": "Ahmed", "age": 30}}
    name = data["person"]["name"]
    طباعة(name)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Ahmed
```

**Explanation:** Accessing nested dictionary values.

## Next Steps

- [Exceptions](/docs/examples/exceptions) - Learn exception handling
- [File Handling](/docs/examples/file-handling) - Explore file I/O
- [OOP](/docs/examples/oop) - Advanced OOP patterns
