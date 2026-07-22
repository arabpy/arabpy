---
title: Dataclasses
description: Data class usage examples
sidebar_label: Dataclasses
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Dataclasses

Examples of data class usage in ArabPy.

## Basic Dataclasses

### Simple Dataclass

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int
        city: str

    person = Person("Ahmed", 30, "Cairo")
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass
    فئة Person:
        name: str
        age: int
        city: str

    person = Person("Ahmed", 30, "Cairo")
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Person(name='Ahmed', age=30, city='Cairo')
```

**Explanation:** Basic dataclass with type hints.

### Dataclass with Default Values

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int = 0
        city: str = "Unknown"

    person = Person("Ahmed")
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass
    فئة Person:
        name: str
        age: int = 0
        city: str = "Unknown"

    person = Person("Ahmed")
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Person(name='Ahmed', age=0, city='Unknown')
```

**Explanation:** Dataclass with default field values.

## Dataclass Features

### Frozen Dataclass

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass(frozen=True)
    class Point:
        x: int
        y: int

    point = Point(3, 4)
    # point.x = 5  # This would raise FrozenInstanceError
    print(point)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass(frozen=True)
    فئة Point:
        x: int
        y: int

    point = Point(3, 4)
    # point.x = 5  # This would raise FrozenInstanceError
    طباعة(point)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Point(x=3, y=4)
```

**Explanation:** Immutable dataclass using frozen=True.

### Dataclass with Methods

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass
    class Rectangle:
        width: float
        height: float
        
        def area(self) -> float:
            return self.width * self.height
        
        def perimeter(self) -> float:
            return 2 * (self.width + self.height)

    rect = Rectangle(5.0, 3.0)
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass
    فئة Rectangle:
        width: float
        height: float
        
        تعريف area(self) -> float:
            إرجاع self.width * self.height
        
        تعريف perimeter(self) -> float:
            إرجاع 2 * (self.width + self.height)

    rect = Rectangle(5.0, 3.0)
    طباعة(f"Area: {rect.area()}")
    طباعة(f"Perimeter: {rect.perimeter()}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Area: 15.0
Perimeter: 16.0
```

**Explanation:** Dataclass with custom methods.

## Advanced Dataclasses

### Dataclass with __post_init__

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int
        
        def __post_init__(self):
            if self.age < 0:
                raise ValueError("Age cannot be negative")

    person = Person("Ahmed", 30)
    print(person)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass
    فئة Person:
        name: str
        age: int
        
        تعريف __post_init__(self):
            إذا self.age < 0:
                رفع ValueError("Age cannot be negative")

    person = Person("Ahmed", 30)
    طباعة(person)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Person(name='Ahmed', age=30)
```

**Explanation:** Dataclass with post-initialization validation.

### Dataclass with Field

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass, field

    @dataclass
    class Student:
        name: str
        grades: list = field(default_factory=list)
        
        def add_grade(self, grade: int):
            self.grades.append(grade)
        
        def average(self) -> float:
            return sum(self.grades) / len(self.grades) if self.grades else 0

    student = Student("Ahmed")
    student.add_grade(85)
    student.add_grade(90)
    print(f"Average: {student.average()}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass, field

    @dataclass
    فئة Student:
        name: str
        grades: list = field(default_factory=list)
        
        تعريف add_grade(self, grade: int):
            self.grades.إضافة(grade)
        
        تعريف average(self) -> float:
            إرجاع مجموع(self.grades) / طول(self.grades) إذا self.grades وإلا 0

    student = Student("Ahmed")
    student.add_grade(85)
    student.add_grade(90)
    طباعة(f"Average: {student.average()}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Average: 87.5
```

**Explanation:** Dataclass with mutable default using field.

## Dataclass Operations

### Convert to Dictionary

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass, asdict

    @dataclass
    class Person:
        name: str
        age: int

    person = Person("Ahmed", 30)
    person_dict = asdict(person)
    print(person_dict)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass, asdict

    @dataclass
    فئة Person:
        name: str
        age: int

    person = Person("Ahmed", 30)
    person_dict = asdict(person)
    طباعة(person_dict)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'name': 'Ahmed', 'age': 30}
```

**Explanation:** Converting dataclass to dictionary using `asdict`.

### Convert to Tuple

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass, astuple

    @dataclass
    class Person:
        name: str
        age: int

    person = Person("Ahmed", 30)
    person_tuple = astuple(person)
    print(person_tuple)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass, astuple

    @dataclass
    فئة Person:
        name: str
        age: int

    person = Person("Ahmed", 30)
    person_tuple = astuple(person)
    طباعة(person_tuple)
    ```
  </TabItem>
</Tabs>

**Output:**
```
('Ahmed', 30)
```

**Explanation:** Converting dataclass to tuple using `astuple`.

## Inheritance with Dataclasses

### Dataclass Inheritance

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int

    @dataclass
    class Employee(Person):
        employee_id: int
        department: str

    employee = Employee("Ahmed", 30, 12345, "Engineering")
    print(employee)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من dataclasses استيراد dataclass

    @dataclass
    فئة Person:
        name: str
        age: int

    @dataclass
    فئة Employee(Person):
        employee_id: int
        department: str

    employee = Employee("Ahmed", 30, 12345, "Engineering")
    طباعة(employee)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Employee(name='Ahmed', age=30, employee_id=12345, department='Engineering')
```

**Explanation:** Dataclass inheritance.

## Next Steps

- [Typing](/docs/examples/typing) - Type hints and annotations
- [API Reference](/docs/api/index) - Detailed API documentation
- [FAQ](/docs/faq) - Frequently asked questions
