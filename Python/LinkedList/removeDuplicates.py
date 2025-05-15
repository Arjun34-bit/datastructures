def removeDuplicates(head):
    temp=head
    
    while temp != None and temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.nexte
        
    return temp