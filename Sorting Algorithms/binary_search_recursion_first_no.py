def binary_search(array, target,debug):
    recursive_binary_search(target,array,0,len(array) - 1,debug)

def recursive_binary_search(target,array,lower_index,upper_index,debug):
    if lower_index < upper_index:
        middle = (lower_index + upper_index) // 2
        if target == array[middle]:
            if target == array[middle - 1]:
                lower_index = middle - 1
                upper_index = middle
                middle = (lower_index + upper_index) // 2
                recursive_binary_search(target,array,lower_index,upper_index,debug)
            print("Element is found at index : ", middle)
        elif target < array[middle]:
            upper_index = middle - 1
            recursive_binary_search(target,array,lower_index,upper_index,middle)
        else:
            lower_index = middle + 1
            recursive_binary_search(target,array,lower_index,upper_index,middle)
    else:
        return -1

#print("Element is found at index : ", middle)

print("Print number of elements you want in array ")
n = int(input())
print(n)
print("List of elements which are space and comma separated")
array = list(map(int, input().strip().split(',')))[:n]
print(array)
print("Enter target element you want to search for: ")
target = int(input())
binary_search(array,target,debug=True)
