N = int(input())
A, B, C, D = [None] * N, [None] * N, [None] * N, [None] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int,input().split())

width = 1501
height = 1501

grid = [[0] * width for _ in range(height)]

for i in range(N):
    grid[B[i]][A[i]] += 1
    grid[D[i]][C[i]] += 1
    grid[B[i]][C[i]] -= 1
    grid[D[i]][A[i]] -= 1

# horizontal gridulative
for h in range(height):
    for w in range(width-1):
        grid[h][w+1] = grid[h][w] + grid[h][w+1]

# vertical gridulatve
for w in range(width):
    for h in range(height-1):
        grid[h+1][w] = grid[h][w] + grid[h+1][w]

count = 0
for h in range(height):
    for w in range(width):
        if grid[h][w] >= 1:
            count += 1

print(count)