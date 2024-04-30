# S = input()

# B_pos = S.find('B')
# C_pos = S.find('C')

# S_A = S[0:B_pos]
# S_B = S[B_pos:C_pos]
# S_C = S[C_pos:len(S)]

# for a in list(S_A):
#     if not a == 'A':
#         print('No')
#         exit()
# for a in list(S_B):
#     if not a == 'B':
#         print('No')
#         exit()
# for a in list(S_C):
#     if not a == 'C':
#         print('No')
#         exit()
# print('Yes')


S = input()
L = ['A','B','C']
ans = ''
for l in L:
    ans += S.count(l) * l

if S == ans:
    print('Yes')
else:
    print('No')


S = input()
l = list(S)
if l == sorted(l):
    print('Yes')
else:
    print('No')