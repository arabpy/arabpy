"""
Arabic code runner for ArabPy.

This module provides a convenient function to execute Python code written in Arabic.
"""

import sys
import traceback
from typing import Dict, Any
from .translator import ArabPyTranslator


def arabic_code_runner(source: str) -> Dict[str, Any]:
    """
    Execute Python code written in Arabic from a string.
    
    This function translates Arabic source code to Python, compiles it, and executes it.
    It returns the globals dictionary after execution so variables can be inspected.
    
    Args:
        source: Arabic source code to execute
        
    Returns:
        Dictionary containing the global namespace after execution
        
    Raises:
        TypeError: If source is not a string
        SyntaxError: If the translated code has syntax errors
        Exception: Any exception raised during execution (with preserved traceback)
        
    Example:
        >>> from arabpy import arabic_code_runner
        >>> 
        >>> code = '''
        >>> اطبع("مرحبا")
        >>> 
        >>> إذا 5 > 3:
        >>>     اطبع("خدام")
        >>> '''
        >>> 
        >>> arabic_code_runner(code)
        مرحبا
        خدام
        {'__builtins__': {...}, ...}
        
        >>> g = arabic_code_runner('''
        >>> س = 10
        >>> اطبع(س)
        >>> ''')
        >>> print(g["س"])
        10
    """
    # Validate input
    if not isinstance(source, str):
        raise TypeError(f"source must be a string, got {type(source).__name__}")
    
    # Create translator instance
    translator = ArabPyTranslator()
    
    # Translate Arabic to Python
    try:
        python_code = translator.to_python(source)
    except Exception as e:
        # Re-raise translation errors with context
        raise RuntimeError(f"Translation failed: {e}") from e
    
    # Replace Arabic comma with regular comma after translation
    python_code = python_code.replace('،', ',')
    
    # Compile the translated code
    try:
        compiled_code = compile(python_code, "<arabpy>", "exec")
    except SyntaxError as e:
        # Enhance syntax error with context
        raise SyntaxError(
            f"Syntax error in translated code: {e}\n"
            f"Translated code:\n{python_code}"
        ) from e
    
    # Execute the compiled code
    globals_dict: Dict[str, Any] = {"__builtins__": __builtins__}
    
    try:
        exec(compiled_code, globals_dict)
    except Exception as e:
        # Preserve the original traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Create a formatted traceback
        tb_lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
        
        # Raise the exception with the original traceback
        raise exc_value.with_traceback(exc_traceback)
    
    return globals_dict
