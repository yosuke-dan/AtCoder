a, b = map(int,input().split())

ans = 'No'
for i in range(a,b+1,1):
    if 100 % i == 0:
       ans = 'Yes'
print(ans)