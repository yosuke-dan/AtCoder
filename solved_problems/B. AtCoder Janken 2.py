N = int(input())

S = [None for _ in range(N)]
C = [None for _ in range(N)]

for i in range(N):
    S[i], C[i] = input().split()

S = sorted(S)

total_rate = 0
for i in range(N):
    total_rate += int(C[i])

mod = total_rate % N

print(S[mod])