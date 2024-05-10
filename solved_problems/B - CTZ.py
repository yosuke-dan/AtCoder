n = int(input())

nt = bin(n)
count = 0
for i in range(-1,-(len(nt)-2),-1):
    if nt[i] == '0':
        count += 1
    else:
        break
print(count)

# bit演算むずい