nine = [int(input()) for _ in range(9)]
max_value = max(nine)
max_index = nine.index(max_value) + 1
print(max_value)  
print(max_index)
