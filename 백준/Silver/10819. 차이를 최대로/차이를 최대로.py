from itertools import permutations

#(1) 순열만들기
n = int(input())
arr = list(map(int, input().split()))
p = list(permutations(arr,n))

result_max = 0

# (2) 반복문으로 튜플을 꺼내 각 순열마다 차이의 합(s)을 구하고, 최대값을 answer에 저장한다
for i in p:
    s = 0                       #각 순열의 합을 담음
    for j in range(n-1):
        s += abs(i[j]-i[j+1])
        
 # 모든 경우 원소들끼리의 차이의 절댓값의 합을 max함수를 이용하여 갱신
    result_max = max(result_max, s)

print(result_max)