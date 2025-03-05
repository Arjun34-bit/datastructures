def sort012(arr):
    # code here
    temp=0
    p=0
    for i in range(0,len(arr)-1):
        p+=1
        for j in range(p,len(arr)):
            if(arr[i]>arr[j]):
                temp=arr[i]     
                arr[i]=arr[j]  
                arr[j]=temp
    return arr

print(sort012([1, 0, 2, 1, 1, 1, 0]))   #Brute Force Approach

def nsort012(arr):
    # code here
    #Solved using DNF method (Dutch Flag Algorithm)

    #  low     mid-1   mid                    high
    # [0,  0,0,  0,     1, 1,1,1,    2,2,2,2,2]
    #    Red       White        Blue
    # Three Pointer Approach


    low=0
    mid=0
    high=len(arr)-1
    
    temp=0
    temp1=0
    while(mid<=high):
        if(arr[mid]==0):
            temp=arr[mid]
            arr[mid]=arr[low]
            arr[low]=temp
            mid+=1
            low+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            high-=1
    return arr

print(nsort012([1, 0, 2, 1, 1, 1, 0]))  #Optimal Approach