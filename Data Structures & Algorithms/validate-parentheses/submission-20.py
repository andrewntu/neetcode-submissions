class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}":"{", ")":"(", "]": "["}
        stack = []
        for string in s:
            if string in valid:
                if stack and stack[-1] == valid[string]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(string)
        return len(stack) == 0

                    
                

        