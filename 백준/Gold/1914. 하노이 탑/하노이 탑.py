import sys

def move(num: int, start: int, goal: int, result: list):
    middle = 6 - start - goal  # 보조 기둥 계산

    if num > 1:
        move(num - 1, start, middle, result)  # 작은 원판들을 보조 기둥으로 이동

    result.append(f"{start} {goal}")  # 이동 기록 저장

    if num > 1:
        move(num - 1, middle, goal, result)  # 작은 원판들을 목표 기둥으로 이동


num = int(sys.stdin.readline().strip())  # 빠른 입력

print(2**num - 1)  # 최소 이동 횟수 출력

if num <= 20:  # n이 너무 크면 출력량을 제한
    result = []
    move(num, 1, 3, result)
    sys.stdout.write("\n".join(result) + "\n")  # 한 번에 출력
