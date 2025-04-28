def countPairs(head1, head2, x):   #Brute Force TC:O(N*M)  SC:O(1)  
    count=0
    
    mover1=head1
    
    while mover1:
        mover2=head2
        while mover2:
            if (mover1.data + mover2.data) == x:
                count+=1
            mover2=mover2.next
        mover1=mover1.next
        
    return count


def countPairs(head1, head2, x):   # Optimised Solution TC:O(N+M) SC:(N)
    mp={}
    
    count=0
    
    mover1=head1
    
    while mover1:
        diff=x - mover1.data
        mp[diff]=diff
        mover1=mover1.next
        
    mover2=head2
    
    while mover2:
        if mover2.data in mp:
            count+=1
        mover2=mover2.next
        
    return count