A, B = map(int,input().split())
for i in range(10):
    if not i == A + B:
        print(i)
        exit()