---
title: Typing
description: Type hints and annotations examples
sidebar_label: Typing
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Typing

Examples of type hints and annotations in ArabPy.

## Basic Type Hints

### Variable Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    name: str = "Ahmed"
    age: int = 30
    height: float = 1.75
    is_active: bool = True
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    name: str = "Ahmed"
    age: int = 30
    height: float = 1.75
    is_active: bool = صحيح_قيمة
    ```
  </TabItem>
</Tabs>

**Explanation:** Basic variable type hints.

### Function Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def add(a: int, b: int) -> int:
        return a + b

    def greet(name: str) -> str:
        return f"Hello, {name}!"
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف add(a: int, b: int) -> int:
        إرجاع a + b

    تعريف greet(name: str) -> str:
        إرجاع f"Hello, {name}!"
    ```
  </TabItem>
</Tabs>

**Explanation:** Function parameter and return type hints.

## Collection Type Hints

### List Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import List

    def process_numbers(numbers: List[int]) -> List[int]:
        return [x * 2 for x in numbers]

    result = process_numbers([1, 2, 3])
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد قائمة

    تعريف process_numbers(numbers: قائمة[int]) -> قائمة[int]:
        إرجاع [x * 2 لكل x في numbers]

    result = process_numbers([1, 2, 3])
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
[2, 4, 6]
```

**Explanation:** List type hints using `قائمة` for `List`.

### Dictionary Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Dict

    def get_age(data: Dict[str, int], name: str) -> int:
        return data.get(name, 0)

    ages = {"Ahmed": 30, "Sara": 25}
    print(get_age(ages, "Ahmed"))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد قاموس

    تعريف get_age(data: قاموس[str, int], name: str) -> int:
        إرجاع data.الحصول(name, 0)

    ages = {"Ahmed": 30, "Sara": 25}
    طباعة(get_age(ages, "Ahmed"))
    ```
  </TabItem>
</Tabs>

**Output:**
```
30
```

**Explanation:** Dictionary type hints using `قاموس` for `Dict`.

### Tuple Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Tuple

    def get_coordinates() -> Tuple[float, float]:
        return 10.5, 20.3

    x, y = get_coordinates()
    print(f"x={x}, y={y}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد مجموعة

    تعريف get_coordinates() -> مجموعة[float, float]:
        إرجاع 10.5, 20.3

    x, y = get_coordinates()
    طباعة(f"x={x}, y={y}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
x=10.5, y=20.3
```

**Explanation:** Tuple type hints using `مجموعة` for `Tuple`.

## Advanced Type Hints

### Optional Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Optional

    def find_user(user_id: int) -> Optional[str]:
        users = {1: "Ahmed", 2: "Sara"}
        return users.get(user_id)

    print(find_user(1))
    print(find_user(3))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد اختياري

    تعريف find_user(user_id: int) -> اختياري[str]:
        users = {1: "Ahmed", 2: "Sara"}
        إرجاع users.الحصول(user_id)

    طباعة(find_user(1))
    طباعة(find_user(3))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Ahmed
None
```

**Explanation:** Optional type hints using `اختياري` for `Optional`.

### Union Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Union

    def process(value: Union[int, str]) -> str:
        return f"Processed: {value}"

    print(process(42))
    print(process("hello"))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد اتحاد

    تعريف process(value: اتحاد[int, str]) -> str:
        إرجاع f"Processed: {value}"

    طباعة(process(42))
    طباعة(process("hello"))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Processed: 42
Processed: hello
```

**Explanation:** Union type hints using `اتحاد` for `Union`.

### Any Type

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Any

    def process_any(value: Any) -> str:
        return f"Type: {type(value).__name__}"

    print(process_any(42))
    print(process_any("hello"))
    print(process_any([1, 2, 3]))
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد أي

    تعريف process_any(value: أي) -> str:
        إرجاع f"Type: {نوع(value).__name__}"

    طباعة(process_any(42))
    طباعة(process_any("hello"))
    طباعة(process_any([1, 2, 3]))
    ```
  </TabItem>
</Tabs>

**Output:**
```
Type: int
Type: str
Type: list
```

**Explanation:** Any type hint using `أي` for `Any`.

## Callable Type Hints

### Function Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Callable

    def apply_operation(x: int, operation: Callable[[int], int]) -> int:
        return operation(x)

    def square(n: int) -> int:
        return n * n

    result = apply_operation(5, square)
    print(result)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد قابل_للاستدعاء

    تعريف apply_operation(x: int, operation: قابل_للاستدعاء[[int], int]) -> int:
        إرجاع operation(x)

    تعريف square(n: int) -> int:
        إرجاع n * n

    result = apply_operation(5, square)
    طباعة(result)
    ```
  </TabItem>
</Tabs>

**Output:**
```
25
```

**Explanation:** Callable type hints using `قابل_للاستدعاء` for `Callable`.

## Class Type Hints

### Class Type Hints

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import Type

    class Animal:
        def speak(self) -> str:
            return "Some sound"

    def create_animal(animal_class: Type[Animal]) -> Animal:
        return animal_class()

    animal = create_animal(Animal)
    print(animal.speak())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد نوع

    فئة Animal:
        تعريف speak(self) -> str:
            إرجاع "Some sound"

    تعريف create_animal(animal_class: نوع[Animal]) -> Animal:
        إرجاع animal_class()

    animal = create_animal(Animal)
    طباعة(animal.speak())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Some sound
```

**Explanation:** Class type hints using `نوع` for `Type`.

## Generic Type Hints

### Type Variables

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from typing import TypeVar, Generic

    T = TypeVar('T')

    class Container(Generic[T]):
        def __init__(self, value: T):
            self.value = value
        
        def get(self) -> T:
            return self.value

    container = Container(42)
    print(container.get())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من الكتابة استيراد TypeVar, Generic

    T = TypeVar('T')

    فئة Container(Generic[T]):
        تعريف __init__(self, value: T):
            self.value = value
        
        تعريف get(self) -> T:
            إرجاع self.value

    container = Container(42)
    طباعة(container.get())
    ```
  </TabItem>
</Tabs>

**Output:**
```
42
```

**Explanation:** Generic type hints with TypeVar.

## Next Steps

- [API Reference](/docs/api/index) - Detailed API documentation
- [FAQ](/docs/faq) - Frequently asked questions
- [Contributing](/docs/contributing) - How to contribute
