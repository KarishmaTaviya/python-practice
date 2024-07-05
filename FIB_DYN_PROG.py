def fastfib(n,memo={}):
    if n<=1:
        return n
    try:
        return memo[n]
    except KeyError:
        result= fastfib(n-1,memo)+fastfib(n-2,memo)
        memo[n]=result
        return result

for i in range(120):
    print(fastfib(i), end=' ')
    if i % 10 == 0:
        print()
'''
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(120):
    print(fibonacci(i), end=' ')
    if i % 10 == 0:
        print()

'''
