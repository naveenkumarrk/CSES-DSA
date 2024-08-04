n = int(input())
ranged_sum = n * (n+1) // 2

if ranged_sum % 2 != 0:
    print("NO")
else:
    s1 = []
    s2 = []
    target = ranged_sum // 2

    curr_sum = 0
    for i in range(n, 0, -1):
        if curr_sum + i <= target:
            s1.append(i)
            curr_sum += i
        else:
            s2.append(i)


    print("YES")
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)