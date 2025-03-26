'''

    def get(i):
    
        Use the given get function which is given as an argument here, 
        that returns the value at index i
        in the infinite sorted binary array.

'''

def firstOne(get):
    
    # Write your code here.
    # This function returns the first index of the occurence of 1
    low=0
    high=1

    while get(high)<1:
        low=high
        high=high*2

    while low<=high:
        mid=low+(high-low)//2

        if get(mid)==1:
            f=-1
            high=mid-1
        elif get(mid)<1:
            low=mid+1
        else:
            high=mid-1
    return low