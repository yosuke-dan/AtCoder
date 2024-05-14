K ,G ,M = map(int,input().split())

glass, mug = 0, 0

for _ in range(K):
    if glass == G:
        glass = 0
    elif mug == 0:
        mug = M
    else:
        # glassの空きとmugの今の量を比較
        glass_space = G - glass
        if glass_space >= mug:
            glass += mug
            mug = 0
        else:
            mug -= glass_space
            glass = G

print(glass,mug)
    