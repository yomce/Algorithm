#1085 직사각형에서 탈출
x, y, w, h = map(int, input().split())
a = [x, y, w-x, h-y]
mini = a[0]
for i in a:
    if i < mini:
        mini = i
print(mini)