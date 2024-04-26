N = input()

N_list = []

for i in range(len(N)):
    N_list.append(N[i])

N_list_set = set(N_list)

# print(N_list)
# print(N_list_set)

count_list = []
for n in N_list_set:
    count_list.append(N_list.count(n))
    
# print(count_list)

for i in range(1,len(N)+1):
    if not count_list.count(i) in [0,2]:
        print('No')
        exit()

print('Yes')