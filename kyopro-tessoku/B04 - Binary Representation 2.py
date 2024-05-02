# N = int(input())
# ans = 0
# for i in [7,6,5,4,3,2,1,0]:
#     wari = 10 ** i
#     ans += (N // wari) * (2 ** i)
#     if wari <= N:
#         N -= wari

N = input()
ans = 0

for i in range(len(N)):
    if N[i] == '1':
        ans += 2 ** (len(N) - i -1)

print(ans)

