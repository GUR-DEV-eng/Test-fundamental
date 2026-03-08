n = input().strip()      # read as string

freq = [0] * 10          # freq[0]..freq[9]

for ch in n:
    if ch.isdigit():
        d = int(ch)
        freq[d] += 1

# print counts of 0 to 9
print(*freq)
