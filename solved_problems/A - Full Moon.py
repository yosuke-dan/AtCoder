n,m,p = map(int,input().split())

if m > n:
    print(0)
    exit()
ans = ((n - m)//p) + 1
print(ans)