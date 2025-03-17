N = int(input())  
fac_list = []
result = 1
for i in range(1,N+1):
  fac_list.append(i)
for j in fac_list:
    result *= j
    
print(result)