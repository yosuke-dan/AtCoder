def main():

    N = int(input())

    # 立法数のリストを作る

    cube_li = []

    cube = 1
    x = 1

    while cube <= N:
        cube_li.append(str(cube))
        x += 1
        cube = x ** 3

    cube_li.reverse()

    for c in cube_li:
        if isKaibun(c):
            print(c)
            exit()

def isKaibun(s):
    if s == s[::-1]:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()