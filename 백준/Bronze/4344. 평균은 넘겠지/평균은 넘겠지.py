num = int(input())
for i in range(num):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1: ]
    
    avg = sum(scores)/N
    avg_over = []
    for i in scores:
        if i > avg:
            avg_over.append(i)
    percent = len(avg_over)/N*100
    
    print(f"{percent:.3f}%")
    