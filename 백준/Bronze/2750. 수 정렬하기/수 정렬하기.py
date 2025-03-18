num_test_case = int(input())

test_case = []
for _ in range(num_test_case):
    test_case.append(int(input()))
    
test_case.sort()

for result in test_case:
    print(result)