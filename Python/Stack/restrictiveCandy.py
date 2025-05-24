def candy(s):
    arr=[]
    result=[]
    
    for i in range(0,len(s)):
        arr.append(s[i])
        
    for j in range(0,len(arr)):
        last=len(arr) - 2 - j   
        for k in range(j+1,k):
            if arr[j] != arr[k]:
                if result[-1] != arr[j]:
                    result.append(arr[j])
            else:
                continue
            
    print(arr)
            
    return result
                
            
    
    

s="geeks"  
print(candy(s))