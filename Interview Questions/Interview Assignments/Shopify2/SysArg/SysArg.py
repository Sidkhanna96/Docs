from typing import List
import sys
import random
import ast

def randInt():
    return random.randrange(1,5)

def main():
    try:
        if len(sys.argv) <= 1:
            raise ValueError("Not enough arguments provided")
        
        _, command = sys.argv

        command = ast.literal_eval(command)

        if not isinstance(command, list):
            raise ValueError("Incorrect command type provided")
        
    except ValueError as e:
        print(f"Error 1: {e}")
        raise  # Let it propagate
    except Exception as e:
        print(f"Error 2: {e}")
        raise  # Let it propagate

    val = randInt()
    print(val)


if __name__ == "__main__":
    main()