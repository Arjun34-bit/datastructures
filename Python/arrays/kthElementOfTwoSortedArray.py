
# Union of two sorted array and returning the kth element of result array whwn its es length is equal to k 

# Worst Case Scenario
    # Time Complexity is O(N1+N2)
    # Space Complexity is O(N1+N2)

# Best Case Scenario
    # Time Complexity is O(K)
    # Space Complexity is O(K)

def kth(a,b,k):
    n1=len(a)
    n2=len(b)
    
    i=0
    j=0
    
    
    result=[]
    
    while i<n1 and j<n2:
        if a[i]<=b[j]:
            result.append(a[i])
            if len(result)==k:
                print(result)
                return result[k-1]
            i+=1
        else:
            result.append(b[j])
            if len(result)==k:
                print(result)
                return result[k-1]
            j+=1
    
    while i<n1:
        result.append(a[i])
        if len(result)==k:
            print(result)
            return result[k-1]
        i+=1
            
    while j<n2:
        result.append(b[j])
        if len(result)==k:
            print(result)
            return result[k-1]
        j+=1
    return 0
                    
                    

    
a=[5 ,5, 8, 8, 8, 9, 11, 11, 11, 11, 11]
b=[4 ,4, 4, 4, 6, 8, 9, 9, 9, 11, 13]

print(kth(a,b,2))