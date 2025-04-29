#Ugly Number

def uglyNumber(n):
    dp=[0]*n
    dp[0]=1
    p1=0
    p2=0
    p3=0

    for i in range(1,n):
        twoM = dp[p1] * 2
        threeM = dp[p2] * 3
        fiveM = dp[p3] * 5

        dp[i]=min(twoM,min(threeM,fiveM))
        
        if dp[i] == twoM:
            p1+=1

        if dp[i] == threeM:
            p2+=1

        if dp[i] == fiveM:
            p3+=1

    return dp[n-1]
    
print(uglyNumber(10))