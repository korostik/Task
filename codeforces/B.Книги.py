# https://codeforces.com/problemset/problem/279/B

n, t = map(int, input().split())
a = [int(x) for x in input().split()]
max_len = -1
left = 0
now_sum = 0
for i in range(len(a)):
    now_sum += a[i]
    if now_sum > t:
        max_len = max(i - left, max_len)
        now_sum -= a[left]
        left += 1
    else:
        max_len = max(i - left + 1, max_len)
print(max_len)
