H, W, N = map(int,input().split())
A, B, C, D = [None] * N,[None] * N,[None] * N,[None] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int,input().split())
    A[i], B[i], C[i], D[i] = A[i]-1, B[i]-1, C[i]-1, D[i]-1

grid = [[0] * (W+1) for _ in range(H+1)]

for i in range(N):
    grid[A[i]][B[i]] += 1
    grid[C[i]+1][D[i]+1] += 1
    grid[A[i]][D[i]+1] -= 1
    grid[C[i]+1][B[i]] -= 1
    # # test print
    # for j in range(H):
    #     print(grid[j])
    # print('------------------')

# cumulative sum
cum = [[0] * (W+2) for _ in range(H+2)]

# w direction
for h in range(H):
    for w in range(W):
        cum[h+1][w+1] = cum[h+1][w] + grid[h][w]
# # test print
# for i in range(H+1):
#     print(cum[i])
# print('------------------')

# h direction
for w in range(W):
    for h in range(H):
        cum[h+1][w+1] += cum[h][w+1]
# # test print
# for  i in range(H+1):
#     print(cum[i])
# print('------------------')

# answer
for h in range(1,H+1):
    print(*cum[h][1:W+1])