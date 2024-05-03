# 全探索でOK 時間はギリギリ

H, W, N = map(int,input().split())
T = input()
field = [None] * H
for h in range(H):
    field[h] = list(input())

ans = 0

for h in range(1,H-1):
    for w in range(1,W-1):
        # 海チェック
        if field[h][w] == '#':
            continue
        # 現在地
        now_h = h
        now_w = w
        fall_into_sea = False
        # 移動
        for t in T:
            if t == 'L':
                now_w -= 1
            if t == 'R':
                now_w += 1
            if t == 'U':
                now_h -= 1
            if t == 'D':
                now_h += 1
            if field[now_h][now_w] == '#':
                fall_into_sea = True
                break
        if not fall_into_sea:
            ans += 1
print(ans)