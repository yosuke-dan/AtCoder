X = input()

for i in range(len(X)):
    if X.count(X[i]) == 1:
        print(i+1)
        exit()
