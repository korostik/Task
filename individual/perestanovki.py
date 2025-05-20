n = int(input())
permutation = []

def search():
    if len(permutation) == n:
        print(" ".join(map(str, permutation)))
    else:
        for i in range(1, n + 1):
            if i in permutation:
                continue
            permutation.append(i)
            search()
            permutation.pop()

search()