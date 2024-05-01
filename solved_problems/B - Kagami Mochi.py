# N = int(input())

# mochi = []
# for _ in range(N):
#     mochi.append(int(input()))

# mochi = set(mochi)

# print(len(mochi))

N = int(input())
d = [input() for i in range(N)]
print(len(set(d)))