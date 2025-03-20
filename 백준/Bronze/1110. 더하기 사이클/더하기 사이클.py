n = input()

if len(n) ==1:
        n = "0" + n
        
num = n
count = 0

while True:
    first_digit = num[0]            #10의 자리 숫자
    second_digit = num[1]           #1의 자리 숫자
    
    new_num = str(int(first_digit) + int(second_digit))
    num = second_digit + new_num[-1:]
    
    count += 1
    
    if num == n:
        print(count)
        break

