input()
members = list(map(int,input().split()))
total = 0
for member in members:
    total += member
print(-1 * total)