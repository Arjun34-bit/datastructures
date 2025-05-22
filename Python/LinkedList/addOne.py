class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
        
    def addOne(self,head):
        #Returns new head of linked List.
        reverseHead=self.reverse(head)
    
        carry=1
        temp=reverseHead
        
        while temp != None:
            temp.data=temp.data + carry
            
            if temp.data < 10:
                carry=0
                break
            else:
                temp.data=0
                carry=1
            temp=temp.next
            
            
        if carry==1:
            newNode=Node(1)
            temp=self.reverse(reverseHead)
            newNode.next=temp
            return newNode
            
            
        return self.reverse(reverseHead)



class Solution:     # Optimal Approach Used Backtracking
    def helper(self,temp):
        if temp == None:
            return 1
        carry=self.helper(temp.next)
        
        temp.data += carry
        
        if temp.data < 10:
            return 0
        temp.data=0
        return 1
    def addOne(self,head):
        #Returns new head of linked List.
        carry = self.helper(head)
        
        if carry == 1:
            newNode = Node(1)
            newNode.next=head
            return newNode
            
        return head