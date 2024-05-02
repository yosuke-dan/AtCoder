N = int(input())
A = list(map(int,input().split()))
ans = 'No'
for a in range(N-2):
    for b in range(a+1,N-1):
        for c in range(b+1,N):
            # print(a,b,c)
            if 1000 == A[a] + A[b] + A[c]:
                ans = 'Yes'

print(ans)