---
title: Arabic Keywords
description: Complete reference of Arabic Python keywords
sidebar_label: Keywords
---

# Arabic Keywords

Complete reference of all Python keywords translated to Arabic.

## Control Flow Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `if` | `إذا` | Conditional statement |
| `elif` | `وإلا_إذا` | Else if condition |
| `else` | `وإلا` | Else condition |
| `for` | `لكل` | For loop |
| `while` | `بينما` | While loop |
| `break` | `كسر` | Exit loop |
| `continue` | `متابعة` | Continue to next iteration |
| `pass` | `مرور` | Placeholder statement |

## Function and Class Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `def` | `تعريف` | Define function |
| `return` | `إرجاع` | Return value |
| `yield` | `إنتاج` | Generator yield |
| `class` | `فئة` | Define class |
| `lambda` | `لامبدا` | Anonymous function |

## Exception Handling Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `try` | `جرب` | Try block |
| `except` | `باستثناء` | Exception handler |
| `finally` | `أخيرا` | Finally block |
| `raise` | `رفع` | Raise exception |
| `assert` | `تأكيد` | Assertion |

## Variable and Scope Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `global` | `عالمي` | Global variable |
| `nonlocal` | `غير_محلي` | Nonlocal variable |
| `del` | `حذف` | Delete object |
| `import` | `استيراد` | Import module |
| `from` | `من` | Import from |
| `as` | `كـ` | Import alias |

## Logical Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `and` | `و` | Logical AND |
| `or` | `أو` | Logical OR |
| `not` | `ليس` | Logical NOT |
| `in` | `في` | Membership test |
| `is` | `هو` | Identity test |

## Boolean and None Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `True` | `صحيح_قيمة` | Boolean true |
| `False` | `خطأ` | Boolean false |
| `None` | `لاشيء` | None value |

## Async Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `async` | `غير_متزامن` | Async function |
| `await` | `انتظار` | Await coroutine |

## Context Manager Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `with` | `مع` | Context manager |

## Other Keywords

| Python | Arabic | Description |
|--------|--------|-------------|
| `match` | `مطابقة` | Pattern matching |
| `case` | `حالة` | Case in match |

## Usage Examples

### Control Flow

```python
# Python
if condition:
    do_something()
elif other_condition:
    do_other()
else:
    do_default()

# Arabic
إذا condition:
    do_something()
وإلا_إذا other_condition:
    do_other()
وإلا:
    do_default()
```

### Functions

```python
# Python
def function_name(param):
    return result

# Arabic
تعريف function_name(param):
    إرجاع result
```

### Classes

```python
# Python
class ClassName:
    def method(self):
        pass

# Arabic
فئة ClassName:
    تعريف method(self):
        مرور
```

### Exception Handling

```python
# Python
try:
    risky_operation()
except Exception as e:
    handle_error()
finally:
    cleanup()

# Arabic
جرب:
    risky_operation()
باستثناء Exception كـ e:
    handle_error()
أخيرا:
    cleanup()
```

## Notes

- Keywords are case-sensitive in both Python and Arabic
- Variable names are not translated, only keywords
- Strings and comments are preserved during translation
- The translation is bidirectional and reversible

## Next Steps

- [Built-in Functions](/docs/arabic-syntax/built-in-functions) - Built-in function translations
- [Modules](/docs/arabic-syntax/modules) - Standard library modules
- [Examples](/docs/examples/index) - Practical examples
