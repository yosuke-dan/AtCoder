N = int(input())
wallet = list(map(int,input().split()))

for i in range(N-1):
    l = list(map(int,input().split()))
    c = wallet[i] // l[0]
    wallet[i+1] += c*l[1]

# print(wallet)
print(wallet[-1])