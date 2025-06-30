# https://codeforces.com/contest/363/problem/B

n, k = map(int, input().split())
a = [int(x) for x in input().split()]
prefix = [0]
summi = 0
for i in range(n):
    summi += a[i]
    prefix.append(summi)
 
mini = 10**10
ans = []
for i in range(len(a) - k + 1):
    if prefix[i + k] - prefix[i] < mini:
        ans = []
        ans.append(i + 1)
        mini = prefix[i + k] - prefix[i]
print(*ans)
