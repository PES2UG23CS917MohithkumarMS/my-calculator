"""
Unit Tests for Calculator
Covers add, subtract, multiply, divide, power, and square_root
"""

import pytest
from src.calculator import add, subtract, multiply, divide, power, square_root
import math


class TestBasicOperations:
    """Test basic arithmetic operations"""

    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
        assert add(10, 15) == 25

    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6


class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation"""

    def test_multiply_input_validation(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)


class TestMultiplyDivide:
    """Test multiplication and division operations"""

    def test_multiply_positive_numbers(self):
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20

    def test_multiply_negative_numbers(self):
        assert multiply(-2, 3) == -6
        assert multiply(-2, -3) == 6

    def test_divide_positive_numbers(self):
        assert divide(6, 3) == 2
        assert divide(20, 5) == 4

    def test_divide_by_zero(self):
        with pytest.raises(ValueError, match="division by zero"):
            divide(5, 0)


class TestPowerSquareRoot:
    """Test exponentiation and square root functions"""

    def test_power_positive_numbers(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1

    def test_power_input_validation(self):
        with pytest.raises(TypeError):
            power("2", 3)
        with pytest.raises(TypeError):
            power(2, "3")

    def test_square_root_positive_numbers(self):
        assert square_root(16) == 4
        assert math.isclose(square_root(2), math.sqrt(2))

    def test_square_root_negative_number(self):
        with pytest.raises(ValueError, match="negative number"):
            square_root(-1)

    def test_square_root_input_validation(self):
        with pytest.raises(TypeError):
            square_root("16")
