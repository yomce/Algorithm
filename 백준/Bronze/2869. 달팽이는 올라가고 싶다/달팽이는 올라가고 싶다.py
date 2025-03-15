A, B, V = map(int, input().split())
climb = (V-A)//(A-B)
climbing = (V-B)%(A-B)
if climbing == 0:
    days = climb +1
else:
    days = climb +2
print(days)