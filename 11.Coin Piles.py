t = int(input())
def coinPiles(t):
    a, b = map(int, input().strip().split())
    x = 2 * a - b
    y = 2 * b  - a

    if x < 0 or y <0 :
        return False
    return not (x % 3) and not (y % 3)
 
for i in range(t):
    print('YES' if  coinPiles(t) else 'NO')
    
         

