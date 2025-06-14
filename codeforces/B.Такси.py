# https://codeforces.com/contest/158/problem/B

n = int(input())
a = [int(x) for x in input().split()]
ans = 0
count1 = 0
count2 = 0
count3 = 0
for i in range(len(a)):
    if a[i] == 4:
        ans += 1
    elif a[i] == 1:
        count1 += 1
    elif a[i] == 2:
        count2 += 1
    else:
        count3 += 1
 
count1 -= count3
if count1 < 0:
    count1 = 0
 
if count2%2 == 1:
    count1 -= 2
count2 = count2 // 2 + count2 % 2
if count1 < 0:
    count1 = 0
if count1 % 4 == 0:
    count1 = count1 // 4
else:
    count1 = count1 // 4 + 1
ans += count1+ count2 + count3
print(ans)
