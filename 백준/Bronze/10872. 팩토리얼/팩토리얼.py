# #10872 팩토리얼
# N = int(input())  
# result = 1
# for i in range(1,N+1):
#   result *= i
    
# print(result)

def factorial(n: int) -> int:
    if n > 0:
        return n*factorial(n-1)
    else:
        return 1

n = int(input())
print(factorial(n))