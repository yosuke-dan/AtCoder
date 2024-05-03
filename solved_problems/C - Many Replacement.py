# N = int(input())
# S = input()
# Q = int(input())
# c, d = [ None ] * Q, [ None ] * Q
# for i in range(Q):
#     c[i], d[i] = input().split()

# for i in range(Q):
#     if c[i] in S:
#         S = S.replace(c[i],d[i])

# print(S)

# 答えみた

# n = int(input())
# s = input()
# q = int(input())

# mae = "abcdefghijklmnopqrstuvwxyz"
# ato = "abcdefghijklmnopqrstuvwxyz"

# for i in range(q):
#   a, b = input().split()
#   ato = ato.replace(a, b)
  
# print(str.maketrans(mae,ato))

# s = s.translate(str.maketrans(mae, ato))

# print(s)

N = int(input())
S = input()
Q = int(input())

before = 'abcdefghijklmnopqrstuvwxyz'
after = 'abcdefghijklmnopqrstuvwxyz'

for i in range(Q):
    A, B = input().split()
    after = after.replace(A,B)

S = S.translate(str.maketrans(before,after))

print(S)