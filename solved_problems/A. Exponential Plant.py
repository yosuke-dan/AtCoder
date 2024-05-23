H = int(input())
# M = list(map(int,input().split()))

height = 0
cnt = 0

while height <= H:
    height += 2 ** cnt    
    cnt += 1

print(cnt)