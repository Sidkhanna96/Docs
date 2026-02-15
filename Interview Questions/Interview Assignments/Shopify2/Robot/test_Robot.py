from ClassRobot import Robot
import pytest
from unittest.mock import patch, Mock


@pytest.fixture
def rob():
    return Robot()

@patch("ClassRobot.robotRandom", return_value=4)  # Properly mock robotRandom
def test_can_simulate_robot(mock_robot_random, rob):
    finalDest = rob.robotSim([4, -1, 4, -2, 4], [[2, 4]])

    # Assert that robotRandom was called once
    mock_robot_random.assert_called_once()

    # Assert the final destination is as expected
    assert finalDest == 65


def test_when_input_not_list_fail(rob):
    with pytest.raises(ValueError):
        rob.robotSim("", [[2, 4]])

    with pytest.raises(ValueError): 
        rob.robotSim([4, -1, 4, -2, 4], "")

def test_when_command_passed_to_turn(rob):
    rob.curDirections = "NORTH"
    rob.turn(-2)
    assert rob.curDirections == "WEST"

def test_move_happy_path(rob):
    rob.curPos = (0, 0)
    rob.curDirections = "NORTH"
    rob.maxDist = 0
    rob.move(3, [])
    assert rob.curPos == (0, 3)
    assert rob.maxDist == 9



    
