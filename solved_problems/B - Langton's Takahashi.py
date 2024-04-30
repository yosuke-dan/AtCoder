H, W, N = map(int,input().split())

grid = [['.' for _ in range(W)]for _ in range(H)]

# 現在地
p = [0,0]
# 向き
d = 0

# 上右下左
q = [[-1,0],[0,1],[1,0],[0,-1]]

for i in range(N):
    if grid[p[0]][p[1]] == '.':
        grid[p[0]][p[1]] = '#'
        d = (d + 1) % 4
    else:
        grid[p[0]][p[1]] = '.'
        d = (d - 1) % 4
    p = [x + y for x, y in zip(p,q[d])]
    p[0] = p[0] % H
    p[1] = p[1] % W

for h in range(H):
     print(''.join(grid[h]))