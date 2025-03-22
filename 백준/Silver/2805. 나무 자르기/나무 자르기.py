import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
# trees.sort()  # 있어도 되고 없어도 됨

def get_cut_sum(trees, h):
    total = 0
    for tree in trees:
        if tree > h:
            total += (tree - h)
    return total

def binary_search(trees, target):
    left = 0
    right = max(trees)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        total = get_cut_sum(trees, mid)

        if total >= target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

print(binary_search(trees, M))
