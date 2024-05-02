N = int(input())
ans = ''
for i in range(9,-1,-1):
    # print(N)
    d = N // (2 ** i)
    if d > 0:
        N -= 2 ** i
        ans += '1'
    else:
        ans += '0'

print(ans)