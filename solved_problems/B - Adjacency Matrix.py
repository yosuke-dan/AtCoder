N = int(input())

matrix = []
result = []

for i in range(N):
    matrix.append(list(map(int,input().split())))

for i in range(N):
    result.append([])
    for j in range(N):
        if matrix[i][j] == 1:
            result[i].append(j+1)
    print(*result[i])

# 多次元配列を扱う
# 要素をスペース区切りで出力したい時は*