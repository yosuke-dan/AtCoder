import copy

N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

def HowManyDishes(stock,recipe,number):
    dish = 10**18
    for i in range(number):
        if recipe[i] == 0:
            continue
        dish = min(dish, stock[i] // recipe[i])
    return dish

# for i in range(N):
#     if A[i] == 0:
#         continue
#     a_cnt = min(a_cnt, Q[i] // A[i])

a_max = HowManyDishes(Q,A,N)

for a in range(a_max+1):
    Q_temp = copy.deepcopy(Q)
    for i in range(N):
        Q_temp[i] -= A[i] * a 
    # for i in range(N):
    #     if B[i] == 0:
    #         continue
    #     b_cnt = min(b_cnt, Q_temp[i] // B[i])
    b_max = HowManyDishes(Q_temp,B,N)
    ans = max(ans,a+b_max)

print(ans)





import copy

N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

# 1回目のmin()を乗りこなすために適当にでかい数字を入れておく
a_cnt = 100000000
for i in range(N):
    if A[i] == 0:
        continue
    a_cnt = min(a_cnt, Q[i] // A[i])



for a in range(a_cnt+1):
    Q_temp = copy.deepcopy(Q)
    for i in range(N):
        Q_temp[i] -= A[i] * a
    b_cnt = 100000000
    for i in range(N):
        if B[i] == 0:
            continue
        b_cnt = min(b_cnt, Q_temp[i] // B[i])
        ans = max(ans,a+b_cnt)

print(ans)