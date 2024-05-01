import re
S = input()

while True:
    if len(S) == 0:
        print('YES')
        break
    elif len(S) >= 7 and S[-7:] == 'dreamer':
        S = S[0:-7]
    elif len(S) >= 6 and S[-6:] == 'eraser':
        S = S[0:-6]
    elif len(S) >= 5 and S[-5:] == 'dream':
        S = S[0:-5]
    elif len(S) >= 5 and S[-5:] == 'erase':
        S = S[0:-5]
    else:
        print('NO')
        break

# import re
# S = input()
# print("YES" if re.match("^(dream|dreamer|erase|eraser)+$", S) else "NO")
