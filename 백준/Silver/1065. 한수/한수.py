N = int(input())

if N == 1000:
    N = 999
    
if N <= 99:
   results = N
   
else:
    results = 99
    
    for i in range(100,N+1):
        a, b, c = map(int,str(i))
        d = b-a  # d는 공차
        if c-b == d:
            results +=1
        else:
            continue
        
print(results)