import importlib.util
import math
import os
import sys
from unittest.mock import patch

import pytest

SCRIPT_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "Calculator.py",
)

spec = importlib.util.spec_from_file_location("calculator_mod", SCRIPT_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules["calculator_mod"] = mod
spec.loader.exec_module(mod)


def _fake_input(returns):
    it = iter(returns)
    def inner(prompt=""):
        return next(it)
    return inner


class TestInput1:
    def test_addition_input(self):
        with patch("builtins.input", _fake_input(["1+2+3"])):
            with patch.object(mod, "print_slow", lambda x: None):
                result = mod.input_1("+")
        assert result == [1.0, 2.0, 3.0]

    def test_subtraction_input(self):
        with patch("builtins.input", _fake_input(["10-5-2"])):
            with patch.object(mod, "print_slow", lambda x: None):
                result = mod.input_1("-")
        assert result == [10.0, 5.0, 2.0]

    def test_multiplication_input(self):
        with patch("builtins.input", _fake_input(["2*3*4"])):
            with patch.object(mod, "print_slow", lambda x: None):
                result = mod.input_1("*")
        assert result == [2.0, 3.0, 4.0]

    def test_division_input(self):
        with patch("builtins.input", _fake_input(["10/2/5"])):
            with patch.object(mod, "print_slow", lambda x: None):
                result = mod.input_1("/")
        assert result == [10.0, 2.0, 5.0]

    def test_invalid_then_valid(self):
        with patch("builtins.input", _fake_input(["abc", "1+2"])):
            with patch.object(mod, "print_slow", lambda x: None):
                result = mod.input_1("+")
        assert result == [1.0, 2.0]


class TestInput2:
    def test_valid(self):
        with patch("builtins.input", _fake_input(["42"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.input_2() == 42.0

    def test_invalid_then_valid(self):
        with patch("builtins.input", _fake_input(["abc", "42"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.input_2() == 42.0


class TestOperations:
    def test_addition(self):
        with patch("builtins.input", _fake_input(["1+2+3"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.addition() == 6.0

    def test_subtraction(self):
        with patch("builtins.input", _fake_input(["10-3-2"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.subtraction() == 5.0

    def test_multiplication(self):
        with patch("builtins.input", _fake_input(["2*3*4"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.multiplication() == 24.0

    def test_division(self):
        with patch("builtins.input", _fake_input(["10/2"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.division() == 5.0

    def test_division_by_zero(self):
        with patch("builtins.input", _fake_input(["10/0", "10/2"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.division() == 5.0

    def test_square(self):
        with patch("builtins.input", _fake_input(["5"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.square_of_x() == 25.0

    def test_square_root(self):
        with patch("builtins.input", _fake_input(["16"])):
            with patch.object(mod, "print_slow", lambda x: None):
                assert mod.square_root_of_x() == 4.0

    def test_negative_square_root(self):
        with patch("builtins.input", _fake_input(["-1"])):
            with patch.object(mod, "print_slow", lambda x: None):
                with pytest.raises((ValueError, OverflowError)):
                    mod.square_root_of_x()
