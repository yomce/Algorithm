find_list = []
for _ in range(9):
    mem_height = int(input())
    find_list.append(mem_height)
find_list.sort()


sum_height = sum(find_list)
fake = []
for i in range(9):
    for j in range(i+1, 9):
        if len(fake) == 2:
            continue
        if sum_height - (find_list[i]+find_list[j]) == 100:
            fake.append(find_list[i])
            fake.append(find_list[j])

for i in find_list:
    if i in fake:
        continue
    print(i)