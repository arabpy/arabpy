---
title: File Handling
description: File I/O operation examples
sidebar_label: File Handling
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# File Handling

Examples of file input/output operations in ArabPy.

## Reading Files

### Read Entire File

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

**Explanation:** Reading entire file using `مع` for `with` and `كـ` for `as`.

### Read Line by Line

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("example.txt", "r") as f:
        for line in f:
            print(line.strip())
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("example.txt", "r") كـ f:
        لكل line في f:
            طباعة(line.strip())
    ```
  </TabItem>
</Tabs>

**Output:**
```
Line 1
Line 2
Line 3
```

**Explanation:** Reading file line by line.

### Read Lines into List

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("example.txt", "r") as f:
        lines = f.readlines()
    print(lines)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("example.txt", "r") كـ f:
        lines = f.قراءة_الأسطر()
    طباعة(lines)
    ```
  </TabItem>
</Tabs>

**Output:**
```
['Line 1\n', 'Line 2\n', 'Line 3\n']
```

**Explanation:** Reading all lines into a list using `قراءة_الأسطر` for `readlines`.

## Writing Files

### Write to File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("output.txt", "w") as f:
        f.write("Hello, World!")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("output.txt", "w") كـ f:
        f.كتابة("Hello, World!")
    ```
  </TabItem>
</Tabs>

**Explanation:** Writing to file using `كتابة` for `write`.

### Write Multiple Lines

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("output.txt", "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")
        f.write("Line 3\n")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("output.txt", "w") كـ f:
        f.كتابة("Line 1\n")
        f.كتابة("Line 2\n")
        f.كتابة("Line 3\n")
    ```
  </TabItem>
</Tabs>

**Explanation:** Writing multiple lines to file.

### Write List to File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    lines = ["Line 1", "Line 2", "Line 3"]
    with open("output.txt", "w") as f:
        f.writelines(line + "\n" for line in lines)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    lines = ["Line 1", "Line 2", "Line 3"]
    مع open("output.txt", "w") كـ f:
        f.كتابة_الأسطر(line + "\n" لكل line في lines)
    ```
  </TabItem>
</Tabs>

**Explanation:** Writing list of lines to file using `كتابة_الأسطر` for `writelines`.

## Appending to Files

### Append to File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    with open("output.txt", "a") as f:
        f.write("New line\n")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    مع open("output.txt", "a") كـ f:
        f.كتابة("New line\n")
    ```
  </TabItem>
</Tabs>

**Explanation:** Appending to existing file.

## File Modes

### Different File Modes

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    # Read mode
    with open("file.txt", "r") as f:
        content = f.read()
    
    # Write mode (overwrites)
    with open("file.txt", "w") as f:
        f.write("New content")
    
    # Append mode
    with open("file.txt", "a") as f:
        f.write("Additional content")
    
    # Read and write mode
    with open("file.txt", "r+") as f:
        content = f.read()
        f.write("Modified content")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    # Read mode
    مع open("file.txt", "r") كـ f:
        content = f.read()
    
    # Write mode (overwrites)
    مع open("file.txt", "w") كـ f:
        f.كتابة("New content")
    
    # Append mode
    مع open("file.txt", "a") كـ f:
        f.كتابة("Additional content")
    
    # Read and write mode
    مع open("file.txt", "r+") كـ f:
        content = f.read()
        f.كتابة("Modified content")
    ```
  </TabItem>
</Tabs>

**Explanation:** Different file opening modes.

## File Operations

### Check if File Exists

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import os

    if os.path.exists("example.txt"):
        print("File exists")
    else:
        print("File does not exist")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد نظام_التشغيل

    إذا نظام_التشغيل.مسار.موجود("example.txt"):
        طباعة("File exists")
    وإلا:
        طباعة("File does not exist")
    ```
  </TabItem>
</Tabs>

**Output:**
```
File exists
```

**Explanation:** Checking if file exists using `نظام_التشغيل` for `os`.

### Delete File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import os

    if os.path.exists("example.txt"):
        os.remove("example.txt")
        print("File deleted")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد نظام_التشغيل

    إذا نظام_التشغيل.مسار.موجود("example.txt"):
        نظام_التشغيل.إزالة("example.txt")
        طباعة("File deleted")
    ```
  </TabItem>
</Tabs>

**Output:**
```
File deleted
```

**Explanation:** Deleting file using `إزالة` for `remove`.

### Rename File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import os

    os.rename("old_name.txt", "new_name.txt")
    print("File renamed")
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد نظام_التشغيل

    نظام_التشغيل.إعادة_تسمية("old_name.txt", "new_name.txt")
    طباعة("File renamed")
    ```
  </TabItem>
</Tabs>

**Output:**
```
File renamed
```

**Explanation:** Renaming file using `إعادة_تسمية` for `rename`.

## Working with Paths

### Using Pathlib

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    from pathlib import Path

    file_path = Path("example.txt")
    if file_path.exists():
        content = file_path.read_text()
        print(content)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    من مسار_المكتبة استيراد مسار

    file_path = مسار("example.txt")
    إذا file_path.موجود():
        content = file_path.قراءة_نص()
        طباعة(content)
    ```
  </TabItem>
</Tabs>

**Output:**
```
File content here
```

**Explanation:** Using pathlib for file operations.

### Join Paths

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import os

    path = os.path.join("folder", "subfolder", "file.txt")
    print(path)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد نظام_التشغيل

    path = نظام_التشغيل.مسار.ربط("folder", "subfolder", "file.txt")
    طباعة(path)
    ```
  </TabItem>
</Tabs>

**Output:**
```
folder/subfolder/file.txt
```

**Explanation:** Joining path components using `ربط` for `join`.

## JSON Files

### Read JSON File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import json

    with open("data.json", "r") as f:
        data = json.load(f)
    print(data)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد جسون

    مع open("data.json", "r") كـ f:
        data = جسون.تحميل(f)
    طباعة(data)
    ```
  </TabItem>
</Tabs>

**Output:**
```
{'key': 'value'}
```

**Explanation:** Reading JSON file using `جسون` for `json`.

### Write JSON File

<Tabs>
  <TabItem value="python" label="Python">
    ```python
    import json

    data = {"name": "Ahmed", "age": 30}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)
    ```
  </TabItem>
  <TabItem value="arabic" label="Arabic">
    ```python
    استيراد جسون

    data = {"name": "Ahmed", "age": 30}
    مع open("data.json", "w") كـ f:
        جسون.حفظ(data, f, indent=2)
    ```
  </TabItem>
</Tabs>

**Explanation:** Writing JSON file using `حفظ` for `dump`.

## Next Steps

- [OOP](/docs/examples/oop) - Advanced OOP patterns
- [Decorators](/docs/examples/decorators) - Function decorators
- [Generators](/docs/examples/generators) - Generator functions
