def dfs(ground, visited, x, y, n, m, symbol):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        visited[cx][cy] = True
        if symbol == '-':
            if cy + 1 < m and ground[cx][cy + 1] == '-' and not visited[cx][cy + 1]:
                stack.append((cx, cy + 1))
        elif symbol == '|':
            if cx + 1 < n and ground[cx + 1][cy] == '|' and not visited[cx + 1][cy]:
                stack.append((cx + 1, cy))

def count_wooden_planks(n, m, ground):
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                if ground[i][j] == '-':
                    dfs(ground, visited, i, j, n, m, '-')
                    count += 1
                elif ground[i][j] == '|':
                    dfs(ground, visited, i, j, n, m, '|')
                    count += 1
    
    return count

# 입력 처리
n, m = map(int, input().split())
ground = [list(input().strip()) for _ in range(n)]

# 결과 출력
print(count_wooden_planks(n, m, ground))
