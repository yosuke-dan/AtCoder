N = int(input())
A = list(map(int, input().split()))

count = 0

def check(A):
    for a in A:
        if a % 2 != 0:
            return False
    return True

while check(A):
    A = list(map(lambda x: x // 2, A))
    count += 1

print(count)
