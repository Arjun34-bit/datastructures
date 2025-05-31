class Solution():
    def merge(self,a,b):
        temp=Node(0)
        res=temp
        
        while (a != None and b != None):
            if a.data < b.data:
                temp.bottom=a
                temp=temp.bottom
                a=a.bottom
            else:
                temp.bottom=b
                temp=temp.bottom
                b=b.bottom
                
        if a != None:
            temp.bottom=a
        else:
            temp.bottom=b
            
        return res.bottom
    
    def flatten(self,root):
        #Your code here 
        
        if root == None or root.next == None:
            return root
            
        root.next = self.flatten(root.next)
        
        root = self.merge(root,root.next)
        
        return root