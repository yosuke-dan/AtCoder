N = int(input())
cards = list(map(int,input().split()))

cards = sorted(cards, reverse=True)

# print(cards)

A_turn = True
Alice, Bob = 0, 0
    
for card in cards:
    if A_turn:
        Alice += card
        A_turn = False
    else:
        Bob += card
        A_turn = True

print(Alice-Bob)