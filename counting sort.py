# This is counting sort.py
def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    # counting
    for num in arr:
        count[num] += 1

    # sorted result
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])  # i ko count[i] bar add kar diya

    return result


unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)
