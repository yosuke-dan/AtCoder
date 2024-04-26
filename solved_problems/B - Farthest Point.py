import math

# 距離を求める関数
def distance(a,b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


N = int(input())

# print('----------------------')

coordinate_list = []
for _ in range(N):
    coordinate_list.append(list(map(int,(input().split()))))

print(coordinate_list)
# print('----------------------')


for i in range(N):
    longest_distance = 0
    for j in range(N):
        distance_btw_ij = distance(coordinate_list[i],coordinate_list[j])
        if i != j and distance_btw_ij > longest_distance:
            longest_distance = distance_btw_ij
            farest_point = j + 1
    print(farest_point)