---
title: Context Managers
description: Context manager and with statement examples
sidebar_label: Context Managers
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Context Managers

Examples of context managers and with statements in ArabPy.

## Basic Context Managers

### File Context Manager

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("example.txt", "r") as f:
        content = f.read()
    print(content)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("example.txt", "r") كـ f:
        content = f.read()
    طباعة(content)
    ```
  </TabItem>
</Tabs>

**Output:**
```
File content here
```

**Explanation:** File context manager using `مع` for `with` and `كـ` for `as`.

### Multiple Context Managers

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        content = fin.read()
        fout.write(content.upper())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("input.txt", "r") كـ fin, open("output.txt", "w") كـ fout:
        content = fin.read()
        fout.كتابة(content.upper())
    ```
  </TabItem>
</Tabs>

**Explanation:** Multiple context managers in one statement.

## Custom Context Managers

### Using contextlib

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from contextlib import contextmanager

    @contextmanager
    def timer():
        import time
        start = time.time()
        yield
        end = time.time()
        print(f"Elapsed: {end - start:.2f}s")

    with timer():
        time.sleep(1)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من contextlib استيراد contextmanager

    @contextmanager
    تعريف timer():
        استيراد time
        start = time.time()
        إنتاج
        end = time.time()
        طباعة(f"Elapsed: {end - start:.2f}s")

    مع timer():
        time.sleep(1)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Elapsed: 1.00s
```

**Explanation:** Custom context manager using decorator.

### Class-based Context Manager

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class Timer:
        def __enter__(self):
            import time
            self.start = time.time()
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            import time
            end = time.time()
            print(f"Elapsed: {end - self.start:.2f}s")

    with Timer():
        import time
        time.sleep(1)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة Timer:
        تعريف __enter__(self):
            استيراد time
            self.start = time.time()
            إرجاع self
        
        تعريف __exit__(self, exc_type, exc_val, exc_tb):
            استيراد time
            end = time.time()
            طباعة(f"Elapsed: {end - self.start:.2f}s")

    مع Timer():
        استيراد time
        time.sleep(1)
    ```
  </TabItem>
</Tabs>

**Output:**
```
Elapsed: 1.00s
```

**Explanation:** Class-based context manager with magic methods.

## Practical Context Managers

### Database Connection

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class DatabaseConnection:
        def __init__(self, db_name):
            self.db_name = db_name
            self.connection = None
        
        def __enter__(self):
            print(f"Connecting to {self.db_name}")
            self.connection = f"Connection to {self.db_name}"
            return self.connection
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"Closing connection to {self.db_name}")
            self.connection = None

    with DatabaseConnection("mydb") as conn:
        print(f"Using: {conn}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة DatabaseConnection:
        تعريف __init__(self, db_name):
            self.db_name = db_name
            self.connection = None
        
        تعريف __enter__(self):
            طباعة(f"Connecting to {self.db_name}")
            self.connection = f"Connection to {self.db_name}"
            إرجاع self.connection
        
        تعريف __exit__(self, exc_type, exc_val, exc_tb):
            طباعة(f"Closing connection to {self.db_name}")
            self.connection = None

    مع DatabaseConnection("mydb") كـ conn:
        طباعة(f"Using: {conn}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Connecting to mydb
Using: Connection to mydb
Closing connection to mydb
```

**Explanation:** Database connection context manager.

### Lock Context Manager

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from threading import Lock

    lock = Lock()

    def critical_section():
        with lock:
            print("Critical section")
            # Protected code here

    critical_section()
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من threading استيراد Lock

    lock = Lock()

    تعريف critical_section():
        مع lock:
            طباعة("Critical section")
            # Protected code here

    critical_section()
    ```
  </TabItem>
</Tabs>

**Output:**
```
Critical section
```

**Explanation:** Thread lock context manager.

### Temporary Directory

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import tempfile

    with tempfile.TemporaryDirectory() as tmpdir:
        print(f"Temp dir: {tmpdir}")
        # Use temporary directory
    # Directory is automatically cleaned up
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد tempfile

    مع tempfile.TemporaryDirectory() كـ tmpdir:
        طباعة(f"Temp dir: {tmpdir}")
        # Use temporary directory
    # Directory is automatically cleaned up
    ```
  </TabItem>
</Tabs>

**Output:**
```
Temp dir: /tmp/tmpXXXXXX
```

**Explanation:** Temporary directory context manager.

## Exception Handling in Context Managers

### Handling Exceptions

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    class SafeOperation:
        def __enter__(self):
            print("Setup")
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is not None:
                print(f"Exception occurred: {exc_val}")
            print("Cleanup")
            return True  # Suppress exception

    with SafeOperation():
        raise ValueError("Test error")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    فئة SafeOperation:
        تعريف __enter__(self):
            طباعة("Setup")
            إرجاع self
        
        تعريف __exit__(self, exc_type, exc_val, exc_tb):
            إذا exc_type ليس هو None:
                طباعة(f"Exception occurred: {exc_val}")
            طباعة("Cleanup")
            إرجاع صحيح_قيمة  # Suppress exception

    مع SafeOperation():
        رفع ValueError("Test error")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Setup
Exception occurred: Test error
Cleanup
```

**Explanation:** Context manager with exception handling.

## Nested Context Managers

### Nested With Statements

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("file1.txt", "r") as f1:
        with open("file2.txt", "r") as f2:
            content1 = f1.read()
            content2 = f2.read()
            print(f"Read {len(content1)} + {len(content2)} bytes")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("file1.txt", "r") كـ f1:
        مع open("file2.txt", "r") كـ f2:
            content1 = f1.read()
            content2 = f2.read()
            طباعة(f"Read {طول(content1)} + {طول(content2)} bytes")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Read 10 + 15 bytes
```

**Explanation:** Nested context managers.

### ExitStack for Multiple Resources

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from contextlib import ExitStack

    files = ["file1.txt", "file2.txt", "file3.txt"]

    with ExitStack() as stack:
        handles = [stack.enter_context(open(f)) for f in files]
        for handle in handles:
            print(f"Opened: {handle.name}")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من contextlib استيراد ExitStack

    files = ["file1.txt", "file2.txt", "file3.txt"]

    مع ExitStack() كـ stack:
        handles = [stack.enter_context(open(f)) لكل f في files]
        لكل handle في handles:
            طباعة(f"Opened: {handle.name}")
    ```
  </TabItem>
</Tabs>

**Output:**
```
Opened: file1.txt
Opened: file2.txt
Opened: file3.txt
```

**Explanation:** ExitStack for managing multiple resources dynamically.

## Next Steps

- [Async/Await](/docs/examples/async-await) - Asynchronous programming
- [Dataclasses](/docs/examples/dataclasses) - Data class usage
- [Typing](/docs/examples/typing) - Type hints and annotations
