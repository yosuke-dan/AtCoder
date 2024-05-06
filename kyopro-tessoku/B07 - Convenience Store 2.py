T = int(input())
N = int(input())
L, R = [0]*N, [0]*N
for i in range(N):
    L[i], R[i] = map(int,input().split())

B = [0]*(T+1)
for i in range(N):
    B[L[i]] += 1
    B[R[i]] -= 1

# print(B)

A = [0]*(T+1)
for i in range(1,T+1):
    A[i] = A[i-1] + B[i-1]

# print(A)

for i in range(T):
    print(A[i+1])