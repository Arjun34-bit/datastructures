def bubbleSort(arr):
    for i in range(0,len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
                count+=1
                
                
                
arr=[4,1,3,9,7]
print(bubbleSort(arr))
print(arr)