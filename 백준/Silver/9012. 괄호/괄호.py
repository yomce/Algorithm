import sys

n = int(sys.stdin.readline())

for _ in range(n):
    line = sys.stdin.readline().strip()
    stack = []
    is_vps = True

    for char in line:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                is_vps = False
                break

    if stack:
        is_vps = False

    print("YES" if is_vps else "NO")
