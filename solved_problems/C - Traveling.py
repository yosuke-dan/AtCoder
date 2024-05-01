N = int(input())

current = [0,0,0]

for _ in range(N):
    target = list(map(int,input().split()))
    time = target[0] - current[0]
    distance = abs(target[1] - current[1]) + abs(target[2] - current[2])
    if time < distance:
        print('No')
        exit()
    if time % 2 != distance % 2:
        print('No')
        exit()
    current = target

print('Yes')