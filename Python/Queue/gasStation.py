def startStation(gas, cost):       # Time Complexity : O(N)   Space Complexity : O(1)      
    if sum(gas) < sum(cost):
        return -1
    
    start=0
    currGas=0
    
    for i in range(0,len(gas)):
        currGas += gas[i] - cost[i]
        
        if currGas < 0:
            start=i+1
            currGas=0
            
            
    return start