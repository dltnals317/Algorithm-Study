while (True):
    record = {}
    second_rank_lst = []
    N,M = map(int,input().split())
    if N==0 and M==0:
        break
    else:
        for i in range(N):
            week = list(map(int,input().split()))
            for x in week:
                if x in record.keys():
                    record[x]+=1
                else:
                    record[x] = 1
        record_lst = sorted(record.items(),key= lambda x:x[1],reverse=True)
        first_cnt = record_lst[0][1]
        second_cnt = record_lst[1][1]
        second_rank_lst.append(record_lst[1][0])
        for i in range(2,len(record_lst)):
            if second_cnt == record_lst[i][1]:
                second_rank_lst.append(record_lst[i][0])
            else:
                break
    second_rank_lst.sort()            
        
    print(" ".join(map(str,second_rank_lst)))