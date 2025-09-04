def countFreq(a):
    mp={}
    for i in range(0,len(a)):
        mp[a[i]]=mp.get(a[i],0)+1
        
    result=[]
    print(mp)
    for i in range(1,len(a)+1):
        if i not in mp:
            result.append(0)
        else:
            result.append(mp[i])
    
    return result

print(countFreq([2,3,2,3,5]))