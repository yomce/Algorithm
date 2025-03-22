import sys
input = sys.stdin.readline

n, c = map(int, input().split())

houses = [int(input()) for _ in range(n)]
houses.sort()

def install_wifi(distance):
    count = 1  # 첫 번째 집엔 설치
    last_installed = houses[0]

    for i in range(1, n):
        if houses[i] - last_installed >= distance:
            count += 1
            last_installed = houses[i]

    return count

# 이진 탐색
left = 1
right = houses[-1] - houses[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    if install_wifi(mid) >= c:
        answer = mid
        left = mid + 1  # 더 넓은 거리 도전
    else:
        right = mid - 1

print(answer)
