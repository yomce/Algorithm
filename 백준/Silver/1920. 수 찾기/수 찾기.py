import sys
input = sys.stdin.readline

N = int(input())
A = set(map(int, input().split()))  # set으로 만들기!

M = int(input())
B = list(map(int, input().split()))

for num in B:
    print(1 if num in A else 0)
