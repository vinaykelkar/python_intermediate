def second_largest_array(array):

    max = float('-inf')
    second_max = float('-inf')

    for i in range(0,len(array)):
        if array[i] > max:
            second_max = max
            max = array[i]
        elif array[i] > second_max:
            second_max = array[i]
    
    return second_max

array = [4,3,10,9,2]

print(second_largest_array(array))
