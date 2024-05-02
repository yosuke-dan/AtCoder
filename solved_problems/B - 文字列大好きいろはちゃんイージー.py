N, L = map(int,input().split())
S = [input() for i in range(N)]

S = sorted(S)

ans = "".join(S)

print(ans)