import pytest
from Robot2 import Robot, main
from unittest.mock import patch
import sys

@pytest.fixture
def robotInstance():
    return Robot()


def test_can_move_robot_without_obstacles(robotInstance):
    farthestDistance = robotInstance.robotSim([4,-1,3], [])
    assert farthestDistance == 25

def test_can_move_robot_with_obstacles(robotInstance):
    farthestDistance = robotInstance.robotSim([4,-1,4,-2,4], [[2,4]])
    assert farthestDistance == 65

def test_raise_error_invalid_input(robotInstance):
    with pytest.raises(ValueError): 
        robotInstance.robotSim("{}", [[2,4]])

def test_sys_argv_consumed():
    test_args = ["Robot2.py", "[4, -1, 4, -2, 4]", "[[2, 4]]"]

    with patch.object(sys, "argv", test_args):
        try:
            main()
        except Exception as e:
            pytest.fail(f"main() raised an exception: {e}")
