def two_knights(k):
    all_ways = (k * k) * ((k * k) - 1) //2

    attack_ways = 2 * 2 * (k - 1) * (k - 2)

    ans =  all_ways - attack_ways

    return ans

n = int(input())

for i in range(1,n+1):
    res = two_knights(i)
    print(res)
