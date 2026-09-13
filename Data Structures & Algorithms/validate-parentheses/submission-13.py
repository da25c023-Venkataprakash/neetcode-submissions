class Solution:
    def isValid(self, s: str) -> bool:
        characters = {'(': ')', '{':'}', '[': ']'}
        stack=[]
        for i in s:
            if i in characters:
                stack.append(i)
            elif i in characters.values():
                if stack:
                    val= stack.pop()
                    print(val)
                    if characters[val] !=i:
                        return False
                else:
                    return False
        
        if stack:
            return False
        return True
          
       




        