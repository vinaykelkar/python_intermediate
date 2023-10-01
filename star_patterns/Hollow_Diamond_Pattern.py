'''
_	_	_	*			
_	_	*	_	*		
_	*	_	_   _	*	
*	_	_	_	_	_	*
_	*	_	_		*	
_	_	*		*		
_	_	_	*			
_ is nothing but spaces for display purpose
'''
print("Please enter any number to print pattern")
n = int(input())
if n % 2 == 0 :
    print("Please enter odd number")

for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        if j == 0 or j == 2 * i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

# downward pyramid
for i in range(n - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(n - i - 1) - 1):
        if j == 0 or j == 2*(n - i - 1) - 2:
            print('*', end='')
        else:
            print(' ', end='')
    print()

