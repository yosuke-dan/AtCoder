N, K = map(int,input().split())
A = sorted(list(set((map(int,input().split())))))

sum_K = K*(K+1)//2

if A[-1] <= K:
    ans = sum_K - sum(A)
else:
    A = list(map(lambda x: 0 if x > K else x,A))
    # print(f'K:{K},K-1:{K-1},sum(A):{sum(A)}')
    ans = sum_K - sum(A)

print(ans)