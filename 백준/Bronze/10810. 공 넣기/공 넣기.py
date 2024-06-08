n,m = map(int,input().split())

basket_lst = [[] for _ in range(n+1)]
for i in range(m):
    start,end,ball = map(int,input().split())
    for i in range(start,end+1): #i=1,2,3,4
        if len(basket_lst[i])>0:
            basket_lst[i].pop()
            basket_lst[i].append(ball)
        else:
            basket_lst[i].append(ball)
basket_lst = basket_lst[1:] 
for ball in basket_lst:
    if len(ball) == 0:
        ball.append(0)

result = []
for ball_lst in basket_lst:
    x = str(ball_lst[0])
    result.append(x)

print(' '.join(result))