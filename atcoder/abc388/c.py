from bisect import bisect_left

n = int(input())
mochi = list(map(int, input().split()))

mochi.sort()

ans = 0
for i in range(n):
  input_mochi = bisect_left(mochi, mochi[i] * 2)
  ans += n - input_mochi

print(ans)
