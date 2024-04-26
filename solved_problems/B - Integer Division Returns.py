X = int(input())
X_dev10 = X // 10
X_lastzero = X % 10 == 0

if X_lastzero:
    print(X_dev10)
else:
    print(X_dev10+1)


# X = input()

# if len(X) == 1:
#     print(1)
#     exit()
# if X[0] == '-' and len(X) == 2:
#     print(0)
#     exit()


# if X[-1] == '0':
#     print(X[0:len(X)-1])
# else:
#     if X[0] == '-':
#         print(X[0:len(X)-1])
#     else:
#         print(int(X[0:len(X)-1])+1)

