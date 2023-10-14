def binary_search(array, target, debug=False):
    #debug=False will help us print the output of everytime we execute this function
    #      [12, 34, 46, 56, 67, 89]
    #indexes 0,  1,  2,  3,  4,  5   
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        middle = (lower_bound + upper_bound ) // 2
        if debug:
            print("Lower bound : ",lower_bound)
            print("Uppoer bound : ", upper_bound)
            print("Middle : ", middle)
        if target == array[middle]:
            return "Value at middle index ", middle
        elif target < array[middle]:
            upper_bound = middle - 1
        else:
            lower_bound = middle + 1
    
    return "Element not available", -1

array = [12,34,46,56,56,56,67,89]
target = 56

binary_search(array, target, debug=True)


