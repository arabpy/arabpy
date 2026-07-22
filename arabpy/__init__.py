"""
ArabPy - Write Python completely in Arabic

A professional Python library that allows writing Python code using Arabic keywords
and identifiers while preserving the ability to use normal Python after translation.
"""

from .translator import ArabPyTranslator
from .dictionary import ARABIC_TRANSLATIONS
from .runner import arabic_code_runner

__version__ = "1.0.0"
__all__ = ["ArabPyTranslator", "ARABIC_TRANSLATIONS", "arabic_code_runner"]
