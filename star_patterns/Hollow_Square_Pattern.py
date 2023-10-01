'''
*	*	* 	* 	*
				
*				*
				
*				*
				
*				*
				
*	*	* 	* 	*

'''
print("Please enter any number to print pattern")
n = int(input())

for i in range(1,2*n):
    for j in range(1,n+1):
        if i == 1 or i == (2*n - 1):
            print("*",end="")
        elif i % 2 == 0:
            print(" ",end="")
        elif i % 2 == 1 and (j == 1 or j == n):
            print("*",end="")
        else:
            print(" ",end="")
    print()