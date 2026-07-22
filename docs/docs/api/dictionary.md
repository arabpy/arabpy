---
title: ARABIC_TRANSLATIONS
description: Translation dictionary API reference
sidebar_label: Dictionary
---

# ARABIC_TRANSLATIONS

The comprehensive translation dictionary used by ArabPy for bidirectional code translation.

## Overview

`ARABIC_TRANSLATIONS` is a dictionary containing over 3,200 translations between Python keywords, built-in functions, operators, exceptions, and their Arabic equivalents.

## Access

```python
from arabpy import ARABIC_TRANSLATIONS

print(len(ARABIC_TRANSLATIONS))  # 3200+
print(type(ARABIC_TRANSLATIONS))  # dict
```

## Structure

The dictionary maps Python terms to Arabic terms:

```python
{
    "def": "تعريف",
    "if": "إذا",
    "for": "لكل",
    "print": "طباعة",
    # ... 3200+ more entries
}
```

## Categories

### Keywords

Python control flow and structural keywords:

```python
from arabpy import ARABIC_TRANSLATIONS

# Control flow
print(ARABIC_TRANSLATIONS["if"])      # إذا
print(ARABIC_TRANSLATIONS["elif"])    # وإلا_إذا
print(ARABIC_TRANSLATIONS["else"])    # وإلا
print(ARABIC_TRANSLATIONS["for"])     # لكل
print(ARABIC_TRANSLATIONS["while"])  # بينما

# Functions and classes
print(ARABIC_TRANSLATIONS["def"])     # تعريف
print(ARABIC_TRANSLATIONS["class"])  # فئة
print(ARABIC_TRANSLATIONS["return"]) # إرجاع
print(ARABIC_TRANSLATIONS["yield"])  # إنتاج

# Exception handling
print(ARABIC_TRANSLATIONS["try"])     # جرب
print(ARABIC_TRANSLATIONS["except"]) # باستثناء
print(ARABIC_TRANSLATIONS["finally"])# أخيرا
print(ARABIC_TRANSLATIONS["raise"])  # رفع
```

### Built-in Functions

Python built-in functions:

```python
from arabpy import ARABIC_TRANSLATIONS

# I/O
print(ARABIC_TRANSLATIONS["print"])  # طباعة
print(ARABIC_TRANSLATIONS["input"])  # إدخال

# Type conversion
print(ARABIC_TRANSLATIONS["int"])    # عدد_صحيح
print(ARABIC_TRANSLATIONS["float"])  # عدد_عشري
print(ARABIC_TRANSLATIONS["str"])    # سلسلة
print(ARABIC_TRANSLATIONS["bool"])   # منطقي

# Sequence operations
print(ARABIC_TRANSLATIONS["len"])    # طول
print(ARABIC_TRANSLATIONS["range"])  # مدى
print(ARABIC_TRANSLATIONS["sorted"]) # مرتب

# Math
print(ARABIC_TRANSLATIONS["abs"])    # قيمة_مطلقة
print(ARABIC_TRANSLATIONS["round"]) # تقريب
print(ARABIC_TRANSLATIONS["min"])    # أدنى
print(ARABIC_TRANSLATIONS["max"])    # أقصى
```

### Operators

Logical and comparison operators:

```python
from arabpy import ARABIC_TRANSLATIONS

# Logical
print(ARABIC_TRANSLATIONS["and"])    # و
print(ARABIC_TRANSLATIONS["or"])     # أو
print(ARABIC_TRANSLATIONS["not"])    # ليس

# Membership and identity
print(ARABIC_TRANSLATIONS["in"])     # في
print(ARABIC_TRANSLATIONS["is"])     # هو
```

### Boolean Values

Boolean constants:

```python
from arabpy import ARABIC_TRANSLATIONS

print(ARABIC_TRANSLATIONS["True"])   # صحيح_قيمة
print(ARABIC_TRANSLATIONS["False"])  # خطأ
print(ARABIC_TRANSLATIONS["None"])   # لاشيء
```

### Exceptions

Python exception types:

```python
from arabpy import ARABIC_TRANSLATIONS

# Common exceptions
print(ARABIC_TRANSLATIONS["Exception"])      # استثناء
print(ARABIC_TRANSLATIONS["ValueError"])    # خطأ_قيمة
print(ARABIC_TRANSLATIONS["TypeError"])     # خطأ_نوع
print(ARABIC_TRANSLATIONS["NameError"])     # خطأ_اسم
print(ARABIC_TRANSLATIONS["SyntaxError"])   # خطأ_صياغة
print(ARABIC_TRANSLATIONS["RuntimeError"])  # خطأ_وقت_التشغيل
print(ARABIC_TRANSLATIONS["ZeroDivisionError"]) # خطأ_قسمة_على_صفر
```

### Standard Library Modules

Common standard library modules:

```python
from arabpy import ARABIC_TRANSLATIONS

# Math
print(ARABIC_TRANSLATIONS["math"])          # رياضيات

# Random
print(ARABIC_TRANSLATIONS["random"])        # عشوائي

# Datetime
print(ARABIC_TRANSLATIONS["datetime"])      # تاريخ_وقت

# JSON
print(ARABIC_TRANSLATIONS["json"])          # جسون

# OS
print(ARABIC_TRANSLATIONS["os"])            # نظام_التشغيل

# Regular expressions
print(ARABIC_TRANSLATIONS["re"])            # تعبير_نمطي
```

### Magic Methods

Python magic methods:

```python
from arabpy import ARABIC_TRANSLATIONS

# Common magic methods
print(ARABIC_TRANSLATIONS["__init__"])     # __تهيئة__
print(ARABIC_TRANSLATIONS["__str__"])      # __سلسلة__
print(ARABIC_TRANSLATIONS["__repr__"])     # __تمثيل__
print(ARABIC_TRANSLATIONS["__len__"])      # __طول__
print(ARABIC_TRANSLATIONS["__getitem__"])  # __الحصول_على_عنصر__
print(ARABIC_TRANSLATIONS["__setitem__"])  # __تعيين_عنصر__
```

## Usage Examples

### Check if a translation exists

```python
from arabpy import ARABIC_TRANSLATIONS

if "print" in ARABIC_TRANSLATIONS:
    print(f"Arabic for 'print': {ARABIC_TRANSLATIONS['print']}")
```

### Get all keywords

```python
from arabpy import ARABIC_TRANSLATIONS

keywords = [k for k in ARABIC_TRANSLATIONS.keys() if k in ['if', 'else', 'for', 'while']]
print(keywords)
```

### Reverse lookup (Arabic to Python)

```python
from arabpy import ARABIC_TRANSLATIONS

# Create reverse dictionary
arabic_to_python = {v: k for k, v in ARABIC_TRANSLATIONS.items()}

print(arabic_to_python["طباعة"])  # print
print(arabic_to_python["إذا"])     # if
```

### Filter by category

```python
from arabpy import ARABIC_TRANSLATIONS

# Get all exception translations
exceptions = {k: v for k, v in ARABIC_TRANSLATIONS.items() if k.endswith("Error")}
print(f"Total exceptions: {len(exceptions)}")
```

### Statistics

```python
from arabpy import ARABIC_TRANSLATIONS

print(f"Total translations: {len(ARABIC_TRANSLATIONS)}")
print(f"Sample entries: {list(ARABIC_TRANSLATIONS.items())[:10]}")
```

## Custom Dictionaries

The ArabPyTranslator class maintains separate dictionaries for efficient translation:

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Access internal dictionaries
print(len(translator.PYTHON_TO_ARABIC))
print(len(translator.ARABIC_TO_PYTHON))
```

## Extending the Dictionary

You can extend the dictionary with custom translations:

```python
from arabpy import ArabPyTranslator

translator = ArabPyTranslator()

# Add custom translation
translator.PYTHON_TO_ARABIC["custom_func"] = "دالة_مخصصة"
translator.ARABIC_TO_PYTHON["دالة_مخصصة"] = "custom_func"
```

## Dictionary Files

The main dictionary is stored in `arabpy/dictionary.py`. There's also an expanded dictionary in `arabpy/dictionary_expanded.py` with additional translations.

```python
# arabpy/dictionary.py
ARABIC_TRANSLATIONS = {
    "def": "تعريف",
    "if": "إذا",
    # ... more entries
}

# arabpy/dictionary_expanded.py
ARABIC_TRANSLATIONS_EXPANDED = {
    # Additional translations
}
```

## Performance Considerations

- The dictionary is loaded once at import time
- Lookup operations are O(1) due to hash table implementation
- The dictionary size (~3,200 entries) has minimal memory impact
- Translation operations are fast due to efficient dictionary lookups

## Contributing

To add new translations to the dictionary:

1. Edit `arabpy/dictionary.py`
2. Add entries in the format `{"python_term": "arabic_term"}`
3. Ensure bidirectional consistency
4. Add tests for new translations
5. Submit a pull request

## See Also

- [ArabPyTranslator](/docs/api/translator) - Translation engine
- [arabic_code_runner](/docs/api/runner) - Code execution
- [Contributing](/docs/contributing) - How to contribute
