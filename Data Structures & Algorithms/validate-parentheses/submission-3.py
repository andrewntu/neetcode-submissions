class Solution:
    def isValid(self, s: str) -> bool:
        para = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in para:
                if not stack or stack[-1] is not para[c]:
                    return False
                else: 
                    stack.pop()
            else:    
                stack.append(c)
        return True if not stack else False