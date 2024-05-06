N = int(input())
A = list(map(int,input().split()))
D = int(input())
L, R = [None] * D,[None] * D
for i in range(D):
    L[i],R[i] = map(int,input().split())


# 左から累積
Lmax = [None] * N
Lmax[0] = A[0]
for i in range(1,N):
    Lmax[i] = max(Lmax[i-1],A[i])

# 右から累積
Rmax = [None] * N
Rmax[N-1] = A[N-1]
for i in range(N-2,-1,-1):
    Rmax[i] = max(Rmax[i+1],A[i])


for i in range(D):
    ans = max(Lmax[L[i]-2],Rmax[R[i]])
    print(ans)
