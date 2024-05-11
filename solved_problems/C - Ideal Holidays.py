from collections import deque

n, holiday, work = map(int,input().split())
week = holiday + work
plans = list(map(int,input().split()))
plans = deque(sorted(set((map(lambda x: x % week,plans)))))

for _ in range(len(plans)):
    plan_width = plans[-1] - plans[0]
    if plan_width < holiday:
        print('Yes')
        exit()
    else:
        plans.append(plans.popleft() + week)
print('No')