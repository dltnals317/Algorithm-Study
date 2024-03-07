import sys
input = sys.stdin.readline
N,K = map(int,input().split())
coin_lst = []
cnt = 0

for i in range(N):
    coin = int(input())
    coin_lst.append(coin)

sored_lst = sorted(coin_lst,reverse = True)

for coin in sored_lst:
    cnt += K//coin
    K = K%coin

print(cnt)