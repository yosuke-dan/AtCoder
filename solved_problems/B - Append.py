A = []

Q = int(input())

for i in range(Q):
    Q_type, Q_value = map(int,input().split())
    if Q_type == 1:
        A.append(Q_value)
    else:
        print(A[-Q_value])

# 感想
# 難易度＝めっちゃ簡単