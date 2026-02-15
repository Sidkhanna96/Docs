import pytest
from SysArg import main
from unittest.mock import patch
import sys

def test_should_run_properly():
    with patch.object(sys, "argv", ["main", "[1, 2]"]):
        with patch("SysArg.randInt", return_value=3) as mock_randint:
            with patch("builtins.print") as mock_print:
                main()

                assert sys.argv == ["main", "[1, 2]"]

                mock_randint.assert_called_once()

                mock_print.assert_any_call(3)

def test_should_raise_error_when_command_is_string():
    with patch.object(sys, "argv", ["main", "incorrect_value"]):
        with pytest.raises(ValueError):
            main()



