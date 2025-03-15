
# Time Complexity is 
# O(NLOGN) + O(NLOGN) + O(N1 +N2)= O(NLOGN)

# Space Complexity is 
# O(N1+N2)

def findUnion(arr1,arr2):
    result=[]
    i=0
    j=0
    n1=len(arr1)
    n2=len(arr2)
    
    arr1.sort()
    arr2.sort()
    
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if len(result)==0 or arr1[i] !=result[-1]:
                result.append(arr1[i])
            i+=1
        else:
            if len(result)==0 or arr2[j] !=result[-1] :
                result.append(arr2[j])
            j+=1
    while j<n2:
        if len(result)==0 or arr2[j] != result[-1]:
            result.append(arr2[j])
        j+=1
    while i<n1:
        if len(result)==0 or arr1[i] !=result[-1]:
            result.append(arr1[i])
        i+=1
    return len(result)


arr1=[1,2,3,4,5]
arr2=[1,2,3]
print(findUnion(arr1,arr2))