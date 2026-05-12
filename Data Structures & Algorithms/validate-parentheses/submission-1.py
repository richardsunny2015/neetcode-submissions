class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {
            "[": "]",
            "{": "}",
            "(": ")"
        }
        for c in s:
            if c in braces:
                stack.append(braces[c])
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False
        return not stack
            


