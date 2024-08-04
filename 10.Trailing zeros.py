# def factorial(n, memo = {}):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         return 1
#     else:
#         res =  n * factorial(n-1, memo)
#         memo[n] = res
#         return res

# f = factorial(n)
# cnt = 0
# while f % 10 == 0:
#     cnt += 1
#     f = f// 10
# print(cnt)

def solve(n):
    if n == 0:
        return 0
    cnt = 0 
    while n >= 5:
        n = n//5
        cnt += n
    return cnt

n = int(input())
print(solve(n))