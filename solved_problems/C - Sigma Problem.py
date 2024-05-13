# import itertools

# N = int(input())
# A = list(map(int,input().split()))


# itertools.combinations
# C = list(map(lambda x: sum(x) % 100000000,itertools.combinations(A, 2)))

# print(sum(C))



N = int(input())
A = sorted(list(map(int,input().split())))
# A = sorted(list(map(int,input().split())), reverse=True)
M = 10 ** 8
# M = 10 # test
total = (N-1)*sum(A)
# print(total)

count = 0
# # 全探索
# for i in range(N-1):
#     for j in range(i+1,N):
#         goukei = A[i] + A[j]
#         if goukei >= 100000000:
#             count += N - j
#             break

# しゃくとり法
less = 0

right = N - 1
for left in range(N-1):
    while left < right and A[left] + A[right] >= M:
        right -= 1
    if left == right:
        break
    less += right - left

same_or_more = N*(N-1)//2 - less

total -= same_or_more * M

print(total)