#Time Complexity : O(n)
#Space Complexity : o(n)

class Solution:
	def pascal(self,result,row,col,ans):
		if col==(row):
			return result
		ans=ans*(row-col)
		ans=ans//col
		result.append(ans)
		self.pascal(result,row,col+1,ans)
		return result

	def nthRowOfPascalTriangle(self,n):
		result=[1]
		ans=1
		return self.pascal(result,n,1,ans)
	



result=[1]
ans=1
obj=Solution()
print(obj.nthRowOfPascalTriangle(5))