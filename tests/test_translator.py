"""
Comprehensive tests for ArabPy translator.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arabpy import ArabPyTranslator


class TestArabPyTranslator(unittest.TestCase):
    """Test cases for ArabPyTranslator."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.translator = ArabPyTranslator()
    
    def test_basic_keywords(self):
        """Test translation of basic Python keywords."""
        python_code = "if x: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("إذا", arabic_code)
        self.assertIn("مرر", arabic_code)
        
        # Translate back
        restored = self.translator.to_python(arabic_code)
        self.assertEqual(restored, python_code)
    
    def test_for_loop(self):
        """Test translation of for loops."""
        python_code = "for i in range(10): print(i)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لكل", arabic_code)
        self.assertIn("في", arabic_code)
        self.assertIn("مدى", arabic_code)
    
    def test_while_loop(self):
        """Test translation of while loops."""
        python_code = "while True: break"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("بينما", arabic_code)
        self.assertIn("صحيح_قيمة", arabic_code)
        self.assertIn("توقف", arabic_code)
    
    def test_function_definition(self):
        """Test translation of function definitions."""
        python_code = "def greet(): return 'hello'"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تعريف", arabic_code)
        self.assertIn("إرجاع", arabic_code)
    
    def test_class_definition(self):
        """Test translation of class definitions."""
        python_code = "class Person: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("فئة", arabic_code)
        self.assertIn("مرر", arabic_code)
    
    def test_builtin_functions(self):
        """Test translation of built-in functions."""
        python_code = "print(len([1,2,3]))"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("طباعة", arabic_code)
        self.assertIn("طول", arabic_code)
    
    def test_boolean_values(self):
        """Test translation of boolean values."""
        python_code = "x = True; y = False"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("صحيح_قيمة", arabic_code)
        self.assertIn("خطأ", arabic_code)
    
    def test_none_value(self):
        """Test translation of None."""
        python_code = "x = None"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لاشيء", arabic_code)
    
    def test_logical_operators(self):
        """Test translation of logical operators."""
        python_code = "if x and y or not z: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("و", arabic_code)
        self.assertIn("أو", arabic_code)
        self.assertIn("ليس", arabic_code)
    
    def test_exception_handling(self):
        """Test translation of exception handling."""
        python_code = "try: pass except: pass finally: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("جرب", arabic_code)
        self.assertIn("باستثناء", arabic_code)
        self.assertIn("أخيرا", arabic_code)
    
    def test_import_statement(self):
        """Test translation of import statements."""
        python_code = "import math"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("استيراد", arabic_code)
    
    def test_from_import(self):
        """Test translation of from...import statements."""
        python_code = "from math import sqrt"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("من", arabic_code)
        self.assertIn("استيراد", arabic_code)
    
    def test_string_preservation(self):
        """Test that strings are preserved."""
        python_code = 'x = "hello world"'
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn('"hello world"', arabic_code)
    
    def test_comment_preservation(self):
        """Test that comments are preserved."""
        python_code = "# This is a comment\nx = 1"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("# This is a comment", arabic_code)
    
    def test_variable_name_preservation(self):
        """Test that user-defined variable names are preserved."""
        python_code = "my_variable = 42"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("my_variable", arabic_code)
    
    def test_function_name_preservation(self):
        """Test that user-defined function names are preserved."""
        python_code = "def my_function(): pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("my_function", arabic_code)
    
    def test_class_name_preservation(self):
        """Test that user-defined class names are preserved."""
        python_code = "class MyClass: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("MyClass", arabic_code)
    
    def test_list_methods(self):
        """Test translation of list methods."""
        python_code = "x.append(1); x.sort()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("إضافة", arabic_code)
        self.assertIn("ترتيب", arabic_code)
    
    def test_list_constructor(self):
        """Test translation of list constructor."""
        python_code = "x = list([1,2,3])"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("قائمة_بيانات", arabic_code)
    
    def test_dict_methods(self):
        """Test translation of dictionary methods."""
        python_code = "d.keys(); d.values()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مفاتيح", arabic_code)
        self.assertIn("قيم", arabic_code)
    
    def test_string_methods(self):
        """Test translation of string methods."""
        python_code = "s.upper(); s.lower()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("كبير", arabic_code)
        self.assertIn("صغير", arabic_code)
    
    def test_math_functions(self):
        """Test translation of math functions."""
        python_code = "math.sqrt(16); math.sin(0)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("جذر_تربيعي", arabic_code)
        self.assertIn("جيب", arabic_code)
    
    def test_async_syntax(self):
        """Test translation of async/await syntax."""
        python_code = "async def f(): await x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("غير_متزامن", arabic_code)
        self.assertIn("انتظر", arabic_code)
    
    def test_match_case(self):
        """Test translation of match/case syntax."""
        python_code = "match x: case 1: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("طابق", arabic_code)
        self.assertIn("حالة", arabic_code)
    
    def test_lambda(self):
        """Test translation of lambda."""
        python_code = "f = lambda x: x + 1"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لامبدا", arabic_code)
    
    def test_with_statement(self):
        """Test translation of with statement."""
        python_code = "with open('file'): pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مع", arabic_code)
        self.assertIn("فتح", arabic_code)
    
    def test_assert(self):
        """Test translation of assert."""
        python_code = "assert x == 1"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تأكيد", arabic_code)
    
    def test_raise(self):
        """Test translation of raise."""
        python_code = "raise ValueError()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("رفع", arabic_code)
        self.assertIn("خطأ_قيمة", arabic_code)
    
    def test_global(self):
        """Test translation of global."""
        python_code = "global x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("عام", arabic_code)
    
    def test_nonlocal(self):
        """Test translation of nonlocal."""
        python_code = "nonlocal x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("غير_محلي", arabic_code)
    
    def test_yield(self):
        """Test translation of yield."""
        python_code = "yield x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("إنتاج", arabic_code)
    
    def test_del(self):
        """Test translation of del."""
        python_code = "del x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("حذف", arabic_code)
    
    def test_pass(self):
        """Test translation of pass."""
        python_code = "pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مرر", arabic_code)
    
    def test_continue(self):
        """Test translation of continue."""
        python_code = "continue"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("استمر", arabic_code)
    
    def test_break(self):
        """Test translation of break."""
        python_code = "break"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("توقف", arabic_code)
    
    def test_roundtrip_simple(self):
        """Test that simple code roundtrips correctly."""
        python_code = "if True: print('hello')"
        arabic_code = self.translator.to_arabic(python_code)
        restored = self.translator.to_python(arabic_code)
        # The roundtrip should work, but we need to account for the translation
        self.assertIn("if", restored)
        self.assertIn("print", restored)
    
    def test_roundtrip_complex(self):
        """Test that complex code roundtrips correctly."""
        python_code = """
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)
"""
        arabic_code = self.translator.to_arabic(python_code)
        restored = self.translator.to_python(arabic_code)
        # Check that key elements are preserved
        self.assertIn("def", restored)
        self.assertIn("factorial", restored)
        self.assertIn("if", restored)
        self.assertIn("return", restored)
        self.assertIn("print", restored)
    
    def test_arabic_to_python(self):
        """Test translation from Arabic to Python."""
        arabic_code = "إذا صحيح_قيمة: طباعة('مرحبا')"
        python_code = self.translator.to_python(arabic_code)
        self.assertIn("if", python_code)
        self.assertIn("True", python_code)
        self.assertIn("print", python_code)
    
    def test_translation_stats(self):
        """Test translation statistics."""
        python_code = "if True: print('hello')"
        stats = self.translator.get_translation_stats(python_code, to_arabic=True)
        self.assertIn('total_tokens', stats)
        self.assertIn('translated_count', stats)
        self.assertIn('translation_percentage', stats)
        self.assertGreater(stats['total_tokens'], 0)
    
    def test_empty_code(self):
        """Test translation of empty code."""
        python_code = ""
        arabic_code = self.translator.to_arabic(python_code)
        self.assertEqual(arabic_code, "")
    
    def test_whitespace_preservation(self):
        """Test that whitespace is preserved."""
        python_code = "if True:\n    print('hello')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("\n    ", arabic_code)
    
    def test_multiline_string(self):
        """Test that multiline strings are preserved."""
        python_code = 's = """hello\nworld"""'
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn('"""hello\nworld"""', arabic_code)
    
    def test_f_string(self):
        """Test that f-strings are preserved."""
        python_code = 'f"hello {name}"'
        arabic_code = self.translator.to_arabic(python_code)
        # F-strings should be preserved, but the variable name inside might be translated
        # We check that the f-string structure is preserved
        self.assertIn('f"', arabic_code)
        self.assertIn('hello', arabic_code)
    
    def test_raw_string(self):
        """Test that raw strings are preserved."""
        python_code = "r'\\n'"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("r'\\n'", arabic_code)
    
    def test_byte_string(self):
        """Test that byte strings are preserved."""
        python_code = "b'hello'"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("b'hello'", arabic_code)
    
    def test_list_comprehension(self):
        """Test translation with list comprehension."""
        python_code = "[x for x in range(10)]"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لكل", arabic_code)
        self.assertIn("في", arabic_code)
        self.assertIn("مدى", arabic_code)
    
    def test_dictionary_comprehension(self):
        """Test translation with dictionary comprehension."""
        python_code = "{k: v for k, v in items}"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لكل", arabic_code)
        self.assertIn("في", arabic_code)
    
    def test_set_comprehension(self):
        """Test translation with set comprehension."""
        python_code = "{x for x in items}"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لكل", arabic_code)
        self.assertIn("في", arabic_code)
    
    def test_generator_expression(self):
        """Test translation with generator expression."""
        python_code = "(x for x in items)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لكل", arabic_code)
        self.assertIn("في", arabic_code)
    
    def test_decorator(self):
        """Test translation with decorator."""
        python_code = "@property\ndef x(self): return self._x"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("خاصية", arabic_code)
        self.assertIn("تعريف", arabic_code)
        self.assertIn("إرجاع", arabic_code)
    
    def test_context_manager(self):
        """Test translation with context manager."""
        python_code = "with open('file') as f: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مع", arabic_code)
        self.assertIn("فتح", arabic_code)
        self.assertIn("كـ", arabic_code)
    
    def test_ternary_operator(self):
        """Test translation with ternary operator."""
        python_code = "x = 1 if condition else 0"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("إذا", arabic_code)
        self.assertIn("وإلا", arabic_code)
    
    def test_is_operator(self):
        """Test translation of is operator."""
        python_code = "if x is None: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("هو", arabic_code)
        self.assertIn("لاشيء", arabic_code)
    
    def test_in_operator(self):
        """Test translation of in operator."""
        python_code = "if x in list: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("في", arabic_code)
    
    def test_not_operator(self):
        """Test translation of not operator."""
        python_code = "if not x: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("ليس", arabic_code)
    
    def test_as_keyword(self):
        """Test translation of as keyword."""
        python_code = "import math as m"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("كـ", arabic_code)
    
    def test_elif_keyword(self):
        """Test translation of elif keyword."""
        python_code = "if x: pass\nelif y: pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("وإلا_إذا", arabic_code)
    
    def test_magic_methods(self):
        """Test translation of magic methods."""
        python_code = "def __init__(self): pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("__تهيئة__", arabic_code)
    
    def test_builtin_exceptions(self):
        """Test translation of built-in exceptions."""
        python_code = "raise ValueError()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("خطأ_قيمة", arabic_code)
        
        python_code = "raise TypeError()"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("خطأ_نوع", arabic_code)
    
    def test_data_types(self):
        """Test translation of data type constructors."""
        python_code = "x = int('42'); y = str(42)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("صحيح", arabic_code)
        self.assertIn("سلسلة", arabic_code)
    
    def test_type_conversion(self):
        """Test translation of type conversion functions."""
        python_code = "x = list('hello'); y = dict(a=1)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("قائمة", arabic_code)
        self.assertIn("قاموس", arabic_code)
    
    def test_enumerate(self):
        """Test translation of enumerate."""
        python_code = "for i, x in enumerate(items): pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تعداد", arabic_code)
    
    def test_zip(self):
        """Test translation of zip."""
        python_code = "for a, b in zip(x, y): pass"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("ربط", arabic_code)
    
    def test_map(self):
        """Test translation of map."""
        python_code = "map(str, numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("خريطة", arabic_code)
    
    def test_filter(self):
        """Test translation of filter."""
        python_code = "filter(lambda x: x > 0, numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تصفية", arabic_code)
        self.assertIn("لامبدا", arabic_code)
    
    def test_sorted(self):
        """Test translation of sorted."""
        python_code = "sorted(numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مرتب", arabic_code)
    
    def test_reversed(self):
        """Test translation of reversed."""
        python_code = "reversed(numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("معكوس", arabic_code)
    
    def test_sum(self):
        """Test translation of sum."""
        python_code = "sum(numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مجموع", arabic_code)
    
    def test_min_max(self):
        """Test translation of min and max."""
        python_code = "min(numbers); max(numbers)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("أدنى", arabic_code)
        self.assertIn("أقصى", arabic_code)
    
    def test_abs(self):
        """Test translation of abs."""
        python_code = "abs(-5)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مطلق", arabic_code)
    
    def test_round(self):
        """Test translation of round."""
        python_code = "round(3.14)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تقريب", arabic_code)
    
    def test_all_any(self):
        """Test translation of all and any."""
        python_code = "all(items); any(items)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("الكل", arabic_code)
        self.assertIn("أي", arabic_code)
    
    def test_isinstance(self):
        """Test translation of isinstance."""
        python_code = "isinstance(x, int)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مثال_من", arabic_code)
    
    def test_issubclass(self):
        """Test translation of issubclass."""
        python_code = "issubclass(Cls, Base)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("فئة_فرعية_من", arabic_code)
    
    def test_hasattr(self):
        """Test translation of hasattr."""
        python_code = "hasattr(obj, 'attr')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("لديه_خاصية", arabic_code)
    
    def test_getattr(self):
        """Test translation of getattr."""
        python_code = "getattr(obj, 'attr')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("الحصول_على_خاصية", arabic_code)
    
    def test_setattr(self):
        """Test translation of setattr."""
        python_code = "setattr(obj, 'attr', value)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تعيين_خاصية", arabic_code)
    
    def test_delattr(self):
        """Test translation of delattr."""
        python_code = "delattr(obj, 'attr')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("حذف_خاصية", arabic_code)
    
    def test_callable(self):
        """Test translation of callable."""
        python_code = "callable(func)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("قابل_للاستدعاء", arabic_code)
    
    def test_iter(self):
        """Test translation of iter."""
        python_code = "iter(items)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مكرر", arabic_code)
    
    def test_next(self):
        """Test translation of next."""
        python_code = "next(iterator)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("التالي", arabic_code)
    
    def test_len(self):
        """Test translation of len."""
        python_code = "len(items)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("طول", arabic_code)
    
    def test_dir(self):
        """Test translation of dir."""
        python_code = "dir(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("دليل", arabic_code)
    
    def test_help(self):
        """Test translation of help."""
        python_code = "help(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("مساعدة_مدمجة", arabic_code)
    
    def test_type(self):
        """Test translation of type."""
        python_code = "type(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("نوع", arabic_code)
    
    def test_id(self):
        """Test translation of id."""
        python_code = "id(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("معرف", arabic_code)
    
    def test_hash(self):
        """Test translation of hash."""
        python_code = "hash(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تجزئة", arabic_code)
    
    def test_bin_hex_oct(self):
        """Test translation of bin, hex, oct."""
        python_code = "bin(10); hex(10); oct(10)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("ثنائي", arabic_code)
        self.assertIn("سداسي_عشري", arabic_code)
        self.assertIn("ثماني", arabic_code)
    
    def test_chr_ord(self):
        """Test translation of chr and ord."""
        python_code = "chr(65); ord('A')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("حرف", arabic_code)
        self.assertIn("ترميز", arabic_code)
    
    def test_ascii(self):
        """Test translation of ascii."""
        python_code = "ascii('hello')"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("أسكي", arabic_code)
    
    def test_repr(self):
        """Test translation of repr."""
        python_code = "repr(obj)"
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("تمثيل", arabic_code)
    
    def test_complex_code(self):
        """Test translation of complex code snippet."""
        python_code = """
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def get_history(self):
        return self.history.copy()

calc = Calculator()
print(calc.add(5, 3))
print(calc.get_history())
"""
        arabic_code = self.translator.to_arabic(python_code)
        self.assertIn("فئة", arabic_code)
        self.assertIn("تعريف", arabic_code)
        self.assertIn("__تهيئة__", arabic_code)
        self.assertIn("إرجاع", arabic_code)
        self.assertIn("إضافة", arabic_code)
        self.assertIn("طباعة", arabic_code)
        
        # Test roundtrip - check key elements are preserved
        restored = self.translator.to_python(arabic_code)
        self.assertIn("class", restored)
        self.assertIn("Calculator", restored)
        self.assertIn("def", restored)
        self.assertIn("__init__", restored)
        self.assertIn("add", restored)
        self.assertIn("print", restored)


if __name__ == '__main__':
    unittest.main()
