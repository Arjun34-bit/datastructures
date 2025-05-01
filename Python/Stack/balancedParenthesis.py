def isBalanced(s):
    st=[]
    
    for b in s:
        if b=="(" or b=="[" or b=="{":
            st.append(b)
        else:
            if len(st)==0:
                return False
            
            tp=st[-1]
            
            if (b==")" and tp=="(") or (b=="]" and tp=="[") or (b=="}" and tp=="{"):
                st.pop()
            else:
                return False
                
        
                
    if len(st)==0:
        return True
    
    return False
    
s="()"
print(isBalanced(s))