def isSubset( a, b):
    c1={}
    c2={}
    for i in range(0,len(a)):
        c1[a[i]]=c1.get(a[i],0)+1
    for j in range(0,len(b)):
        c2[b[j]]=c2.get(b[j],0)+1

    for num in c2:
        if c2[num]>c1.get(num,0):
            return False
    return True

print(isSubset([1,2,2],[1,1]))