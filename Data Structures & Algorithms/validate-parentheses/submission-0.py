class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}
        for chars in s:
            if chars in closeToOpen:
                if stack and stack [-1] == closeToOpen[chars]:
                    stack.pop()
                else: 
                    return False
                
            else:
                stack.append(chars)

        return True if not stack else False