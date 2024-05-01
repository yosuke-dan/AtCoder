N, Y = map(int,input().split())

combination = []

for a in range(N+1):
    for b in range(N-a+1):
        c = N - a - b
        if c < 0:
            continue
        if 10000 * a + 5000 * b + 1000 * c == Y:
            print(a,b,c)
            exit()

print(-1,-1,-1)


# N,Y = map(int,list(input().split()))
# for a in range(N+1):
#     for b in range(N-a+1):
#         c = (Y - 10000*a -5000*b)//1000
#         if(c>=0 and a+b+c==N):
#             print(a,b,c)
#             exit()

# print(-1,-1,-1)