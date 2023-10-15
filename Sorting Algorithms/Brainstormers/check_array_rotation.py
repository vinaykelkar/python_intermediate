def array_rotation(array):
    if len(array) == 1 or len(array) == 0:
        return 0
    else:
        min = array[0]
        count = 0
        for i in range(1,len(array)):
            if array[i] < min:
                count = count + 1
        
        if count == 0:
            return 0
        
        else:
            return len(array)- count



array=[1,2]
print(array_rotation(array))