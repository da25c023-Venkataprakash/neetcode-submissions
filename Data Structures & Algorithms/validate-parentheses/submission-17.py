class Solution:
    def isValid(self, s: str) -> bool:
        d= {"{":'}', "(":')', "[":']'}
        box=[]
        for i in s:
            if i in d:
                box.append(i)
            
            elif box and d[box.pop()]==i:
                continue
            else:
                return False
                
        return len(box) == 0