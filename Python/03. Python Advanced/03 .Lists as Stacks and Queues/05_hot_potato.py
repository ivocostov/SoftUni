from collections import deque

kids_names = deque(name for name in input().split())
tosses = int(input())


def game(participants, ball_tosses):
    while len(participants) > 1:
        for rotation in range(ball_tosses - 1):
            participants.append(participants.popleft())

        print(f"Removed {participants.popleft()}")
    print(f"Last is {kids_names[0]}")


game(kids_names, tosses)
