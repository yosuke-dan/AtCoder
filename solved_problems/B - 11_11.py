M = int(input())
D = list(map(int,input().split()))


'''
1 11 111

2 22 222
3 33 333


11 11 111
'''
# ゾロ目がありえる月のリスト
Z = [1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77,88,99]

cnt = 0
# zorome_list = []

for m in range(M):
    month = m + 1
    if month not in Z:
        continue
    if month < 10:
        day = month
    else:
        day = month % 10
        month = day
    while day <= D[m]:
        cnt += 1
        # zorome_list.append(str(month)+'/'+str(day))
        day = day * 10 + month
    
print(cnt)
# print(zorome_list)