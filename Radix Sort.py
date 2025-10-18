def radixSort(arr):
    maxVal = max(arr)
    exp = 1

    while maxVal // exp > 0:
        # 10 buckets banaye (0-9 digits ke liye)
        radixArray = [[] for _ in range(10)]

        # elements ko unke digit ke hisaab se bucket me daalo
        for val in arr:
            radixIndex = (val // exp) % 10
            radixArray[radixIndex].append(val)

        # buckets se wapas array banao (stable order me)
        arr = [val for bucket in radixArray for val in bucket]

        exp *= 10

    return arr


# Example
myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
sortedArray = radixSort(myArray)
print("Sorted array:", sortedArray)
# This is Radix Sort.py
