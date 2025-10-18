def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # target nahi mila

# Example
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
myTarget = 15

result = binary_search(myArray, myTarget)

if result != -1:
    print(f"Value {myTarget} found at index {result}")
else:
    print(f"Value {myTarget} not found")
# This is binary_search.py
