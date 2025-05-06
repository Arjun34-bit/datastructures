def removeLoop(head):        
    slow=head
    fast=head
    
    while fast != None and fast.next != None:
        slow=slow.next
        fast=fast.next.next
        
        if slow==fast:
            slow=head
            if slow == fast:
                while fast.next != slow:
                    fast = fast.next
                fast.next = None
                return True
            
            while slow.next != fast.next:
                slow=slow.next
                fast=fast.next
            fast.next=None
            return True
            
    return False