N = int(input())
A = list(map(int,input().split()))

rec = [None for i in range(N)] 
rec[0] = A[0]

for i in range(N-1):
    rec[i+1] = rec[i] + A[i+1]

# print(abs(min(rec))+rec[-1])

extra = min(rec)

if extra < 0:
    ans = -1 * (extra) + rec[-1]
else:
    ans = rec[-1]

print(ans)