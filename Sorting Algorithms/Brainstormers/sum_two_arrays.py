def sum_two_arrays(n1,n2):
    number1 = ''
    number2 = ''
    sum = 0
    temp_array=[]
    if len(n1) == 0 and len(n2) == 0:
        return 0
    for i in range(0,len(n1)):
        number1 = number1 + str(n1[i])
    
    for j in range(0,len(n2)):
        number2 = number2 + str(n2[j])
    
    sum = int(number1)+int(number2)
    str_sum = str(sum)

    
    if len(n1) > len(n2):
        for k in range(0,len(n1)):
            n1[k] = str_sum[k]
        return n1
    
    elif len(n2) > len(n1):
        for k in range(0,len(n2)):
            n2[k] = str_sum[k]
        return n2
    
    elif len(n1) == len(n2) and len(str_sum) == len(n1):
        for k in range(0,len(n1)):
            n1[k] = str_sum[k]
        return n1
    
    else:
        for k in range(0,len(str_sum)):
            temp_array.append(str_sum[k])
        return temp_array



n1 = [6,9,8]
n2 = [5,9,2]
print(sum_two_arrays(n1,n2))

