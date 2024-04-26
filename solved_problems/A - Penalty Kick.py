N = int(input())

PK_result = ""

for i in range(N):
    if (i + 1) % 3 == 0:
        PK_result += 'x'
    else:
        PK_result += 'o'

print(PK_result)