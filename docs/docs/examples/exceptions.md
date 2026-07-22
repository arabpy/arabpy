---
title: Exceptions
description: Exception handling examples
sidebar_label: Exceptions
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Exceptions

Examples of exception handling in ArabPy.

## Basic Exception Handling

### Try-Except Block

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء ZeroDivisionError:
        طباعة("Cannot divide by zero")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Cannot divide by zero
```

**Explanation:** Basic try-except block using `جرب` for `try` and `باستثناء` for `except`.

### Try-Except-Else

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 2
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print(f"Result: {result}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 2
    باستثناء ZeroDivisionError:
        طباعة("Cannot divide by zero")
    وإلا:
        طباعة(f"Result: {result}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Result: 5.0
```

**Explanation:** Try-except-else block where else executes if no exception occurs.

### Try-Except-Finally

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Cannot divide by zero")
    finally:
        print("Cleanup code")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء ZeroDivisionError:
        طباعة("Cannot divide by zero")
    أخيرا:
        طباعة("Cleanup code")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Cannot divide by zero
Cleanup code
```

**Explanation:** Try-except-finally block using `أخيرا` for `finally`.

## Multiple Exception Handlers

### Multiple Except Blocks

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        value = int("abc")
    except ValueError:
        print("Invalid value")
    except TypeError:
        print("Invalid type")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        value = عدد_صحيح("abc")
    باستثناء ValueError:
        طباعة("Invalid value")
    باستثناء TypeError:
        طباعة("Invalid type")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Invalid value
```

**Explanation:** Multiple exception handlers for different error types.

### Catching Multiple Exceptions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        value = int("abc")
    except (ValueError, TypeError):
        print("Invalid input")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        value = عدد_صحيح("abc")
    باستثناء (ValueError, TypeError):
        طباعة("Invalid input")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Invalid input
```

**Explanation:** Catching multiple exception types in one block.

## Exception Information

### Accessing Exception Message

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء ZeroDivisionError كـ e:
        طباعة(f"Error: {e}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Error: division by zero
```

**Explanation:** Accessing exception object using `كـ` for `as`.

### Getting Exception Type

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except Exception as e:
        print(f"Exception type: {type(e).__name__}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء Exception كـ e:
        طباعة(f"Exception type: {نوع(e).__name__}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Exception type: ZeroDivisionError
```

**Explanation:** Getting the exception type name.

## Raising Exceptions

### Raise Exception

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def validate_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        return age

    try:
        validate_age(-5)
    except ValueError as e:
        print(f"Error: {e}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف validate_age(age):
        إذا age < 0:
            رفع ValueError("Age cannot be negative")
        إرجاع age

    جرب:
        validate_age(-5)
    باستثناء ValueError كـ e:
        طباعة(f"Error: {e}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Error: Age cannot be negative
```

**Explanation:** Raising exceptions using `رفع` for `raise`.

### Raise Custom Exception

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class CustomError(Exception):
        pass

    def process():
        raise CustomError("Something went wrong")

    try:
        process()
    except CustomError as e:
        print(f"Custom error: {e}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة CustomError(Exception):
        مرور

    تعريف process():
        رفع CustomError("Something went wrong")

    جرب:
        process()
    باستثناء CustomError كـ e:
        طباعة(f"Custom error: {e}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Custom error: Something went wrong
```

**Explanation:** Raising custom exceptions.

### Re-raising Exceptions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Logging error")
        raise  # Re-raise the same exception
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        result = 10 / 0
    باستثناء ZeroDivisionError:
        طباعة("Logging error")
        رفع  # Re-raise the same exception
    ```
  </TabItem>
</Tabs>

**Output:**
```
Logging error
ZeroDivisionError: division by zero
```

**Explanation:** Re-raising exceptions after handling.

## Common Exception Patterns

### File Handling with Exceptions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    try:
        with open("nonexistent.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("IO error occurred")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    جرب:
        مع open("nonexistent.txt", "r") كـ f:
            content = f.read()
    باستثناء FileNotFoundError:
        طباعة("File not found")
    باستثناء IOError:
        طباعة("IO error occurred")
    ```
  </TabItem>
</Tabs>

**Output:**
```
File not found
```

**Explanation:** File handling with exception management.

### Input Validation

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def get_positive_number():
        while True:
            try:
                value = int(input("Enter a positive number: "))
                if value <= 0:
                    raise ValueError("Must be positive")
                return value
            except ValueError as e:
                print(f"Error: {e}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف get_positive_number():
        بينما صحيح_قيمة:
            جرب:
                value = عدد_صحيح(إدخال("Enter a positive number: "))
                إذا value <= 0:
                    رفع ValueError("Must be positive")
                إرجاع value
            باستثناء ValueError كـ e:
                طباعة(f"Error: {e}")
    ```
  </TabItem>
</Tabs>

**Explanation:** Input validation with exception handling.

## Exception Chaining

### Exception Chaining

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    def process_data():
        try:
            data = int("invalid")
        except ValueError as e:
            raise RuntimeError("Data processing failed") from e

    try:
        process_data()
    except RuntimeError as e:
        print(f"Error: {e}")
        print(f"Caused by: {e.__cause__}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    تعريف process_data():
        جرب:
            data = عدد_صحيح("invalid")
        باستثناء ValueError كـ e:
            رفع RuntimeError("Data processing failed") من e

    جرب:
        process_data()
    باستثناء RuntimeError كـ e:
        طباعة(f"Error: {e}")
        طباعة(f"Caused by: {e.__cause__}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Error: Data processing failed
Caused by: invalid literal for int() with base 10: 'invalid'
```

**Explanation:** Exception chaining to preserve original exception context.

## Next Steps

- [File Handling](/docs/examples/file-handling) - Learn file I/O operations
- [OOP](/docs/examples/oop) - Advanced OOP patterns
- [Decorators](/docs/examples/decorators) - Function decorators
