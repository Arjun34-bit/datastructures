def removeDuplicates(a):
    n=len(a)

    a.sort()

    i=0
    j=i+1

    while i<n and j<n:
        if a[i]!=a[j]:
            a[i+1]=a[j]
            i+=1
        else:
            j+=1
    return i+1


a=[1,1,2,3,3]
print(removeDuplicates(a))