from queue import Queue

def reverseQueue(q):      #Brute Force Approach
    st=[]
    while q.qsize() != 0:
        st.append(q.get())
        
    print(st)
        
        
    while st:
        q.put(st.pop())
        
        
    return q
    
    
    
q=Queue()
q.put(1)
q.put(2)
q.put(3)

print(reverseQueue(q))
        
       
            
        

def reverseQueue( q):
    if q.empty():
        return q
    item = q.get()
    reverseQueue(q)
    q.put(item)
    return q