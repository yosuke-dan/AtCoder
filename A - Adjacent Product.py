N = int(input())

values = list(map(int,input().split()))

results = []

for i in range(N-1):
    results.append(values[i] * values[i+1])

print(*results)