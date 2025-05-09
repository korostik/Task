def f(k, n, subset):
    if (k == n + 1):
        print(subset)
    else:
        subset.append(k)
        f(k + 1, n, subset)
        subset.pop()
        f(k + 1, n, subset)

f(1, 3, [])
