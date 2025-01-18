from collections import deque

snakes = deque([0])
q = int(input())

for _ in range(q):
    query = input()

    if len(query) > 1:
        q, l = query.split()
        q, l = int(q), int(l)
    else:
        q = int(query)

    if q == 1:
        snakes.append(snakes[len(snakes) - 1] + l)
    elif q == 2:
        snakes.popleft()
    else:
        print(snakes[l - 1] - snakes[0])
