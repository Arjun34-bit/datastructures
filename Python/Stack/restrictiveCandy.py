def Reduced_String(k, s):
    if k == 1:
        return ""
    
    stack = []  

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()  
        else:
            stack.append([char, 1])
    
    return "".join(char * count for char, count in stack)
    
    
s="geeeksforgeeeks"
k=3
print(Reduced_String(k,s))