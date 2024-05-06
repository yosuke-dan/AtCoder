# N = [int(input())]

# ans = 0

# def division(N,num):
#     half = num // 2
#     is_one = half == 1
#     is_even = num % 2 == 0
#     if is_even and is_one:
#         return
#     elif is_even and not is_one:
#         N.append(half)
#         N.append(half)
#         return
#     elif not is_even and not is_one:
#         N.append(half)
#         N.append(half+1)
#         return
#     elif not is_even and is_one:
#         N.append(half+1)
#         return
#     return
    

# while len(N)>0:
#     popped = N.pop(0)
#     division(N,popped)
#     ans += popped
#     # print(N)

# print(ans)



from functools import cache

@cache
def f(N):
    return 0 if N == 1 else f(N // 2) + f((N + 1) // 2) + N

print(f(int(input())))
