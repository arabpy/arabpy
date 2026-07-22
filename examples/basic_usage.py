"""
Basic usage examples for ArabPy.
"""

from arabpy import ArabPyTranslator

# Create a translator instance
translator = ArabPyTranslator()

# Example 1: Simple Python to Arabic translation
print("Example 1: Simple translation")
print("=" * 50)

python_code = """
def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, World!")

for i in range(5):
    greet(f"User {i}")
"""

print("Original Python code:")
print(python_code)

arabic_code = translator.to_arabic(python_code)
print("\nTranslated to Arabic:")
print(arabic_code)

# Example 2: Arabic to Python translation
print("\n\nExample 2: Arabic to Python")
print("=" * 50)

arabic_code2 = """
تعريف جمع(أ، ب):
    إرجاع أ + ب

نتيجة = جمع(10، 20)
طباعة(نتيجة)
"""

print("Original Arabic code:")
print(arabic_code2)

python_code2 = translator.to_python(arabic_code2)
print("\nTranslated back to Python:")
print(python_code2)

# Example 3: Roundtrip translation
print("\n\nExample 3: Roundtrip translation")
print("=" * 50)

original = """
class Calculator:
    def __init__(self):
        self.value = 0
    
    def add(self, x):
        self.value += x
        return self.value
    
    def multiply(self, x):
        self.value *= x
        return self.value

calc = Calculator()
print(calc.add(5))
print(calc.multiply(3))
"""

print("Original Python:")
print(original)

to_arabic = translator.to_arabic(original)
print("\nTo Arabic:")
print(to_arabic)

back_to_python = translator.to_python(to_arabic)
print("\nBack to Python:")
print(back_to_python)

print("\nRoundtrip successful:", original.strip() == back_to_python.strip())
