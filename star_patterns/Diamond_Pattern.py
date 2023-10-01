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
if n % 2 == 0 :
    print("Please enter odd number")
n1 = (n // 2) + 1
n2 = n - n1

for i in range(1,n1+1):
    for spaces in range(1, n1 - i + 1):
        print(" ",end="")
    for stars in range(1,2*i - 1 +1):
        print("*",end="")
    print()

for i in range(n2,0,-1):
    for spaces in range(0, n2 - i + 1):
        print(" ",end="")
    for stars in range(0, 2*i - 1):
        print("*",end="")
    print()