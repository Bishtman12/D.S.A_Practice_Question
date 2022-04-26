def minJumps( arr, n):
    if n<= 1: # if only 1 number then no jump needed
        return 0
    if arr[0] == 0: # Not possible to reach end of array
        return -1

    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n): #jump is already 1 so start from index 1
        if i == n - 1: # when end of array is reached
            return jump

        maxReach = max(maxReach, i + arr[i]) #updating if there is a better ladder present
        step -= 1 # taking each step
        if step == 0: # when steps reaches zero then take another ladder so jump+=1
            jump += 1
            if i >= maxReach: #  cannot reach the end if the index is higher than ladder.
                return -1
            step = maxReach - i #updating the maximum stairs
    return -1
arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
size = len(arr)
print("Minimum number of jumps to reach end is % d " % minJumps(arr, size))