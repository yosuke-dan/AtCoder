D = int(input())
N = int(input())
L = [None]*N
R = [None]*N

inc = [0]*(D+2)

for i in range(N):
    L[i], R[i] = map(int,input().split())
    inc[L[i]] += 1
    inc[R[i]+1] -= 1
# print(inc)


ans = [0]*(D+1)
for j in range(1,D+1):
    ans[j] = ans[j-1] + inc[j]

# print(ans)

for i in range(1,len(ans)):
    print(ans[i])