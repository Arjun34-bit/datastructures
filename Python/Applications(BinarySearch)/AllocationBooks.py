class LinearSearch():
    def allocateBooks(self,books,pages):
        currStudent=1
        currPage=0
        
        n=len(books)
        
        for i in range(0,n):
            if currPage+books[i] <= pages:
                currPage+=books[i]
            else:
                currStudent+=1
                currPage=books[i]
                
        return currStudent


    def books(self,books,students):
        if(len(books)<students):
            return -1
        
        low=max(books)
        high=sum(books)
        
        for pages in range(low,high):
            countStudent=self.allocateBooks(books,pages)
            
            if countStudent==students:
                return pages
            

class BinarySearch():
    def allocateBooks(self,books,pages):
        currStudent=1
        currPage=0
        
        n=len(books)
        
        for i in range(0,n):
            if currPage+books[i] <= pages:
                currPage+=books[i]
            else:
                currStudent+=1
                currPage=books[i]
                
        return currStudent


    def books(self,books,students):
        if(len(books)<students):
            return -1
        
        low=max(books)
        high=sum(books)

        while low<=high:
            mid=low+(high-low)//2

            noOfStudents=self.allocateBooks(books,mid)

            if noOfStudents > students:
                low=mid+1
            else:
                high=mid-1
        return low                          #this concent is called polarity




obj=LinearSearch()
obj1=BinarySearch()
book=[12, 34, 67, 90]
student=2
print("Linear Search",obj.books(book,student))
print("Binary Search",obj1.books(book,student))