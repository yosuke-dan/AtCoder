N = int(input())

T, A = 0, 0

for i in range(N):
    X, Y = map(int,input().split())
    T += X
    A += Y

if T > A:
    print('Takahashi')
elif T == A:
    print('Draw')
else:
    print('Aoki')