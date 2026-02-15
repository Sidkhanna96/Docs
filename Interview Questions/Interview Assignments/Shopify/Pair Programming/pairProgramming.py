# CLI App - We pass certain prompts
# Move a Robot around on a 2D plane - Pointing in a direction , Turn to face different directions and move in direction it is facing

# Clarifying:
# Starting Point - Top left of the display
# Maybe x,y axis points and just point on the 2D plain - or maybe just a * interface
# Infinite boundaries

# Example:
# Start: 0,0 - Direction downwards - initial prompt 
# User inputs - Direction point and move towards point
    # Command Changes Direction
    # then move towards that direction

class Robot:
    def __init__(self) -> None:
        self.point = (0,0)
        self.direction = "D"
        self.turnCommand = {"D": "L", "L": "U", "U": "R", "R":"D"}

    def _move(self):
        if self.direction == "D":
            self.point = (self.point[0], self.point[1]-1)
        elif self.direction == "L":
            self.point = (self.point[0]-1, self.point[1])
        elif self.direction == "U":
            self.point = (self.point[0], self.point[1]+1)
        elif self.direction == "R":
            self.point = (self.point[0]+1, self.point[1])
        else:
            raise ValueError("Incorrect Command")
    
    def command(self, userInput):
        if userInput == "T":
            self.direction = self.turnCommand[self.direction]
        
        if userInput == "M":
            self._move()

        strPoint = "".join(map(str, self.point))
        
        print("Direction:" + self.direction + "\nPosition: " + strPoint)

            

print("The current position of the Robot (0,0) pointing Down")
robotRover = Robot()
# Turn and move - T / M

isExit = False
while not isExit:
    userInput = input("pres E to exit, Enter command T to turn robot or M to move robot a single pace: ")
    # Print the position on x, y plane and the direction the robot is facing
    if userInput == "E":
        isExit = True
        continue
    robotRover.command(userInput)