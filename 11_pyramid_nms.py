def pattern(n):
    k = 2 * n - 2
    x = 0
    for i in range(0, n):
        x += 1
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0,i*2+1):
            print(x, end=" ")
        print("\r")
    k = n - 2
pattern(4)
