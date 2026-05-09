import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedInput = re.sub(r'[^a-zA-Z0-9]', '',s.strip().replace(" ","").lower())
        cleanedReveredInput = cleanedInput[::-1]    
        if cleanedInput == cleanedReveredInput:
            return True
        return False