def duplicates(arr):
    seen=set()
    for a in arr:
        if a in seen:
            return True
        else:
            seen.add(a)
    return False
    
print(duplicates([1,1,2,3,4,5,6]))

#Time Complexity O(n)  for loop iterates to the length of the array
#Space Complexity O(n) for creating the new set