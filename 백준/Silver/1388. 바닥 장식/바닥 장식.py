n, m = map(int, input().split())
floor = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)] #방문한 곳 다시 안 보도록 체크용 리스트

count = 0

for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue #방문한 칸이면 스킵

        if floor[i][j] == '-':
            # 가로 방향 탐색
            newj = j
            while newj < m and floor[i][newj] == '-':
                visited[i][newj] = True
                newj += 1
            count += 1

        elif floor[i][j] == '|':
            # 세로 방향 탐색
            newi = i
            while newi < n and floor[newi][j] == '|':
                visited[newi][j] = True
                newi += 1
            count += 1

print(count)

