
from collections import deque, defaultdict

# 입력 처리
N = int(input())  # 사람 수 입력
friend_dict = defaultdict(deque)  # 친구 관계 저장
graph = [input() for _ in range(N)]  # 친구 관계 입력 받기

# 친구 관계 설정
for i in range(N):
    for idx, is_friend in enumerate(graph[i]):
        if is_friend == "Y":
            friend_dict[i].append(idx)

# 지금까지 최대 친구 수 
max_two_friends = 0

for i in range(N): #i번 사람에 대한 친구
    visited = [False] * N  # 방문 여부를 기록할 리스트
    queue = deque()  # BFS 큐
    two_friends = set()  # 2-친구를 저장할 집합 (중복 방지)
    
    # 1-직접 친구들을 큐에 추가
    for friend in friend_dict[i]:
        two_friends.add(friend)  # 직접 친구 추가
        queue.append(friend)
        visited[friend] = True
    
    # 2-간접 친구(친구의 친구) 탐색
    while queue:
        person = queue.popleft()  # 내 직접 친구를 한 명씩 꺼내서 탐색
        for friend in friend_dict[person]:
            if friend != i and not visited[friend]:  # 자기 자신 제외, 방문 안 한 사람만
                two_friends.add(friend)  # i번째 사람의 2-친구 추가
                visited[friend] = True  # 방문 처리
    
    # 현재 사람의 2-친구 수를 계산하고 최대값 갱신
    max_two_friends = max(max_two_friends, len(two_friends))

print(max_two_friends)