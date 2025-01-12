n, d = map(int, input().split())
snakes = [list(map(int, input().split())) for _ in range(n)]

ans = [[T * (L + k + 1) for T, L in snakes] for k in range(d)]
# ans = []
# for k in range(d):
#   temp = []
#   for t, l in snakes:
#     temp.append(t * (l + k+1))
#   ans.append(temp)

[print(max(x)) for x in ans]
