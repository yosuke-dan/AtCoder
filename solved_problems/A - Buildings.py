n = int(input())
l = list(map(int,input().split()))

lone = l[0]
for i in range(1,n):
    if lone < l[i]:
        print(i+1)
        exit()

print(-1)