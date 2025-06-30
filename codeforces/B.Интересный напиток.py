# https://codeforces.com/contest/706/problem/B

def f(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if x < a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return l


n = int(input())
a = [int(x) for x in input().split()]
a.sort()
q = int(input())
for i in range(q):
    m = int(input())
    print(f(a, m))
