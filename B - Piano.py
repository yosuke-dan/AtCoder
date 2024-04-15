w_b = list(map(int,input().split()))


piano = 'wbwbwwbwbwbw'
piano += piano
piano += piano
piano += piano
piano += piano
piano += piano

len_piano = len(piano)

piano_slices = set()

# 何文字目から切り取る？
for i in range(len_piano):
    # 何文字切り取る？
    for j in range(len_piano):
        piano_pattern = piano[i:i+j+1]
        piano_slices.add((piano_pattern.count('w'),piano_pattern.count('b')))

#print(sorted(piano_slices))

found = False

for slice in piano_slices:
    if slice == (w_b[0],w_b[1]):
        print('Yes')
        found = True

if not found:
    print('No')