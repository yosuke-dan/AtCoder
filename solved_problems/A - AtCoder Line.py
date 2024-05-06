n, x, y ,z = map(int,input().split())

if x > z > y:
    print('Yes')
    exit()
if y > z > x:
    print('Yes')
    exit()
print('No')