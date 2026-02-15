import pytest
from unittest.mock import patch
from ShopifyQuestion import TestClass, main

def test_should_print_hello_world():
    t = TestClass()

    with patch("builtins.print") as mockPrint:
        t.test()
        mockPrint.assert_called_once()
        mockPrint.assert_called_with("Hello World")


def test_should_print_hello_world_with_main():
    with patch("builtins.print") as mockPrint:
        main()
        mockPrint.assert_called_once()
        mockPrint.assert_called_with("Hello World")