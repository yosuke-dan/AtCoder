
N = int(input())


def is326likeNumber(n):
    strn = str(n)
    v100 = int(strn[0])
    v10 = int(strn[1])
    v1 = int(strn[2])
    if v100 * v10 == v1:
        return True
    else:
        return False
    
for i in range(N,999):
    if is326likeNumber(i):
        print(i)
        break