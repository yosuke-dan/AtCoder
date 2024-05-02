# S = list(input())
# N = len(S)

# patterns = []

# for i in range(N-1):
#     for j in range(i+1,N):
#         result = S
#         print(i,j)
#         temp = result[i]
#         result[i] = result[j]
#         result[j] = temp
#         pattern = ''.join(result)
#         print(pattern)
#         patterns.append(pattern)

# print(patterns)

# print(len(set(patterns)))

### ChatGPTによるリファクタリング

# S = list(input())
# N = len(S)

# unique_patterns = set()  # 重複を許さないためにセットを使用

# for i in range(N-1):
#     for j in range(i+1, N):
#         result = S[:]  # Sのコピーを作成
#         result[i], result[j] = result[j], result[i]  # シンプルなスワップ
#         pattern = ''.join(result)
#         unique_patterns.add(pattern)  # セットに追加

# # print(unique_patterns)
# print(len(unique_patterns))

# ↑これだとTLEです。

S = list(input())

Sset = set(S)
# print(Sset)
lenS = len(S)

# 全ての文字の選び方
all_patterns = lenS * (lenS - 1) // 2

# 同じ文字を選ぶijのパターンの数
same_patterns = 0

for ss in Sset:
    ss_count = S.count(ss)
    if ss_count >= 2:
        same_patterns += ss_count * (ss_count - 1) // 2

#　違う文字を選ぶパターン
diff_patterns = all_patterns - same_patterns

if same_patterns >= 1:
    ans = diff_patterns + 1
else:
    ans = diff_patterns

print(ans)