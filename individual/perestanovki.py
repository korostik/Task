n = int(input())
permutation = []
ans = []
def search():
    if len(permutation) == n:
        ans.append(permutation)
    else:
        for i in range(1, n + 1):
            if i in permutation:
                continue
            permutation.append(i)
            search()
            permutation.pop()

if __name__ == '__main__':
    search()
