# Given height of sticks in an array and the initial position of bird which has fixed stick 
# height of 0, she picks up sticks from both side alternatively. In other words, it will first start 
# right to find the stick and bring it to the initial position, then start left to do the same. Return all 
# the indices from where the bird picks up the sticks until the total height of all sticks reaches 100.

def hundredSticks(arr):
    reverse = True
    left, right = 0, len(arr)-1
    total = 0
    ans = []

    while left <= right and total < 100:

        if reverse:
            total += arr[right]
            ans.append(right)
            right -= 1
        else:
            total += arr[left]
            ans.append(left)
            left += 1

        reverse = not reverse

    return ans

sticks = [0,10,15,20,35,30,25,50,5,1]
print(hundredSticks(sticks))


# Candy Crush


# An array of slots is given which are all initially uncolored. n queries [x,y] will be given where x = position, y = color. Each query means to paint slot at x position with color y. For each query find out how many consecutive slot pairs share the same color.
# Eg: [0,0,0,0,0,0]
# Queries: [[1,2],[2,2],[0,3],[3,2],[1,1]]
# Ans: [0, 1, 1, 2, 0]
def consecutiveSlotOptimized(arr, queries):
    ans = []
    n = len(arr)
    
    total_pairs = 0  # start at 0, ignore initial pairs
    
    for i, c in queries:
        # Remove old pairs (only if non-zero colors)
        if i > 0 and arr[i] != 0 and arr[i] == arr[i-1]:
            total_pairs -= 1
        if i < n-1 and arr[i] != 0 and arr[i] == arr[i+1]:
            total_pairs -= 1
        
        # Paint the slot
        arr[i] = c
        
        # Add new pairs (only if non-zero colors)
        if i > 0 and arr[i] != 0 and arr[i] == arr[i-1]:
            total_pairs += 1
        if i < n-1 and arr[i] != 0 and arr[i] == arr[i+1]:
            total_pairs += 1
        
        ans.append(total_pairs)
    
    return ans

print(consecutiveSlotOptimized([0,0,0,0,0,0], [[1,2],[2,2],[0,3],[3,2],[1,1]]))
# Output: [0, 1, 1, 2, 0]

# Given a string (ex. “CodeSignal”) and n, replace the nth consonant to the next consonant

def switchConsonant(word, n):
    
        


print(switchConsonant("CodeSignal", 3))
print(switchConsonant("CodeSignal", 4))