array1= [1,3,4,7,11]
array2= [4,9,11,13]

array3= []


def merged_sorted_array(array1,array2):
    i , j = 0,0
    len1, len2 = len(array1), len(array2)
    while (i<len(array1) and j<len(array2)):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i = i + 1
        elif array1[i] >= array2[j]:
            array3.append(array2[j])
            j = j + 1
    
    while i < len1:
        array3.append(array1[i])
        i = i + 1
        
    while j < len2:
        array3.append(array2[j])
        j = j + 1
    


    return array3

print(merged_sorted_array(array1,array2))