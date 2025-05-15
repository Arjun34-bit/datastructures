# arr=[17,15,8,9,2,4,6]

# my approach
#First Swap

# 17 8 15 2 4 6 9

#Second Swap

# 8 17 2 4 6 15 9

#Third Swap

# 8 2 4 6 17 15 9

def divide(head):
    temp=head

    oddStart=None
    oddEnd=None

    evenStart=None
    evenEnd=None

    while temp is not None:
        x=temp.data
        next_node = temp.next
        temp.next = None
        if x % 2 != 0:
            if oddStart is None:
                oddStart=temp
                oddEnd=temp
            else:
                oddEnd.next=temp
                oddEnd=oddEnd.next
        else:
            if evenStart is None:
                evenStart=temp
                evenEnd=temp
            else:
                evenEnd.next=temp
                evenEnd=evenEnd.next
                
        temp = next_node
        
    
    if oddEnd is not None:
        oddEnd=None
    if evenStart is None:
        evenStart=oddStart
    else:
        evenEnd.next=oddStart
    
    return evenStart
        




