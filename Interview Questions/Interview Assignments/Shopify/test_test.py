import pytest
from test import Packaging

# result = Packaging(["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"])
# result.package()

class TestTestClass:

    def setup_method(self):
        self.testPackaging = Packaging(["Cam", "Cam", "Cam", "Game", "Game", "Cam", "Cam", "Blue", "Blue"])

    def test_add(self):
        result  = self.testPackaging.package()
        assert result == [[3, 'Cam'], [2, 'Game'], [2, 'Blue']]