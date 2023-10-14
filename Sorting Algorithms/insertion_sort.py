def insertion_sort(array):
    for i in range(1,len(array)):
        j = i 
        for j in range(j,0,-1):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array

print("Print number of elements you want in array")
n = int(input())
print("Please enter comma seprated elements")
array = list(map(int, input().strip().split(',')))[:n]
print(array)
print(insertion_sort(array))
#8,5,3,1