def sort_array(array):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for i in range(0,len(array)):
        if array[i] == 0:
            count_0 += 1
        elif array[i] == 1:
            count_1 += 1
        else:
            count_2 += 1
    
    i = 0
    while (count_0 > 0):
        array[i] = 0
        i = i + 1
        count_0 -= 1

    while (count_1 > 0):
        array[i] = 1
        i = i + 1
        count_1 -= 1
    
    while (count_2 > 0):
        array[i] = 2
        i = i + 1
        count_2 -= 1
    
    return array

array = [0,1,2,0,2,0,1]
print(sort_array(array))