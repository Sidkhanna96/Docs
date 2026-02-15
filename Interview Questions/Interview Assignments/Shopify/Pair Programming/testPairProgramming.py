import pytest
from pairProgramming import Robot

print("HELLO")

class PairProgrammingTest:

    def setup_method(self):
        self.rover = Robot()

    def test_move_down(self):
        """
        Testing Move functionality down
        """
        self.rover = Robot()
        self.rover._move()
        print("HERE")
        assert self.rover.point == (0,-1)