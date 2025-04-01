def selection(arr):

    n=len(arr)

    for i in range(0,n-1):
        mini=i
        for j in range(i,n):
            if arr[j]<arr[mini]:
                mini=j
        temp=arr[mini]
        arr[mini]=arr[i]
        arr[i]=temp


arr=[4,5,6,1,2,3]
print(selection(arr))
print(arr)