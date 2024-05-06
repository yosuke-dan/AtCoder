S = input()
T = input()

start_point = 1

ans = []

for s in S:
    found_index = T.find(s)   
    ans.append(T.find(s) + start_point)
    T = T[found_index+1:]
    start_point += found_index + 1

print(*ans)