---
title: Built-in Functions
description: Arabic translations for Python built-in functions
sidebar_label: Built-in Functions
---

# Built-in Functions

Complete reference of Python built-in functions translated to Arabic.

## Input/Output Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `print` | `طباعة` | Print to console |
| `input` | `إدخال` | Get user input |

## Type Conversion Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `int` | `عدد_صحيح` | Convert to integer |
| `float` | `عدد_عشري` | Convert to float |
| `str` | `سلسلة` | Convert to string |
| `bool` | `منطقي` | Convert to boolean |
| `list` | `قائمة` | Convert to list |
| `tuple` | `مجموعة` | Convert to tuple |
| `dict` | `قاموس` | Convert to dictionary |
| `set` | `مجموعة_فريدة` | Convert to set |
| `bytes` | `بايت` | Convert to bytes |

## Sequence Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `len` | `طول` | Get length |
| `range` | `مدى` | Create range |
| `enumerate` | `تعداد` | Enumerate items |
| `zip` | `ضغط` | Combine sequences |
| `sorted` | `مرتب` | Sort sequence |
| `reversed` | `معكوس` | Reverse sequence |

## Math Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `abs` | `قيمة_مطلقة` | Absolute value |
| `round` | `تقريب` | Round number |
| `min` | `أدنى` | Minimum value |
| `max` | `أقصى` | Maximum value |
| `sum` | `مجموع` | Sum of items |
| `pow` | `أس` | Power function |

## Object Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `type` | `نوع` | Get type |
| `isinstance` | `هو_مثيل` | Check instance |
| `issubclass` | `هو_فئة_فرعية` | Check subclass |
| `hasattr` | `لديه_خاصية` | Check attribute |
| `getattr` | `الحصول_على_خاصية` | Get attribute |
| `setattr` | `تعيين_خاصية` | Set attribute |
| `delattr` | `حذف_خاصية` | Delete attribute |
| `id` | `معرف` | Get object id |

## String Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `chr` | `حرف` | Character from code |
| `ord` | `كود` | Code from character |

## Iteration Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `iter` | `مكرر` | Create iterator |
| `next` | `التالي` | Next item |
| `map` | `خريطة` | Map function |
| `filter` | `تصفية` | Filter items |
| `reduce` | `تقليل` | Reduce items |

## Collection Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `all` | `الكل` | All true |
| `any` | `أي` | Any true |

## Dictionary Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `dict` | `قاموس` | Create dictionary |
| `keys` | `المفاتيح` | Get keys |
| `values` | `القيم` | Get values |
| `items` | `العناصر` | Get items |
| `get` | `الحصول` | Get value |

## File Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `open` | `فتح` | Open file |

## Variable Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `globals` | `المتغيرات_العالمية` | Global variables |
| `locals` | `المتغيرات_المحلية` | Local variables |
| `vars` | `متغيرات` | Object variables |

## Code Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `eval` | `تقييم` | Evaluate code |
| `exec` | `تنفيذ` | Execute code |
| `compile` | `ترجمة` | Compile code |

## Help Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `help` | `مساعدة` | Get help |
| `dir` | `دليل` | List attributes |

## Other Functions

| Python | Arabic | Description |
|--------|--------|-------------|
| `repr` | `تمثيل` | String representation |
| `hash` | `تجزئة` | Hash value |
| `format` | `تنسيق` | Format string |
| `bin` | `ثنائي` | Binary string |
| `hex` | `سداسي_عشري` | Hexadecimal string |
| `oct` | `ثماني` | Octal string |
| `slice` | `شريحة` | Slice object |
| `object` | `كائن` | Base object |
| `super` | `فئة_الأصل` | Parent class |
| `property` | `خاصية` | Property decorator |
| `staticmethod` | `طريقة_ثابتة` | Static method |
| `classmethod` | `طريقة_فئة` | Class method |

## Usage Examples

### Input/Output

```python
# Python
print("Hello, World!")
name = input("Enter your name: ")

# Arabic
طباعة("Hello, World!")
name = إدخال("Enter your name: ")
```

### Type Conversion

```python
# Python
x = int("123")
y = float("3.14")
z = str(456)

# Arabic
x = عدد_صحيح("123")
y = عدد_عشري("3.14")
z = سلسلة(456)
```

### Sequence Operations

```python
# Python
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
total = sum(numbers)
sorted_nums = sorted(numbers)

# Arabic
numbers = [1, 2, 3, 4, 5]
length = طول(numbers)
total = مجموع(numbers)
sorted_nums = مرتب(numbers)
```

### Object Inspection

```python
# Python
obj = SomeClass()
obj_type = type(obj)
if isinstance(obj, SomeClass):
    print("It's an instance")

# Arabic
obj = SomeClass()
obj_type = نوع(obj)
إذا هو_مثيل(obj, SomeClass):
    طباعة("It's an instance")
```

### Dictionary Operations

```python
# Python
data = {"key": "value"}
keys = data.keys()
values = data.values()
item = data.get("key")

# Arabic
data = {"key": "value"}
keys = data.المفاتيح()
values = data.القيم()
item = data.الحصول("key")
```

## Notes

- Built-in functions are translated to their Arabic equivalents
- Function behavior remains the same regardless of language
- All built-in functions are supported
- Translation is bidirectional and reversible

## Next Steps

- [Modules](/docs/arabic-syntax/modules) - Standard library modules
- [Examples](/docs/examples/index) - Practical examples
- [API Reference](/docs/api/index) - Detailed API documentation
