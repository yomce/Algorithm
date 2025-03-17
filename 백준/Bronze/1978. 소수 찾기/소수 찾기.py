def find_prime_num(n:int = 1000):

    prime_num_list = [2]
    for num in range(3, n+1):
        
        for prime_number in prime_num_list:
            if num % prime_number == 0:
                break
            
            if prime_num_list[-1] == prime_number:
                prime_num_list.append(num)
                
    return prime_num_list

num_test_case = int(input())

test_list = list(map(int, input().split()))

num_prime = 0
list_all_prime_num = find_prime_num(n = 1000)

for test_case in test_list:
    if test_case in list_all_prime_num:
        num_prime += 1
        
print(num_prime)