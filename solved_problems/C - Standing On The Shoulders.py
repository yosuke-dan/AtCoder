N = int(input())
A, B, C = [None]*N,[None]*N,[None]*N

for i in range(N):
    A[i],B[i] = map(int,input().split())
    C[i] = B[i] - A[i]

max_value = max(C)

# 最大値のインデックスを見つける
max_index = C.index(max_value)

print(sum(A)+B[max_index]-A[max_index])
