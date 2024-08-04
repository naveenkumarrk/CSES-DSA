text = input()
def palindromeReorder(text):
    freq = {}
    cnt = 0
    ch = ''
    for ele in text:
        freq[ele] = freq.get(ele, 0) + 1

    for key , val in freq.items():
        if val % 2:
            ch = key
            cnt +=1 
    if (len(text) % 2 == 0 and cnt > 0) or cnt >1:
        return 'NO SOLUTION'
        

    else:
        res = ''
        for key , val in freq.items():
            for i in range(val//2):
                res += key
        if len(text) % 2:
            res += ch + res[::-1]
            return res
        res += res [::-1]
        return res

print(palindromeReorder(text))