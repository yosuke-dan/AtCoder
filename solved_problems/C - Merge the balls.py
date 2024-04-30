N = int(input())

balls = list(map(int,input().split()))

li = []
for ball in balls:
    li.append(ball)
    while len(li) > 1 and li[-1] == li[-2]:
        add_ball = li[-1]
        del li[-2:]
        li.append(add_ball+1)
    # print(li)

print(len(li))