a = int(input())
b = int(input())
c = int(input())
num = a*b*c
digits = list(map(int, str(num))) 
for i in range(10):
    print(digits.count(i))