# 同じ文字だけで構成されているか判定する
def isConposedByOneCharacter(s):
    length = len(s)
    # 空文字
    if length == 0:
        return False
    # 1文字
    if length == 1:
        return True
    # 2文字以上
    for i in range(len(s)-1):
        if not s[i] == s[i + 1]:
            return False
    return True


test =  'aaa'
ans = isConposedByOneCharacter(test)

print(test,ans)