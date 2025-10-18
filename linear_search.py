def linear_search(arr, target):
    for i, val in enumerate(arr):   # index aur value dono milega
        if val == target:
            return i
    return -1

arr = [3, 7, 2, 9, 5]
target = 9

result = linear_search(arr, target)

if result != -1:
    print(f"Value {target} found at index {result}")
else:
    print(f"Value {target} not found")
# This is linear_search.py
