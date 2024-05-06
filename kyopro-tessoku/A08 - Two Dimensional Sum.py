H, W = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(H)]

Q = int(input())
A, B, C, D = [None] * Q,[None] * Q,[None] * Q,[None] * Q

for i in range(Q):
    A[i], B[i], C[i], D[i] = map(int,input().split())

# sum horizontal 横方向に累積（横＋１）
grid_h = [[0] * (W + 1) for _ in range(H)] 
for h in range(H):
    for w in range(W):
        grid_h[h][w + 1] = grid_h[h][w] + grid[h][w]

# sum vertical 縦方向に累積（縦＋１）
grid_v = [[0] * (W + 1) for _ in range(H + 1)]
for w in range(W):
    for h in range(H):
        grid_v[h+1][w+1] = grid_v[h][w+1] + grid_h[h][w+1]

# 答えを求める
for i in range(Q):
    answer = grid_v[C[i]][D[i]] - grid_v[C[i]][B[i]-1] - grid_v[A[i]-1][D[i]] + grid_v[A[i]-1][B[i]-1]
    print(answer)

# 出力テスト
# for h in range(H):
#     print(grid[h])
# for h in range(H):
#     print(grid_h[h])
# for h in range(H+1):
#     print(grid_v[h])