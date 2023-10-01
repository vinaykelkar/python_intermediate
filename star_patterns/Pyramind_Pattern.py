'''
_	_	*		
_	*	*	*	
*	*	*	*	*
_	*	*	*	
_	_	*		
_ is nothing but spaces for display purpose
'''
print("Please enter any number to print pattern")
n = int(input())

for i in range(1,n+1):
    for spaces in range(1, n - i + 1):
        print(" ",end="")
    for stars in range(1,2*i - 1 +1):
        print("*",end="")
    print()