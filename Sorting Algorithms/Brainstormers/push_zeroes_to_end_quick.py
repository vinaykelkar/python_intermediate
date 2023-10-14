def push_zeroes(array):
    position = 0

    for i in range(0,len(array)):
        if array[i] != 0 :
            array[i],array[position] = array[position],array[i]
            position = position + 1

    
    print(array)
    

array = [0,1,7,4]
push_zeroes(array)
