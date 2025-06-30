# https://codeforces.com/contest/1343/problem/B

def f(n):
    a = []
    chet = 2
    summ_chet = 0
    for i in range(n // 2):
        summ_chet += chet
        a.append(chet)
        chet += 2
        
        
    nechet = 1
    summ_nechet = 0
    for i in range(n // 2 - 1):
        summ_nechet += nechet
        a.append(nechet)
        nechet += 2
        
    if (summ_chet - summ_nechet) % 2 == 0:
        print("NO")
    else:
        a.append(summ_chet - summ_nechet)
        print("YES")
        print(*a)
    
        
    
 
t = int(input())
for i in range(t):
    n = int(input())
    f(n)
