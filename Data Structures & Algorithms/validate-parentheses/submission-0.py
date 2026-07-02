class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cs = { ")" : "(", "]" : "[", "}" : "{" }
        for b in s:
            if b in cs:
                if stack and stack[-1] == cs[b]:
                    stack.pop()

                else:
                    return False
            else:
                stack.append(b)
        return True if not stack else False
    
