N, K = map(int,input().split())
ans = 0
# for red in range(1,K+1,1):
#     if red > N:
#         continue
#     for blue in range(1,K+1,1):
#         if blue > N:
#             continue
#         white = K - red - blue
#         if 1 <= white <= N:
#             ans += 1

for red in range(1,N+1):
    for blue in range(1,N+1):
        white = K - red - blue
        if 1 <= white <= N:
            ans += 1

print(ans)