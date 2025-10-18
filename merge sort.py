def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # left half ko sort karo
    right = merge_sort(arr[mid:])  # right half ko sort karo

    return merge(left, right)      # dono halves ko merge karo


def merge(left, right):
    result = []
    i = j = 0

    # dono list ke elements compare karke chhota wala result me daalo
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # agar left ya right me elements bache hain to sabko add kar do
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Example
myArray = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", myArray)
sortedArray = merge_sort(myArray)
print("Sorted array:", sortedArray)
# This is merge sort.py
