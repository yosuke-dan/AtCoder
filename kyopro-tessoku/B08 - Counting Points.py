N = int(input())
X, Y = [None] * N, [None] * N
for i in range(N):
    X[i], Y[i] = map(int,input().split())
Q = int(input())
a, b, c, d = [None] * Q, [None] * Q, [None] * Q, [None] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int,input().split())

X_max = max(X)
Y_max = max(Y)
# X_max = 1500
# Y_max = 1500

# 座標をグリッドに可視化
grid = [[0] * X_max for i in range(Y_max)]
for i in range(N):
    grid[Y[i]-1][X[i]-1] += 1
# # test print
# for i in range(Y_max):
#     print(grid[i])

# reccurence grid (larger than grid : x+1,Y+1)
r_grid = [[0] * (X_max + 1) for i in range(Y_max + 1)]

# X軸方向に累積
for y in range(Y_max):
    for x in range(X_max):
        r_grid[y+1][x+1] = r_grid[y+1][x] + grid[y][x]
# # test print
# for i in range(Y_max+1):
#     print(r_grid[i])

# Y軸方向に累積
for x in range(X_max):
    for y in range(Y_max):
        r_grid[y+1][x+1] = r_grid[y+1][x+1] + r_grid[y][x+1]
# # test print
# for i in range(Y_max+1):
#     print(r_grid[i])

# 答えを求める
for i in range(Q):
    ans = r_grid[d[i]][c[i]] - r_grid[b[i]-1][c[i]] - r_grid[d[i]][a[i]-1] + r_grid[b[i]-1][a[i]-1]
    print(ans)