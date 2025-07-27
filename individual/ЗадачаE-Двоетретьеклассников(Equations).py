n, m = map(int, input().split())
d = {1: 2}
i = 1
k = 2
k2 = 2
count = 2
while i != m:
    d[count] = k2 + 1
    k -= 1
    count += 1
    if k == 0:
        k2 += 1
        k = k2
    i += 1

dmax = n - d[m] + 1
d2 = {}
for i in range(1, m + 1):
    d2[i] = d2.get(i, i + 1)

if m >= n:
    dmin = 1
else:
    dmin = n - d2[m] + 1

if dmin <= 0 or dmax <= 0 or m > (1 + n) * n // 2:
    print(-1)
else:
    print(dmin, dmax)