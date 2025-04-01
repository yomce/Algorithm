import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.read
preorder = list(map(int, input().split()))

def postorder(start, end):
    if start >= end:
        return
    root = preorder[start]
    split = end
    for i in range(start + 1, end):
        if preorder[i] > root:
            split = i
            break
    postorder(start + 1, split)
    postorder(split, end)
    print(root)

postorder(0, len(preorder))
