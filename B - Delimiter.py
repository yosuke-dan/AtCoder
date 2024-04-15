A = []

try:
    while True:
        s = input()
        if s:
            A.append(int(s))
        else:
            break
except:
    pass

for i in range(len(A) - 1, -1, -1):
    print(A[i])