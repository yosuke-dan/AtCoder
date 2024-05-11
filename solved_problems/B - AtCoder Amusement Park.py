from collections import deque

N, K = map(int,input().split())
groups = deque(list(map(int,input().split())))
onboard = 0

count = 0

while groups:
    if onboard + groups[0] <= K:
        onboard += groups.popleft()
    else:
        onboard = 0
        count += 1

print(count+1)