class Solution:
    def isValid(self, s: str) -> bool:
        p = {"(": ")", "[": "]", "{": "}"}
        stack=[]
        for i in s:
            if i in p: 
                stack.append(i)
            else:
                if not stack or p[stack.pop()]!=i:
                    return False
        return not stack
