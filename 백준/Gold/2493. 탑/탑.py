import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n  # 인덱스 0-based

for i in range(n):
    # 현재 탑보다 낮은 탑은 모두 제거
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()

    # 남아있는 탑이 있으면 신호 수신 가능
    if stack:
        result[i] = stack[-1] + 1  # +1: 1-based 인덱스 출력용

    # 현재 탑을 스택에 넣음
    stack.append(i)

print(' '.join(map(str, result)))
