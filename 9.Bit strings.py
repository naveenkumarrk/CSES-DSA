n = int(input())

def bitString(base,n ):
    return (base ** n) % (10 ** 9 + 7)

res = bitString(2, n)
print(res)