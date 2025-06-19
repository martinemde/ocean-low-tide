#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive Python syntax for theme color testing.

This module contains various Python constructs to test syntax highlighting.
"""

import os
import sys
import json
import asyncio
from typing import Dict, List, Optional, Union, Tuple, Any, TypeVar, Generic
from collections import defaultdict, namedtuple
from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto
from abc import ABC, abstractmethod
from contextlib import contextmanager
import re

# Comments and docstrings
# Single line comment
"""
Multi-line string that can serve as documentation
"""

# Constants and variables
CONSTANT_VALUE = 42
_PRIVATE_CONSTANT = "private"
__DUNDER_CONSTANT = "dunder"

# Numbers and literals
integer = 123
float_num = 3.14159
scientific = 1.23e-4
negative = -456
binary = 0b1010
octal = 0o777
hexadecimal = 0xFF
complex_num = 3 + 4j

# Strings and formatting
single_quoted = 'single quoted string'
double_quoted = "double quoted string"
triple_single = '''triple single quoted
multiline string'''
triple_double = """triple double quoted
multiline string"""

# String formatting
name = "World"
formatted_string = f"Hello, {name}!"
old_format = "Hello, {}!".format(name)
old_style = "Hello, %s!" % name

# Raw strings
raw_string = r"Raw string with \n no escaping"
unicode_string = "Unicode: 🐍 ñ ü"

# Bytes
byte_string = b"byte string"
byte_array = bytearray(b"mutable bytes")

# Collections
list_example = [1, 2, 3, "mixed", True, None]
tuple_example = (1, 2, 3)
set_example = {1, 2, 3, 4}
dict_example = {
    "key": "value",
    1: "number key",
    (1, 2): "tuple key",
    **{"spread": "operator"}
}

# List/dict/set comprehensions
list_comp = [x**2 for x in range(10) if x % 2 == 0]
dict_comp = {k: v**2 for k, v in enumerate(range(5))}
set_comp = {x for x in range(10) if x % 2 == 0}
generator_exp = (x**2 for x in range(10))

# Boolean and None
true_val = True
false_val = False
none_val = None

# Operators
arithmetic = 1 + 2 - 3 * 4 / 5 // 6 % 7 ** 8
comparison = 1 < 2 <= 3 > 4 >= 5 == 6 != 7
logical = True and False or not True
bitwise = 1 & 2 | 3 ^ 4 << 5 >> 6
assignment = 1
assignment += 2
assignment -= 1
assignment *= 2
assignment /= 2
assignment //= 2
assignment %= 2
assignment **= 2
assignment &= 1
assignment |= 1
assignment ^= 1
assignment <<= 1
assignment >>= 1

# Membership and identity
membership = 1 in [1, 2, 3]
identity = 1 is not None

# Class definitions
class BaseClass:
    """Base class with various features."""

    class_variable = "shared"
    _protected = "protected"
    __private = "private"

    def __init__(self, value: int = 0):
        self.instance_variable = value
        self._protected_instance = "protected"
        self.__private_instance = "private"

    def instance_method(self) -> str:
        """Instance method with type hints."""
        return f"Instance method: {self.instance_variable}"

    @classmethod
    def class_method(cls) -> str:
        """Class method."""
        return f"Class method: {cls.class_variable}"

    @staticmethod
    def static_method(param: str) -> str:
        """Static method."""
        return f"Static method: {param}"

    @property
    def computed_property(self) -> int:
        """Property decorator."""
        return self.instance_variable * 2

    @computed_property.setter
    def computed_property(self, value: int) -> None:
        self.instance_variable = value // 2

    def __str__(self) -> str:
        return f"BaseClass({self.instance_variable})"

    def __repr__(self) -> str:
        return f"BaseClass(value={self.instance_variable})"

    def __len__(self) -> int:
        return self.instance_variable

    def __getitem__(self, key: int) -> int:
        return self.instance_variable + key

    def __setitem__(self, key: int, value: int) -> None:
        self.instance_variable = value - key

# Inheritance
class DerivedClass(BaseClass):
    """Derived class demonstrating inheritance."""

    def __init__(self, value: int = 0, extra: str = ""):
        super().__init__(value)
        self.extra = extra

    def instance_method(self) -> str:
        """Override parent method."""
        parent_result = super().instance_method()
        return f"{parent_result} + {self.extra}"

# Multiple inheritance
class Mixin:
    """Mixin class."""

    def mixin_method(self) -> str:
        return "Mixin functionality"

class MultipleInheritance(BaseClass, Mixin):
    """Class with multiple inheritance."""
    pass

# Abstract base class
class AbstractClass(ABC):
    """Abstract base class."""

    @abstractmethod
    def abstract_method(self) -> str:
        """Abstract method that must be implemented."""
        pass

    def concrete_method(self) -> str:
        """Concrete method in abstract class."""
        return "Concrete implementation"

# Dataclass
@dataclass
class DataClassExample:
    """Dataclass with various field types."""
    name: str
    age: int
    active: bool = True
    tags: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

# Named tuple
Point = namedtuple('Point', ['x', 'y'])
point = Point(1, 2)

# Enum
class Color(Enum):
    """Enum example."""
    RED = 1
    GREEN = 2
    BLUE = 3

class Status(IntEnum):
    """IntEnum example."""
    PENDING = auto()
    RUNNING = auto()
    COMPLETE = auto()

# Generic types
T = TypeVar('T')
U = TypeVar('U', bound=str)

class GenericClass(Generic[T]):
    """Generic class example."""

    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

# Function definitions
def simple_function(param: str) -> str:
    """Simple function with type hints."""
    return f"Hello, {param}!"

def function_with_defaults(a: int, b: int = 10, c: str = "default") -> Tuple[int, str]:
    """Function with default parameters."""
    return a + b, c

def function_with_args(*args: int, **kwargs: str) -> Dict[str, Any]:
    """Function with *args and **kwargs."""
    return {"args": args, "kwargs": kwargs}

def function_with_annotations(
    required: str,
    optional: Optional[int] = None,
    *args: str,
    keyword_only: bool = False,
    **kwargs: Any
) -> Union[str, int]:
    """Function with various parameter types."""
    if keyword_only:
        return len(required)
    return required

# Lambda functions
lambda_simple = lambda x: x * 2
lambda_complex = lambda x, y=10: x + y if x > 0 else y

# Decorators
def decorator_function(func):
    """Simple decorator."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def parametrized_decorator(param: str):
    """Parametrized decorator."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator param: {param}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_function
@parametrized_decorator("test")
def decorated_function(x: int) -> int:
    """Function with multiple decorators."""
    return x * 2

# Control flow
def control_flow_examples():
    """Examples of control flow statements."""

    # If statements
    x = 10
    if x > 0:
        print("positive")
    elif x < 0:
        print("negative")
    else:
        print("zero")

    # Ternary operator
    result = "positive" if x > 0 else "non-positive"

    # For loops
    for i in range(10):
        if i == 5:
            continue
        if i == 8:
            break
        print(i)

    for item in ["a", "b", "c"]:
        print(item)

    for key, value in {"a": 1, "b": 2}.items():
        print(f"{key}: {value}")

    # While loop
    count = 0
    while count < 5:
        count += 1
        if count == 3:
            continue

    # Match statement (Python 3.10+)
    def match_example(value):
        match value:
            case 1:
                return "one"
            case 2 | 3:
                return "two or three"
            case x if x > 10:
                return "greater than ten"
            case [1, 2, *rest]:
                return f"list starting with 1, 2: {rest}"
            case {"name": str(name), "age": int(age)} if age >= 18:
                return f"adult named {name}"
            case _:
                return "default case"

# Exception handling
def exception_examples():
    """Exception handling examples."""

    try:
        risky_operation()
    except ValueError as e:
        print(f"ValueError: {e}")
    except (TypeError, AttributeError) as e:
        print(f"Type or Attribute error: {e}")
    except Exception as e:
        print(f"General exception: {e}")
    else:
        print("No exception occurred")
    finally:
        print("Cleanup code")

    # Raising exceptions
    raise ValueError("Custom error message")

# Custom exception
class CustomException(Exception):
    """Custom exception class."""

    def __init__(self, message: str, code: int = 0):
        super().__init__(message)
        self.code = code

# Context managers
@contextmanager
def custom_context_manager():
    """Custom context manager."""
    print("Entering context")
    try:
        yield "context value"
    finally:
        print("Exiting context")

def context_manager_examples():
    """Context manager usage examples."""

    with open("file.txt", "r") as f:
        content = f.read()

    with custom_context_manager() as value:
        print(f"Context value: {value}")

# Async/await
async def async_function(delay: float = 1.0) -> str:
    """Async function example."""
    await asyncio.sleep(delay)
    return "Async result"

async def async_generator():
    """Async generator example."""
    for i in range(5):
        yield i
        await asyncio.sleep(0.1)

async def async_context_manager():
    """Async context manager example."""
    async with some_async_context():
        result = await async_function()
        return result

# Regular expressions
pattern = re.compile(r'\d+\.\d+')
match = pattern.search("Version 1.23.4")
if match:
    version = match.group()

# File operations
def file_operations():
    """File operation examples."""

    # Reading files
    with open("data.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Writing files
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("Hello, World!\n")
        f.writelines(["Line 1\n", "Line 2\n"])

    # JSON operations
    data = {"key": "value", "number": 42}
    with open("data.json", "w") as f:
        json.dump(data, f, indent=2)

    with open("data.json", "r") as f:
        loaded_data = json.load(f)

# Built-in functions
def builtin_examples():
    """Examples using built-in functions."""

    # Map, filter, reduce
    numbers = list(range(10))
    squared = list(map(lambda x: x**2, numbers))
    evens = list(filter(lambda x: x % 2 == 0, numbers))

    # Zip and enumerate
    letters = ['a', 'b', 'c']
    for i, (num, letter) in enumerate(zip(numbers, letters)):
        print(f"{i}: {num} -> {letter}")

    # Any, all
    has_even = any(x % 2 == 0 for x in numbers)
    all_positive = all(x >= 0 for x in numbers)

    # Min, max, sum
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)

    # Sorted, reversed
    sorted_desc = sorted(numbers, reverse=True)
    reversed_list = list(reversed(numbers))

# Special methods and protocols
class IterableClass:
    """Class implementing iterator protocol."""

    def __init__(self, data: List[Any]):
        self.data = data

    def __iter__(self):
        return iter(self.data)

    def __len__(self):
        return len(self.data)

    def __contains__(self, item):
        return item in self.data

# Metaclass
class MetaClass(type):
    """Metaclass example."""

    def __new__(cls, name, bases, attrs):
        attrs['meta_attribute'] = 'Added by metaclass'
        return super().__new__(cls, name, bases, attrs)

class ClassWithMeta(metaclass=MetaClass):
    """Class using metaclass."""
    pass

# Module-level code
if __name__ == "__main__":
    # Main execution block
    print("Running as main module")

    # Variable unpacking
    a, b, *rest = [1, 2, 3, 4, 5]
    first, *middle, last = range(10)

    # Dictionary unpacking
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, **dict1}

    # Function calls with unpacking
    args = (1, 2, 3)
    kwargs = {"keyword": "value"}
    result = function_with_args(*args, **kwargs)

    # Walrus operator (Python 3.8+)
    if (n := len("hello")) > 3:
        print(f"Length is {n}")

    # F-string expressions
    value = 42
    print(f"Value: {value}, Hex: {value:x}, Binary: {value:b}")
    print(f"Calculation: {2 + 3 = }")

    # Type checking
    assert isinstance(value, int)
    assert issubclass(DerivedClass, BaseClass)

# Global and nonlocal
global_var = "global"

def outer_function():
    """Function demonstrating nonlocal."""
    outer_var = "outer"

    def inner_function():
        nonlocal outer_var
        global global_var
        outer_var = "modified outer"
        global_var = "modified global"

    inner_function()
    return outer_var

# Special attributes
print(__name__)
print(__file__)
print(__doc__)

# Ellipsis
def placeholder_function():
    """Placeholder function."""
    ...

# Type annotations
def annotated_function(
    param1: List[Dict[str, int]],
    param2: Optional[Tuple[str, ...]],
    param3: Union[int, str, None] = None
) -> Dict[str, Any]:
    """Function with complex type annotations."""
    return {"param1": param1, "param2": param2, "param3": param3}
