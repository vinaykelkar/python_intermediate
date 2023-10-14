array = [5,0,7,4,8,1,3,0,7,2,0]
n = 11

def push_zeroes(array, n):
    for i in range(0, n-1):
        for j in range(0, n-1-i): 
            if array[j] < array[j+1] and array[j] == 0:
                array[j], array[j+1] = array[j+1], array[j]
    
    return array

print(push_zeroes(array,n))

#used bubble sort and brute force approach