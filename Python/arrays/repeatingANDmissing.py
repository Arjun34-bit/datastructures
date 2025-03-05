# Brute Force Approach

# arr=[2,1,3,5]   [1,2,3,4,5]

#Better Approach 
#Time Complexity : O(N^2) because nested for loops
#Space Complexity : O(1) 
def missingandrepeating(arr):
    missing=-1
    repeating=-1

    for i in range(1,len(arr)):                 #1
        count=0
        for j in range(0,len(arr)-1):           #2
            if(arr[j]==i):
                count+=1
        if(count==2):
            repeating=i
        if(count==0):
            missing=1
        if(repeating!=-1 and missing!=-1):
            break
    return [repeating,missing]


# print(missingandrepeating([1]))  #Brute Force Approach


#Better Approach 
#Time Complexity : O(2N) because two for loops
#Space Complexity : O(N+2) created hash_arr of length of array in addition 2
def missingandrepeating1(arr):
    hash_arr=[0]*(len(arr)+2)
    missing=-1
    for i in range(0,len(arr)):                             #1
        hash_arr[arr[i]]=hash_arr[arr[i]]+1
    for j in range(1,len(hash_arr)):                        #2
        if(hash_arr[j]==0):
            missing=j
        if(missing!=-1):
            break
    return missing


print(missingandrepeating1([2,4,1]))


def missingandrepeating2(arr):
    n=len(arr)
    SN=(n * (n+1))/2
    SN2=(n * (n+1) * (2*n+1))/6
    S=0
    S2=0
    for i in range(0,n):
        S+=arr[i]
        S2+=arr[i] * arr[i]

    val1=S-SN
    val2=S2-SN2
    
    if(val1!=0):
        val2=val2/val1
    
    x=(val1+val2)/2
    y=x-val1
    
    return y