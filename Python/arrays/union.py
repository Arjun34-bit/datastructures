def findUnion(arr1,arr2):
    result={}
    i=0
    j=0
    n1=len(arr1)-1
    n2=len(arr2)-1
    
    while i<n1 and j<n2:
        if arr1[i]<=arr2[j]:
            if len(result)==0 or arr1[i] not in result:
                result[i]=arr1[i]
                # print(result)
            i+=1
        else:
            if len(result)==0 or arr2[j] not in result:
                result['i']=arr2[j]
                print(result)
            j+=1
    return len(result)


arr1=[1,2,3,4,5]
arr2=[1,2,3]
print(findUnion(arr1,arr2))