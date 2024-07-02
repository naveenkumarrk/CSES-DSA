# CSES - Repetitions in DNA 
DNA = input()

max_freq = 1
curr_freq = 1

i, j = 0, 1

while j < len(DNA):
    if DNA[i] == DNA[j]:
        curr_freq += 1
    else:
        if curr_freq > max_freq:
            max_freq = curr_freq
        curr_freq = 1
        i = j
    j += 1

if curr_freq > max_freq:
    max_freq = curr_freq
    
print(max_freq)