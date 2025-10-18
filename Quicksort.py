def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # pehla element pivot le liya
        left = [x for x in arr[1:] if x <= pivot]   # pivot se chhote
        right = [x for x in arr[1:] if x > pivot]   # pivot se bade
        return quicksort(left) + [pivot] + quicksort(right)


my_array = [64, 34, 25, 12, 22, 11, 90, 5]
sorted_array = quicksort(my_array)
print("Sorted array:", sorted_array)
