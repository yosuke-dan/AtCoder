N, L, R = map(int,input().split())
A = list(map(int,input().split()))

ans_list = []

for a in A:
    if a <= L:
        ans = L
    elif L < a < R:
        ans = a
    else:
        ans = R
    ans_list.append(str(ans))

print(' '.join(ans_list))