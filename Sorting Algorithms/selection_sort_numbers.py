def selection_sort(array):
    for i in range(0,len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] <  array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    
    return array
        


print("Print number of elements you want in array")
n = int(input())
print("Please enter comma seprated elements")
array = list(map(int, input().strip().split(',')))[:n]
print(array)
print(selection_sort(array))