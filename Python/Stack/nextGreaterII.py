def nextGreaterElements(nums):
    n=len(nums)

    if n<=1:
        return [-1]

    nge=[-1] * n
    st=[]

    for i in range(2*n-1,-1,-1):

        while st and st[-1] <= nums[i%n]:
            st.pop()

        if i<2*n:
            if st:
                nge[i%n]=st[-1]
            else:
                nge[i%n]=-1

        st.append(nums[i%n])

    return nge
        
        
arr=[1,2,1]
print(nextGreaterElements(arr))        #  TC:O(2n + 2n)  ~ TIME COMPLEXITY:O(n)  and SPACE COMPLEXITY:O(n)