def rotate_array_by_n(array,rotate):
    temp_array = []
    if rotate == 0 or rotate == len(array):
        return array
    else:
        for i in range(rotate,len(array)):
            temp_array.append(array[i])
        
        for j in range(0,rotate):
            temp_array.append(array[j])
    
    return temp_array





array = [1,3,6,11,12,17]
rotate = 4
print(rotate_array_by_n(array,rotate))