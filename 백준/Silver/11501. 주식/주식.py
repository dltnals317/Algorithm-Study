t = int(input())


for _ in range(t):
    n = int(input())
    stock = list(map(int,input().split()))
    profit = 0
    max_price = 0
    selected = []
    for i in range(len(stock)-1,-1,-1):
        if stock[i]>max_price:
            max_price = stock[i]
        else:
            value = max_price - stock[i]
            profit+=value
    print(profit)