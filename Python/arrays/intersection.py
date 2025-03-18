def intersection(a,b):
    n1=len(a)
    n2=len(b)

    a.sort()
    b.sort()

    left=0
    right=left+1

    count=0

    while left<n1 and right<n2:
        if a[left]==b[right]:
            count+=1
            left+=1
            right+=1
        elif b[right]>a[left]:
            left+=1
        else:
            right+=1
    return count+1



a=[1, 2, 4, 3, 5, 6]  #11,23,24,75,89
b=[3, 4, 5, 6, 7] #2,4,89
print(intersection(a,b))