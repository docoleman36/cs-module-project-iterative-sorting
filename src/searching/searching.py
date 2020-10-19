# Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
# If x matches with an element, return the index.
# If x doesn’t match with any of elements, return -1.


def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
# Compare the item in the middle of the data set to the item we are searching for.
# If it is the same, stop. We found it and are done!
# Else, if the item we are searching for is LESS than the item in the middle:
# Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
# Else, the item we are searching for is GREATER than the item in the middle:
# Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high)
        guess = arr[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1  # not found
