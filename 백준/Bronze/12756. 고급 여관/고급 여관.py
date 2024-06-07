card_lst = []
for i in range(2):
    fight,live = map(int,input().split())
    card_lst.append((fight,live))
a_fight = card_lst[0][0]
a_live = card_lst[0][1]
b_fight = card_lst[1][0]
b_live = card_lst[1][1]

while True:
    b_live -= a_fight
    a_live -= b_fight
    if a_live<=0 or b_live <=0:
        break
if b_live <= 0 and a_live <= 0:
    print("DRAW")
elif b_live <= 0 and a_live>0:
    print("PLAYER A")
elif a_live <= 0 and b_live>0:
    print("PLAYER B")