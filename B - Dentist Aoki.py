N, Q = map(int, input().split())
tooth = list(map(int,input().split()))

tooth_set = set(tooth)

for teeth in tooth_set:
    if tooth.count(teeth) % 2 == 1:
        N -= 1

print(N)
    


# teeth_drop_duplicates = []
# duplicates = 0

# for teeth in tooth:
#     if not teeth in teeth_drop_duplicates:
#         teeth_drop_duplicates.append(teeth)
#     else:
#         duplicates += 1