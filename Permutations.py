n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print('NO SOLUTION')
else:
        odd = [i for i in range(1, n + 1, 2)]
        even = [i for i in range(2, n +1, 2 )]
        arrangement  = even + odd
        print(" ".join(map(str,arrangement)))
