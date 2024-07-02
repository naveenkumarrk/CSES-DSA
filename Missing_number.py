# CSES - Missing number 
n = int(input())
arr = list(map(int, input().split()))
n_sum = n * (n+1) // 2
missing = n_sum - sum(arr) 
print(missing)