---
title: Object-Oriented Programming
description: OOP patterns and examples
sidebar_label: OOP
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Object-Oriented Programming

Advanced OOP patterns and examples in ArabPy.

## Encapsulation

### Private Attributes

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class BankAccount:
        def __init__(self, balance):
            self.__balance = balance
        
        def deposit(self, amount):
            self.__balance += amount
        
        def get_balance(self):
            return self.__balance

    account = BankAccount(1000)
    account.deposit(500)
    print(account.get_balance())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة BankAccount:
        تعريف __init__(self, balance):
            self.__balance = balance
        
        تعريف deposit(self, amount):
            self.__balance += amount
        
        تعريف get_balance(self):
            إرجاع self.__balance

    account = BankAccount(1000)
    account.deposit(500)
    طباعة(account.get_balance())
    ```
  </TabItem>
</Tabs>

**Output:**
```
1500
```

**Explanation:** Encapsulation with private attributes using double underscore.

### Property Decorators

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
        
        @property
        def fahrenheit(self):
            return (self._celsius * 9/5) + 32

    temp = Temperature()
    temp.celsius = 25
    print(f"Fahrenheit: {temp.fahrenheit}")
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
        
        @خاصية
        تعريف fahrenheit(self):
            إرجاع (self._celsius * 9/5) + 32

    temp = Temperature()
    temp.celsius = 25
    طباعة(f"Fahrenheit: {temp.fahrenheit}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Fahrenheit: 77.0
```

**Explanation:** Property decorators for controlled attribute access.

## Inheritance

### Method Overriding

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Animal:
        def speak(self):
            return "Some sound"

    class Dog(Animal):
        def speak(self):
            return "Woof!"

    class Cat(Animal):
        def speak(self):
            return "Meow!"

    animals = [Dog(), Cat()]
    for animal in animals:
        print(animal.speak())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Animal:
        تعريف speak(self):
            إرجاع "Some sound"

    فئة Dog(Animal):
        تعريف speak(self):
            إرجاع "Woof!"

    فئة Cat(Animal):
        تعريف speak(self):
            إرجاع "Meow!"

    animals = [Dog(), Cat()]
    لكل animal في animals:
        طباعة(animal.speak())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Woof!
Meow!
```

**Explanation:** Method overriding in inheritance hierarchy.

### Super Method

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
        
        def speak(self):
            return f"{self.name} makes a sound"

    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)
            self.breed = breed
        
        def speak(self):
            return f"{self.name} barks"

    dog = Dog("Buddy", "Labrador")
    print(dog.speak())
    print(f"Breed: {dog.breed}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Animal:
        تعريف __init__(self, name):
            self.name = name
        
        تعريف speak(self):
            إرجاع f"{self.name} makes a sound"

    فئة Dog(Animal):
        تعريف __init__(self, name, breed):
            فئة_الأصل.__init__(self, name)
            self.breed = breed
        
        تعريف speak(self):
            إرجاع f"{self.name} barks"

    dog = Dog("Buddy", "Labrador")
    طباعة(dog.speak())
    طباعة(f"Breed: {dog.breed}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Buddy barks
Breed: Labrador
```

**Explanation:** Using super() to call parent class methods with `فئة_الأصل` for `super`.

## Polymorphism

### Duck Typing

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Duck:
        def quack(self):
            return "Quack!"

    class Person:
        def quack(self):
            return "I'm quacking like a duck"

    def make_quack(obj):
        return obj.quack()

    print(make_quack(Duck()))
    print(make_quack(Person()))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Duck:
        تعريف quack(self):
            إرجاع "Quack!"

    فئة Person:
        تعريف quack(self):
            إرجاع "I'm quacking like a duck"

    تعريف make_quack(obj):
        إرجاع obj.quack()

    طباعة(make_quack(Duck()))
    طباعة(make_quack(Person()))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Quack!
I'm quacking like a duck
```

**Explanation:** Duck typing - objects with same interface can be used interchangeably.

### Abstract Base Classes

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from abc import ABC, abstractmethod

    class Shape(ABC):
        @abstractmethod
        def area(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height
        
        def area(self):
            return self.width * self.height

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius
        
        def area(self):
            return 3.14 * self.radius ** 2

    shapes = [Rectangle(5, 3), Circle(2)]
    for shape in shapes:
        print(f"Area: {shape.area()}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من abc استيراد ABC, abstractmethod

    فئة Shape(ABC):
        @abstractmethod
        تعريف area(self):
            مرور

    فئة Rectangle(Shape):
        تعريف __init__(self, width, height):
            self.width = width
            self.height = height
        
        تعريف area(self):
            إرجاع self.width * self.height

    فئة Circle(Shape):
        تعريف __init__(self, radius):
            self.radius = radius
        
        تعريف area(self):
            إرجاع 3.14 * self.radius ** 2

    shapes = [Rectangle(5, 3), Circle(2)]
    لكل shape في shapes:
        طباعة(f"Area: {shape.area()}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Area: 15
Area: 12.56
```

**Explanation:** Abstract base classes defining interface for subclasses.

## Design Patterns

### Singleton Pattern

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Singleton:
        _instance = None
        
        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
            return cls._instance

    s1 = Singleton()
    s2 = Singleton()
    print(s1 is s2)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Singleton:
        _instance = None
        
        تعريف __new__(cls):
            إذا cls._instance هو None:
                cls._instance = فئة_الأصل.__new__(cls)
            إرجاع cls._instance

    s1 = Singleton()
    s2 = Singleton()
    طباعة(s1 هو s2)
    ```
  </TabItem>
</Tabs>

**Output:**
```
True
```

**Explanation:** Singleton pattern ensuring only one instance exists.

### Factory Pattern

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class AnimalFactory:
        @staticmethod
        def create_animal(animal_type):
            if animal_type == "dog":
                return Dog()
            elif animal_type == "cat":
                return Cat()
            else:
                raise ValueError("Unknown animal")

    class Dog:
        def speak(self):
            return "Woof!"

    class Cat:
        def speak(self):
            return "Meow!"

    dog = AnimalFactory.create_animal("dog")
    print(dog.speak())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة AnimalFactory:
        @طريقة_ثابتة
        تعريف create_animal(animal_type):
            إذا animal_type == "dog":
                إرجاع Dog()
            وإلا_إذا animal_type == "cat":
                إرجاع Cat()
            وإلا:
                رفع ValueError("Unknown animal")

    فئة Dog:
        تعريف speak(self):
            إرجاع "Woof!"

    فئة Cat:
        تعريف speak(self):
            إرجاع "Meow!"

    dog = AnimalFactory.create_animal("dog")
    طباعة(dog.speak())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Woof!
```

**Explanation:** Factory pattern for object creation.

## Next Steps

- [Decorators](/docs/examples/decorators) - Function decorators
- [Generators](/docs/examples/generators) - Generator functions
- [Context Managers](/docs/examples/context-managers) - With statements
