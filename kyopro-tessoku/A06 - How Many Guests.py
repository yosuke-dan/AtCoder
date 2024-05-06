# N, Q = map(int,input().split())
# A = list(map(int,input().split()))
# questions = [list(map(int,input().split())) for _ in range(Q)]

# rec_A = []
# rec_A.append(A[0])

# for i in range(len(A)-1):
#     rec_A.append(rec_A[i] + A[i+1])

# for question in questions:
#     ans = rec_A[question[1]-1]
#     minus = rec_A[question[0]-2] if question[0]>1 else 0
#     ans -= minus
#     print(ans)

N, Q = map(int,input().split())
A = list(map(int,input().split()))
qs = [list(map(int,input().split())) for _ in range(Q)]

rec_A = [0,]

for i in range(len(A)):
    rec_A.append(rec_A[i] + A[i])

# print(rec_A)
# for question in questions:
#     ans = rec_A[question[1]]
#     minus = rec_A[question[0]-1]
#     ans -= minus
#     print(ans)

for q in qs:
    ans = rec_A[q[1]] - rec_A[q[0]-1]
    print(ans)