def move(n:int, start:int, goal:int):
    middle = 6-start-goal
    if n == 1:
        print(start, goal)
        return
    
    move(n-1, start, middle)    # 작은 원판들을 보조 기둥으로 이동
    print(start, goal)          # 이동 기록 저장
    move(n-1, middle, goal)     # 작은 원판들을 목표 기둥으로 이동
        
n = int(input())  
print(2**n - 1) 
if n <= 20 :
    move(n, 1, 3)
