X = input()

for i in range(len(X)-1):
    if not X[i] == X[i+1]:
        hako = i + 1
print(hako)