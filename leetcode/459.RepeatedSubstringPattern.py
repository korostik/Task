class Solution:
    def z_function(self, s):
        n = len(s)
        z = [0] * n
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1
        return z
        
    def repeatedSubstringPattern(self, s: str) -> bool:
        a = self.z_function(s)
        n = len(a)
        for i in range(1, n):
            if len(a) % i != 0:
                continue
            el = (len(a) // i - 1) * i
            ans = 1
            for j in range(i, n, i):
                if a[j] != el:
                    ans = -1
                    break
                el -= i
                if el <= 0:
                    break
            if ans == 1:
                return True
        return False
