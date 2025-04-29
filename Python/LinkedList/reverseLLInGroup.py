class Solution:
    def leftOutReverse(self,head):
        firstNode=head  
        curr=head.next   
        prev=None
        
        while curr:
            temp=curr.next   
            curr.next=prev   
            prev=curr   
            curr=temp 
            
            if curr==None:
                firstNode.next=prev
        return None
        
    def firstReverse(self,head,k):
        firstNode=head
        
        curr=head
        prev=None
        
        count=1
        
        while count<=k:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            
            if(count==k):
                firstNode.next=curr
                self.leftOutReverse(firstNode)
            
            count+=1
            
        return prev
    def reverseKGroup(self, head, k):
        # Code here
        
        newHead=self.firstReverse(head,k)
        return newHead