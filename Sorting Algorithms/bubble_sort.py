def bubble_sort(array):
    count = 0
    for k in range(0,len(array)-1):
            for i in range(0,len(array)-1-k):
                if i != len(array) - 1:
                    if array[i] > array[i+1]:
                        array[i], array[i+1] = array[i+1], array[i]
                        count = count + 1
            if count == 0:
                 print(count)
                 return array
    return array


print("Print number of elements you want in array")
n = int(input())
print("Please enter comma seprated elements")
array = list(map(int, input().strip().split(',')))[:n]
print(array)
print(bubble_sort(array))