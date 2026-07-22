---
title: API Reference
description: Complete API reference for ArabPy
sidebar_label: API Reference
---

# API Reference

Complete API reference for the ArabPy library.

## Overview

ArabPy provides a simple and intuitive API for translating Python code to Arabic and vice versa. The library consists of three main components:

- **ArabPyTranslator** - Main translation engine
- **arabic_code_runner** - Direct code execution
- **ARABIC_TRANSLATIONS** - Translation dictionary

## Quick Reference

```python
from arabpy import ArabPyTranslator, arabic_code_runner, ARABIC_TRANSLATIONS

# Translation
translator = ArabPyTranslator()
arabic_code = translator.to_arabic(python_code)
python_code = translator.to_python(arabic_code)

# Execution
namespace = arabic_code_runner(arabic_code)

# Dictionary
print(len(ARABIC_TRANSLATIONS))  # 3200+ translations
```

## Modules

- [ArabPyTranslator](/docs/api/translator) - Translation engine
- [arabic_code_runner](/docs/api/runner) - Code execution
- [ARABIC_TRANSLATIONS](/docs/api/dictionary) - Translation dictionary

## Type Hints

All ArabPy functions include full type hints for better IDE support and type checking:

```python
from arabpy import ArabPyTranslator
from typing import Dict, Any

translator: ArabPyTranslator = ArabPyTranslator()
result: Dict[str, Any] = translator.to_python("س = 10")
```

## Error Handling

ArabPy provides clear error messages for common issues:

```python
from arabpy import arabic_code_runner

try:
    result = arabic_code_runner(123)  # TypeError
except TypeError as e:
    print(f"Error: {e}")
```

## Next Steps

- [ArabPyTranslator](/docs/api/translator) - Detailed translator API
- [arabic_code_runner](/docs/api/runner) - Execution API
- [ARABIC_TRANSLATIONS](/docs/api/dictionary) - Dictionary API
