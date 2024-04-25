X = input()
ans = 'No'

if len(X) == 1:
    if X.isupper():
        ans = 'Yes'
        print(ans)
    else:
        print(ans)
    exit()

if X[0].isupper() and X[1:len(X)].islower():
    ans = 'Yes'
print(ans)



# s= input()

# if s != s.lower() and s[1:] == s[1:].lower():
#   print('Yes')
#   # print(s[1:])
# else:
#   print('No')