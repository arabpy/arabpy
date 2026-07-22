---
title: Classes
description: Class definition and OOP examples
sidebar_label: Classes
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Classes

Examples of class definitions and object-oriented programming in ArabPy.

## Basic Classes

### Simple Class

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
        
        def greet(self):
            return f"Hello, {self.name}!"

    person = Person("Ahmed")
    print(person.greet())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Person:
        تعريف __init__(self, name):
            self.name = name
        
        تعريف greet(self):
            إرجاع f"Hello, {self.name}!"

    person = Person("Ahmed")
    طباعة(person.greet())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Hello, Ahmed!
```

**Explanation:** Basic class with constructor and method using `فئة` for `class` and `تعريف` for `def`.

### Class with Multiple Methods

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Calculator:
        def __init__(self):
            self.result = 0
        
        def add(self, x):
            self.result += x
            return self.result
        
        def subtract(self, x):
            self.result -= x
            return self.result

    calc = Calculator()
    print(calc.add(10))
    print(calc.subtract(5))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Calculator:
        تعريف __init__(self):
            self.result = 0
        
        تعريف add(self, x):
            self.result += x
            إرجاع self.result
        
        تعريف subtract(self, x):
            self.result -= x
            إرجاع self.result

    calc = Calculator()
    طباعة(calc.add(10))
    طباعة(calc.subtract(5))
    ```
  </TabItem>
</Tabs>

**Output:**
```
10
5
```

**Explanation:** Class with multiple methods maintaining internal state.

## Inheritance

### Single Inheritance

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    dog = Dog("Buddy")
    print(f"{dog.name} says: {dog.speak()}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Animal:
        تعريف __init__(self, name):
            self.name = name
        
        تعريف speak(self):
            إرجاع "Some sound"

    فئة Dog(Animal):
        تعريف speak(self):
            إرجاع "Woof!"

    dog = Dog("Buddy")
    طباعة(f"{dog.name} says: {dog.speak()}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Buddy says: Woof!
```

**Explanation:** Class inheritance with method overriding.

### Multiple Inheritance

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Flyer:
        def fly(self):
            return "Flying"

    class Swimmer:
        def swim(self):
            return "Swimming"

    class Duck(Flyer, Swimmer):
        pass

    duck = Duck()
    print(duck.fly())
    print(duck.swim())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Flyer:
        تعريف fly(self):
            إرجاع "Flying"

    فئة Swimmer:
        تعريف swim(self):
            إرجاع "Swimming"

    فئة Duck(Flyer, Swimmer):
        مرور

    duck = Duck()
    طباعة(duck.fly())
    طباعة(duck.swim())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Flying
Swimming
```

**Explanation:** Multiple inheritance using `مرور` for `pass`.

## Special Methods

### String Representation

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def __str__(self):
            return f"Point({self.x}, {self.y})"

    point = Point(3, 4)
    print(point)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Point:
        تعريف __init__(self, x, y):
            self.x = x
            self.y = y
        
        تعريف __str__(self):
            إرجاع f"Point({self.x}, {self.y})"

    point = Point(3, 4)
    طباعة(point)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Point(3, 4)
```

**Explanation:** String representation using `__str__` magic method.

### Length Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class MyList:
        def __init__(self, items):
            self.items = items
        
        def __len__(self):
            return len(self.items)

    my_list = MyList([1, 2, 3, 4, 5])
    print(len(my_list))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة MyList:
        تعريف __init__(self, items):
            self.items = items
        
        تعريف __len__(self):
            إرجاع طول(self.items)

    my_list = MyList([1, 2, 3, 4, 5])
    طباعة(طول(my_list))
    ```
  </TabItem>
</Tabs>

**Output:**
```
5
```

**Explanation:** Custom length using `__len__` magic method.

### Item Access

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class MyDict:
        def __init__(self):
            self.data = {}
        
        def __setitem__(self, key, value):
            self.data[key] = value
        
        def __getitem__(self, key):
            return self.data[key]

    d = MyDict()
    d["name"] = "ArabPy"
    print(d["name"])
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة MyDict:
        تعريف __init__(self):
            self.data = {}
        
        تعريف __setitem__(self, key, value):
            self.data[key] = value
        
        تعريف __getitem__(self, key):
            إرجاع self.data[key]

    d = MyDict()
    d["name"] = "ArabPy"
    طباعة(d["name"])
    ```
  </TabItem>
</Tabs>

**Output:**
```
ArabPy
```

**Explanation:** Custom item access using `__setitem__` and `__getitem__`.

## Properties

### Getter and Setter

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Temperature:
        def __init__(self):
            self._celsius = 0
        
        @property
        def celsius(self):
            return self._celsius
        
        @celsius.setter
        def celsius(self, value):
            if value < -273.15:
                raise ValueError("Too cold!")
            self._celsius = value

    temp = Temperature()
    temp.celsius = 25
    print(temp.celsius)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Temperature:
        تعريف __init__(self):
            self._celsius = 0
        
        @خاصية
        تعريف celsius(self):
            إرجاع self._celsius
        
        @celsius.setter
        تعريف celsius(self, value):
            إذا value < -273.15:
                رفع ValueError("Too cold!")
            self._celsius = value

    temp = Temperature()
    temp.celsius = 25
    طباعة(temp.celsius)
    ```
  </TabItem>
</Tabs>

**Output:**
```
25
```

**Explanation:** Property decorator using `@خاصية` for `@property`.

## Class Methods and Static Methods

### Class Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Math:
        @classmethod
    def add(cls, a, b):
        return a + b

    result = Math.add(5, 3)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Math:
        @طريقة_فئة
        تعريف add(cls, a, b):
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

**Explanation:** Class method using `@طريقة_فئة` for `@classmethod`.

### Static Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Math:
        @staticmethod
    def multiply(a, b):
        return a * b

    result = Math.multiply(5, 3)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Math:
        @طريقة_ثابتة
        تعريف multiply(a, b):
            إرجاع a * b

    result = Math.multiply(5, 3)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
15
```

**Explanation:** Static method using `@طريقة_ثابتة` for `@staticmethod`.

## Next Steps

- [Loops](/docs/examples/loops) - Learn about iteration
- [Conditions](/docs/examples/conditions) - Explore conditional logic
- [OOP](/docs/examples/oop) - Advanced OOP patterns
