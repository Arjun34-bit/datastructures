def startStation(gas, cost):        
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