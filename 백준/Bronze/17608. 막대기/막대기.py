import sys

n = int(sys.stdin.readline())
sticks = [int(sys.stdin.readline()) for _ in range(n)]

count = 0
max_height = 0

# 오른쪽에서 보니까 뒤에서부터 확인
for height in reversed(sticks):
    if height > max_height:
        count += 1
        max_height = height

print(count)
