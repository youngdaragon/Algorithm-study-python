def count_possible_positions(x1, y1, r1, x2, y2, r2):
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  

    if d == 0 and r1 == r2:  # 원이 무한대로 겹치는 경우
        return -1
    elif d > r1 + r2 or d + min(r1, r2) < max(r1, r2):  # 두 원이 겹치지 않는 경우
        return 0
    elif d == r1 + r2 or d + min(r1, r2) == max(r1, r2):  # 두 원이 한 점에서 만나는 경우
        return 1
    else:  # 두 원이 두 점에서 만나는 경우
        return 2

if __name__ == "__main__":
    T = int(input())  # 테스트 케이스 개수 입력

    for _ in range(T):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(count_possible_positions(x1, y1, r1, x2, y2, r2))
