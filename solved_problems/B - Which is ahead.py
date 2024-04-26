# N = input()

# array = input()

# Q = int(input())

# for _ in range(Q):
#     querry = list(input().split())
#     if array.find(querry[0]) < array.find(querry[1]) :
#         print(querry[0])
#     else:
#         print(querry[1])

N = int(input())

numbers = list(map(int,input().split()))

Q = int(input())

for i in range(Q):
    query = list(map(int,input().split()))
    for number in numbers:
        if number == query[0]:
            print(query[0])
            break
        elif number == query[1]:
            print(query[1])
            break
        
