N = int(input())

Ag = []
Bg = []



for i in range(N):
    Ag.append(list(input()))
for i in range(N):
    Bg.append(list(input()))

# print(Ag,Bg)

for i in range(N):
    for j in range(N):
        if Ag[i][j] != Bg[i][j]:
            print(i+1,end=' ')
            print(j+1)
            exit()