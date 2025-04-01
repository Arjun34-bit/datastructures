def insertion(arr):

    n=len(arr)

    for i in range(0,n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp

            j-=1


arr=[4,3,2,1]
print(insertion(arr))
print(arr)