N = input()

slice_patterns = list()

for i in range(len(N)):
    for j in range(len(N)):
        pattern = N[j:j+(i+1)]
        if not pattern in slice_patterns:
            slice_patterns.append(pattern)

print(len(slice_patterns))