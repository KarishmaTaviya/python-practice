#palindrome with recursion

def pal(n):
    if len(n)<1:
        return True
    else:
        if n[0]==n[-1]:
            return pal(n[1:-1])
        else:
            return False

a=input('Enter any word : ')

if (pal(a)==True):
    print('\nPalindrome')
else:
    print('\nNot Palindrome')
