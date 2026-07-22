---
title: Modules
description: Arabic translations for Python standard library modules
sidebar_label: Modules
---

# Modules

Arabic translations for commonly used Python standard library modules.

## Math Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `math.sqrt` | `رياضيات.جذر_تربيعي` | Square root |
| `math.pow` | `رياضيات.أس` | Power |
| `math.sin` | `رياضيات.جيب` | Sine |
| `math.cos` | `رياضيات.جيب_تمام` | Cosine |
| `math.tan` | `رياضيات.ظل` | Tangent |
| `math.pi` | `رياضيات.باي` | Pi constant |
| `math.e` | `رياضيات.إي` | Euler's number |

```python
# Python
import math
result = math.sqrt(16)

# Arabic
استيراد رياضيات
result = رياضيات.جذر_تربيعي(16)
```

## Random Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `random.random` | `عشوائي.عشوائي` | Random float |
| `random.randint` | `عشوائي.عدد_صحيح_عشوائي` | Random integer |
| `random.choice` | `عشوائي.اختيار` | Random choice |
| `random.shuffle` | `عشوائي.خلط` | Shuffle list |

```python
# Python
import random
num = random.randint(1, 10)

# Arabic
استيراد عشوائي
num = عشوائي.عدد_صحيح_عشوائي(1, 10)
```

## Datetime Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `datetime.date` | `تاريخ_وقت.تاريخ` | Date object |
| `datetime.time` | `تاريخ_وقت.وقت` | Time object |
| `datetime.datetime` | `تاريخ_وقت.تاريخ_وقت` | Datetime object |
| `datetime.timedelta` | `تاريخ_وقت.فترة_زمنية` | Time delta |

```python
# Python
from datetime import datetime
now = datetime.now()

# Arabic
من تاريخ_وقت استيراد تاريخ_وقت
now = تاريخ_وقت.الآن()
```

## JSON Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `json.dump` | `جسون.حفظ` | Save JSON |
| `json.load` | `جسون.تحميل` | Load JSON |
| `json.dumps` | `جسون.تحويل_لسلسلة` | Convert to string |
| `json.loads` | `جسون.تحميل_من_سلسلة` | Load from string |

```python
# Python
import json
data = json.loads('{"key": "value"}')

# Arabic
استيراد جسون
data = جسون.تحميل_من_سلسلة('{"key": "value"}')
```

## OS Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `os.path.join` | `نظام_التشغيل.مسار.ربط` | Join paths |
| `os.getcwd` | `نظام_التشغيل.المسار_الحالي` | Current directory |
| `os.listdir` | `نظام_التشغيل.قائمة_الملفات` | List files |
| `os.mkdir` | `نظام_التشغيل.إنشاء_مجلد` | Create directory |

```python
# Python
import os
path = os.path.join("folder", "file.txt")

# Arabic
استيراد نظام_التشغيل
path = نظام_التشغيل.مسار.ربط("folder", "file.txt")
```

## Re Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `re.match` | `تعبير_نمطي.مطابقة` | Match pattern |
| `re.search` | `تعبير_نمطي.بحث` | Search pattern |
| `re.findall` | `تعبير_نمطي.البحث_الكل` | Find all |
| `re.sub` | `تعبير_نمطي.استبدال` | Substitute |

```python
# Python
import re
matches = re.findall(r'\d+', text)

# Arabic
استيراد تعبير_نمطي
matches = تعبير_نمطي.البحث_الكل(r'\d+', text)
```

## Collections Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `collections.Counter` | `مجموعات.عداد` | Counter object |
| `collections.defaultdict` | `مجموعات.قاموس_افتراضي` | Default dict |
| `collections.namedtuple` | `مجموعات.مجموعة_مسماه` | Named tuple |

```python
# Python
from collections import Counter
counts = Counter([1, 1, 2, 3])

# Arabic
من مجموعات استيراد عداد
counts = عداد([1, 1, 2, 3])
```

## Itertools Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `itertools.count` | `أدوات_التكرار.عد` | Count iterator |
| `itertools.cycle` | `أدوات_التكرار.دورة` | Cycle iterator |
| `itertools.chain` | `أدوات_التكرار.سلسلة` | Chain iterators |

```python
# Python
from itertools import count
counter = count()

# Arabic
من أدوات_التكرار استيراد عد
counter = عد()
```

## Pathlib Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `pathlib.Path` | `مسار_المكتبة.مسار` | Path object |

```python
# Python
from pathlib import Path
file_path = Path("file.txt")

# Arabic
من مسار_المكتبة استيراد مسار
file_path = مسار("file.txt")
```

## Typing Module

| Python | Arabic | Description |
|--------|--------|-------------|
| `typing.List` | `الكتابة.قائمة` | List type hint |
| `typing.Dict` | `الكتابة.قاموس` | Dict type hint |
| `typing.Optional` | `الكتابة.اختياري` | Optional type hint |
| `typing.Union` | `الكتابة.اتحاد` | Union type hint |

```python
# Python
from typing import List, Optional

def process(items: List[str]) -> Optional[str]:
    pass

# Arabic
من الكتابة استيراد قائمة, اختياري

تعريف process(items: قائمة[سلسلة]) -> اختياري[سلسلة]:
    مرور
```

## Common Patterns

### Import Statements

```python
# Python
import math
from datetime import datetime
import os as operating_system

# Arabic
استيراد رياضيات
من تاريخ_وقت استيراد تاريخ_وقت
استيراد نظام_التشغيل كـ operating_system
```

### Module Usage

```python
# Python
import random
import json

data = {"number": random.randint(1, 100)}
json_str = json.dumps(data)

# Arabic
استيراد عشوائي
استيراد جسون

data = {"number": عشوائي.عدد_صحيح_عشوائي(1, 100)}
json_str = جسون.تحويل_لسلسلة(data)
```

## Notes

- Module translations cover commonly used standard library modules
- Not all standard library modules are translated yet
- Contributions for additional module translations are welcome
- Module names can be used in English if translation is not available

## Next Steps

- [API Reference](/docs/api/index) - Detailed API documentation
- [Examples](/docs/examples/index) - Practical examples
- [Contributing](/docs/contributing) - Help expand module translations
