from typing import List
import random

def robotRandom():
    return random.randrange(1, 5)

class Robot:
    def __init__(self) -> None:
        pass

    def move(self, command: int, obstacles: List) -> None:
        self.dir = {"NORTH": (0,1),
                    "SOUTH": (0,-1),
                    "WEST": (-1,0),
                    "EAST": (1,0)}
        i = 0
        d1, d2 = self.dir[self.curDirections]

        while i < command: 
            
            newRow, newCol = self.curPos[0] + d1, self.curPos[1] + d2
            if (newRow, newCol) in obstacles:
                break
            
            self.curPos = (newRow, newCol)
            self.maxDist = max(self.maxDist, newRow**2 + newCol**2)
            i += 1
            

    def turn(self, command: List) -> None:
        directions = {
            "NORTH": {-2: "WEST", -1:"EAST"},
            "EAST":  {-2: "NORTH", -1: "SOUTH"},
            "SOUTH": {-2: "EAST",  -1: "WEST"},
            "WEST":  {-2: "SOUTH", -1: "NORTH"}
            }

        self.curDirections = directions[self.curDirections][command]

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        if not isinstance(commands, list) or not isinstance(obstacles, list):
            raise ValueError(f"Commands and obstacles must be of type List. Got {type(commands)} and {type(obstacles)}.")
        
        randIntVal = robotRandom()
        
        self.curPos = (0,0)
        self.curDirections = "NORTH"
        self.maxDist = 0 
        setObstacles = set(map(tuple, obstacles))

        for command in commands:
            if command in {-1,-2}:
                self.turn(command)
            else:
                self.move(command, setObstacles)

        return self.maxDist
    


def main():
    rob = Robot()

    print(rob.robotSim([4, -1, 3], []))
    print(rob.robotSim([4, -1, 4, -2, 4], [[2, 4]]))
    print(rob.robotSim([6, -1, -1, 6], [[0, 0]]))


if __name__ == "__main__":
    main()

