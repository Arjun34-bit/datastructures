def printNos(count,n):
    if count>n:
        return
    print(count)
    count+=1
    
    printNos(count,n)
    
def main(n):
    count=1
    printNos(count,n)
    
print(main(10))