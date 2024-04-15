S = input()
len_S = len(S)
ans = 'No'

if not (S[0] == '<' and S[-1] == '>'):
    print(ans)
    exit(0)

for i in range(len_S - 2):
    if not S[i+1:i+2] == '=':
        print(ans)
        exit(0)

ans = 'Yes'
print(ans)



# 模範解答
s = input()
if s == "<"+"="*(len(s)-2)+">":
  print("Yes")
else:
  print("No")