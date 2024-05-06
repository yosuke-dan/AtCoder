N = int(input())
A = list(map(int,input().split()))
Q = int(input())
L, R = [None]*Q, [None]*Q
for i in range(Q):
    L[i],R[i] = map(int,input().split())

rec = [0]
for i in range(N):
    rec.append(rec[i]+A[i])

for i in range(Q):
    turns = R[i] - L[i] + 1
    wins = rec[R[i]] - rec[L[i]-1]
    # print(f'turns:{turns},wins:{wins}')
    if wins * 2 > turns:
        ans = 'win' 
    elif wins * 2 == turns:
        ans = 'draw'
    else:
        ans = 'lose'
    print(ans)