my_array=[7,8,4,1,9,0,2]
n=len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j],my_array[j+1]= my_array[j+1],my_array[j]
            print("sorted array:",my_array)