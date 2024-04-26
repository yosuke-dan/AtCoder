s = input()

s_list = []
for i in range(len(s)):
    s_list.append(s[i])

s_set = sorted(list(set(s_list)))

# print(s_list, "\n", s_set)

s_dict = {}
for s_s in s_set:
    # print(s_s,s_list.count(s_s))
    s_dict.setdefault(s_s,s_list.count(s_s))

# print(s_dict)
print(max(s_dict, key=s_dict.get))