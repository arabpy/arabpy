"""
Simple tests for arabic_code_runner function.
"""

import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from arabpy import arabic_code_runner


class TestArabicCodeRunnerSimple(unittest.TestCase):
    """Simple test cases for arabic_code_runner function."""
    
    def test_basic_assignment(self):
        """Test basic variable assignment."""
        code = 'x = 10'
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 10)
    
    def test_if_statement(self):
        """Test if statement."""
        code = '''
إذا 5 > 3:
    x = 1
وإلا:
    x = 0
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 1)
    
    def test_for_loop(self):
        """Test for loop."""
        code = '''
total = 0
لكل i في مدى(5):
    total = total + i
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['total'], 10)
    
    def test_while_loop(self):
        """Test while loop."""
        code = '''
x = 0
بينما x < 5:
    x = x + 1
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['x'], 5)
    
    def test_function_definition(self):
        """Test function definition."""
        code = '''
تعريف add(a, b):
    إرجاع a + b

result = add(10, 20)
'''
        result = arabic_code_runner(code)
        self.assertEqual(result['result'], 30)
    
    def test_type_validation(self):
        """Test that TypeError is raised for non-string input."""
        with self.assertRaises(TypeError):
            arabic_code_runner(123)
    
    def test_empty_string(self):
        """Test execution of empty string."""
        result = arabic_code_runner('')
        self.assertIn('__builtins__', result)
    
    def test_return_value(self):
        """Test that the function returns the globals dictionary."""
        code = 'x = 42'
        result = arabic_code_runner(code)
        self.assertIsInstance(result, dict)
        self.assertIn('x', result)
        self.assertEqual(result['x'], 42)


if __name__ == '__main__':
    unittest.main()
