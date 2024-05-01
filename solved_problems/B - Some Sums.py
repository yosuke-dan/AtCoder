N, A, B = map(int,input().split())

# def SomeSums(number):
#     return sum(list(map(int,list(str(number)))))

def betterSum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum

ans = 0
for i in range(N+1):
    if A <= betterSum(i) <= B:
        ans += i

print(ans)