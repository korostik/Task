# https://codeforces.com/contest/1669/problem/B

def f(a):
    d = {}
    for i in range(len(a)):
        d[a[i]] = d.get(a[i], 0) + 1
        if d[a[i]] >= 3:
            return a[i]
    return -1

t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    print(f(a))
