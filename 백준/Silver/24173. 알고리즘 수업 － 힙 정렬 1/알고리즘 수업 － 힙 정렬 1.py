import sys
input = sys.stdin.readline
def heapify(arr,parent_idx,n):
    global count
    smallest = parent_idx
    left_child = 2 * parent_idx + 1
    right_child = 2 * parent_idx + 2
    if (left_child < n and arr[left_child] < arr[smallest]):
        smallest = left_child
    if (right_child < n and arr[right_child] < arr[smallest]):
        smallest = right_child
    

    if smallest != parent_idx:#index상으로 뭔가 바뀐게 있다면
        
        arr[parent_idx],arr[smallest] = arr[smallest],arr[parent_idx] # 실제 값도 바꿔주고
        count +=1
        if count == k:
            if arr[smallest] < arr[parent_idx]:
                print(arr[smallest],arr[parent_idx])
            elif arr[smallest] > arr[parent_idx]:
                print(arr[parent_idx],arr[smallest])
            exit()
        heapify(arr,smallest,n) #바뀐 것에 대해서도 최소힙 진행(가장 루트 말고)

def heap_sort(arr):
    global count
    n = len(arr)
    #최소 힙 정렬
    for i in range(n//2 - 1, -1,-1):
        heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i] #root와 가장 마지막 요소를 바꾸고 나서,
        count +=1
        if count == k:
            if arr[i] < arr[0]:
                print(arr[i],arr[0])
            elif arr[i] > arr[0]:
                print(arr[0],arr[i])
            exit()
        heapify(arr,0,i) # 변경된 heap에서 다시 최소 heap 구성

    
# 테스트
n,k = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
heap_sort(arr)
print(-1)
