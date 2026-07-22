"""
Comprehensive tests for arabic_code_runner function.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arabpy import arabic_code_runner


class TestArabicCodeRunner(unittest.TestCase):
    """Test cases for arabic_code_runner function."""
    
    def test_print_statement(self):
        """Test execution of print statements."""
        code = 'طباعة(123)'
        result = arabic_code_runner(code)
        self.assertIn('__builtins__', result)
    
    def test_if_statement(self):
        """Test execution of if statements."""
        code = '''
إذا 5 > 3:
    x = 1
وإلا:
    x = 0
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 1)
    
    def test_for_loop(self):
        """Test execution of for loops."""
        code = '''
total = 0
لكل i في مدى(5):
    total = total + i
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['total'], 10)  # 0+1+2+3+4 = 10
    
    def test_while_loop(self):
        """Test execution of while loops."""
        code = '''
x = 0
بينما x < 5:
    x = x + 1
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 5)
    
    def test_function_definition(self):
        """Test execution of function definitions."""
        code = '''
تعريف add(a, b):
    إرجاع a + b

result = add(10, 20)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['result'], 30)
    
    def test_function_call(self):
        """Test calling defined functions."""
        code = '''
تعريف multiply(a, b):
    إرجاع a * b

x = multiply(3, 4)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 12)
    
    def test_exception_handling(self):
        """Test exception handling."""
        code = '''
جرب:
    x = 1 / 0
باستثناء:
    x = 1
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 1)
    
    def test_raise_exception(self):
        """Test raising exceptions."""
        code = '''
تعريف f():
    رفع ValueError

جرب:
    f()
باستثناء ValueError كـ e:
    x = 1
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 1)
    
    def test_unicode_strings(self):
        """Test Unicode string handling."""
        code = '''
x = "test"
y = "Hello World"
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 'test')
        self.assertEqual(result['y'], 'Hello World')
    
    def test_variables(self):
        """Test variable assignment and retrieval."""
        code = '''
x = 10
y = 3.14
z = "text"
w = [1, 2, 3]
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 10)
        self.assertEqual(result['y'], 3.14)
        self.assertEqual(result['z'], 'text')
        self.assertEqual(result['w'], [1, 2, 3])
    
    def test_nested_blocks(self):
        """Test nested code blocks."""
        code = '''
لكل i في مدى(3):
    لكل j في مدى(2):
        إذا i == j:
            x = 1
        وإلا:
            x = 0
'''
        result = arabic_code_runner(code)
        self.assertIn('x', result)
    
    def test_class_definition(self):
        """Test class definition and usage."""
        code = '''
فئة TestClass:
    تعريف __init__(self, value):
        self.value = value
    
    تعريف get(self):
        إرجاع self.value

obj = TestClass(42)
x = obj.get()
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 42)
    
    def test_boolean_values(self):
        """Test boolean value handling."""
        code = '''
x_true = صحيح_قيمة
x_false = خطأ
'''
        result = arabic_code_runner(code)
        self.assertTrue(result['x_true'])
        self.assertFalse(result['x_false'])
    
    def test_none_value(self):
        """Test None value handling."""
        code = '''
x = لاشيء
'''
        result = arabic_code_runner(code)
        self.assertIsNone(result['x'])
    
    def test_list_operations(self):
        """Test list operations."""
        code = '''
my_list = [1, 2, 3]
my_list.append(4)
length = len(my_list)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['length'], 4)
    
    def test_dict_operations(self):
        """Test dictionary operations."""
        code = '''
my_dict = {"a": 1, "b": 2}
value = my_dict["a"]
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['value'], 1)
    
    def test_math_operations(self):
        """Test mathematical operations."""
        code = '''
x = 10 + 5
y = 10 - 5
z = 10 * 5
w = 10 / 5
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 15)
        self.assertEqual(result['y'], 5)
        self.assertEqual(result['z'], 50)
        self.assertEqual(result['w'], 2.0)
    
    def test_logical_operators(self):
        """Test logical operators."""
        code = '''
x_and = صحيح_قيمة و خطأ
x_or = صحيح_قيمة أو خطأ
x_not = ليس صحيح_قيمة
'''
        result = arabic_code_runner(code)
        self.assertFalse(result['x_and'])
        self.assertTrue(result['x_or'])
        self.assertFalse(result['x_not'])
    
    def test_comparison_operators(self):
        """Test comparison operators."""
        code = '''
x_greater = 5 > 3
x_less = 5 < 3
x_equal = 5 == 5
x_not_equal = 5 != 3
'''
        result = arabic_code_runner(code)
        self.assertTrue(result['x_greater'])
        self.assertFalse(result['x_less'])
        self.assertTrue(result['x_equal'])
        self.assertTrue(result['x_not_equal'])
    
    def test_type_validation(self):
        """Test that TypeError is raised for non-string input."""
        with self.assertRaises(TypeError):
            arabic_code_runner(123)
        
        with self.assertRaises(TypeError):
            arabic_code_runner(None)
        
        with self.assertRaises(TypeError):
            arabic_code_runner([])
    
    def test_empty_string(self):
        """Test execution of empty string."""
        result = arabic_code_runner('')
        self.assertIn('__builtins__', result)
    
    def test_syntax_error_preservation(self):
        """Test that syntax errors are properly reported."""
        code = '''
تعريف ف(:
    إرجاع 1
'''
        with self.assertRaises(SyntaxError):
            arabic_code_runner(code)
    
    def test_runtime_error_preservation(self):
        """Test that runtime errors preserve traceback."""
        code = '''
x = 1 / 0
'''
        with self.assertRaises(ZeroDivisionError):
            arabic_code_runner(code)
    
    def test_indentation_preservation(self):
        """Test that indentation is preserved correctly."""
        code = '''
تعريف f():
    x = 1
    y = 2
    إرجاع x
'''
        result = arabic_code_runner(code)
        self.assertIn('x', result)
    
    def test_string_preservation(self):
        """Test that strings are not modified."""
        code = '''
x = "def"
y = "if"
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 'def')
        self.assertEqual(result['y'], 'if')
    
    def test_comment_preservation(self):
        """Test that comments are preserved."""
        code = '''
# This is a comment
x = 10
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 10)
    
    def test_multiple_statements(self):
        """Test multiple statements in one execution."""
        code = '''
x = 10
y = x * 2
z = x * x
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 10)
        self.assertEqual(result['y'], 20)
        self.assertEqual(result['z'], 100)
    
    def test_return_value(self):
        """Test that the function returns the globals dictionary."""
        code = '''
x = 42
'''
        result = arabic_code_runner(code)
        self.assertIsInstance(result, dict)
        self.assertIn('x', result)
        self.assertEqual(result['x'], 42)
    
    def test_builtin_functions(self):
        """Test built-in function calls."""
        code = '''
my_list = [3, 1, 2]
sorted_list = sorted(my_list)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['sorted_list'], [1, 2, 3])
    
    def test_lambda(self):
        """Test lambda expressions."""
        code = '''
f = lambda a: a * 2
result = f(5)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['result'], 10)
    
    def test_list_comprehension(self):
        """Test list comprehension."""
        code = '''
result = [a * 2 لكل a في مدى(5)]
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['result'], [0, 2, 4, 6, 8])


if __name__ == '__main__':
    unittest.main()
