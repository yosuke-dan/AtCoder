B = int(input())

limit = 10 ** 18
res = 0
cnt = 1
res_li = []

while res <= limit:
    res = cnt ** cnt
    if res == B:
        print(cnt)
        exit()
    cnt += 1


print(-1)