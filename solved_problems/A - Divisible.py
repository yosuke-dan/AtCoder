
header = list(map(int,input().split()))
values = list(map(int,input().split()))
print(header)
print(values)

output = []

for i in range(header[0]):
    if values[i] % header[1] == 0:
        output.append(str(int(values[i] / header[1])))

print(*output)