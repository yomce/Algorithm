def find_prime_num(n = 10000):
    """
    find list of prime number under num 'n'
    """
    
    prime_num_list = [2]
    
    for num in range(3, n+1):
        
        for prime_number in prime_num_list:
            if num % prime_number == 0:  # not frame, next num
                break
            elif num % prime_number != 0:  # can't divid
                pass
            if prime_num_list[-1] == prime_number:
                prime_num_list.append(num)
        
    return prime_num_list
    
    
num_test = int(input())
test_case = []

for test in range(num_test):
    input_num = int(input())
    test_case.append(input_num)

list_all_frame_num = find_prime_num(n=10000)

for test_num in test_case:
    
    middle_num = test_num // 2
    
    while True:
        if middle_num in list_all_frame_num:
            left_num = middle_num
            break
        else:
            middle_num -= 1
    
    left_num_index = list_all_frame_num.index(middle_num)
    
    while True:
        left_num = list_all_frame_num[left_num_index]
        right_num = test_num-left_num
        
        if right_num in list_all_frame_num:
            break
        
        else:
            left_num_index -= 1
    
    left_num, right_num
            
    print(f"{left_num} {right_num}")