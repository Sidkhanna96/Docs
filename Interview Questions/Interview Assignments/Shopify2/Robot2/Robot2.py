import sys
import ast
from typing import List

class Robot:
    def __init__(self) -> None:
        self.curPos = (0,0)
        self.direction = "NORTH"
        self.maxDist = 0

    def reset(self) -> None:
        self.curPos = (0, 0)
        self.direction = "NORTH"
        self.maxDist = 0

    def move(self, command: int, obstacles: List[int]) -> None:
        setObstacles = set(map(tuple, obstacles))
        movingDirection = {"NORTH": (0,1), "SOUTH": (0,-1), "EAST": (1,0), "WEST": (-1,0)}

        d1, d2 = movingDirection[self.direction]
        index = 0

        while index < command:
            newRow, newCol = self.curPos[0] + d1, self.curPos[1] + d2

            if (newRow, newCol) in setObstacles:
                break

            self.curPos = (newRow, newCol)
            self.maxDist = max(self.maxDist, newRow**2 + newCol**2)

            index += 1

    def turn(self, command: int) -> None:
        changeDirection = {"NORTH": {-1: "EAST", -2: "WEST"}, 
                            "SOUTH": {-1: "WEST", -2: "EAST"},
                            "WEST": {-1: "NORTH", -2: "SOUTH"},
                            "EAST": {-1: "SOUTH", -2: "NORTH"}}
        
        self.direction = changeDirection[self.direction][command]
    
    def robotSim(self, commands: List[int], obstacles: List[int]) -> int:
        if not isinstance(commands, list) or not all(isinstance(c, int) for c in commands):
            raise ValueError("Commands must be a list of integers.")
        
        for command in commands:
            if command in {-1, -2}:
                self.turn(command)
            elif 1 <= command <= 9:
                self.move(command, obstacles)
            else:
                raise ValueError("Invalid Command provided")

        return self.maxDist

def main():
    try:
        # Extract arguments from sys.argv
        args = sys.argv[1:]  # Exclude the script name
        if len(args) < 1:
            raise ValueError("At least one argument (commands) is required.")

        # Convert the first argument to a list of commands
        commands = ast.literal_eval(args[0])
        if not isinstance(commands, list) or not all(isinstance(c, int) for c in commands):
            raise ValueError("Commands must be a list of integers.")

        # Convert the second argument (if provided) to a list of obstacles
        obstacles = ast.literal_eval(args[1]) if len(args) > 1 else []
        if not isinstance(obstacles, list) or not all(isinstance(o, list) and len(o) == 2 for o in obstacles):
            raise ValueError("Obstacles must be a list of [x, y] pairs.")

    except ValueError as e:
        print(f"Error: {e}")
        return
    except SyntaxError:
        print("Error: Invalid format for commands or obstacles. Ensure they are valid Python lists.")
        return
    except Exception as e:
        print(f"Error: Unknown error occurred: {e}")
        return

    robotInstance = Robot()

    print(robotInstance.robotSim(commands, obstacles))

    # print(robotInstance.robotSim([4,-1,3], [])) #25
    # print(robotInstance.robotSim([4,-1,4,-2,4], [[2,4]])) #65
    # print(robotInstance.robotSim([6,-1,-1,6], [[0,0]])) #36

if __name__ == "__main__":
    main()