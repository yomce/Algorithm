n = int(input())

count = 0   #count변수 0으로 초기화

while n >= 0:
    if n % 5 == 0:
        count += n//5
        print(count)
        break
    
    n -= 2
    count += 1
    
else:
    print(-1)
    