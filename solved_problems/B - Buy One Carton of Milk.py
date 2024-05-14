N, S, M, L = map(int,input().split())

# s6 m8 l12  n max100

# 16 120 150 200
# 10

# 8個入りを2個買うのが良い

total = 100000000

for s in range(20):
    for m in range(20):
        for l in range(20):
            if 6 * s + 8 * m + 12 * l >= N:
                total = min(s * S + m * M + l * L, total)
                break

print(total)