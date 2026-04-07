class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = "".join(char.lower() for char in s if char.isalnum())
        
        left, right = 0, len(letters)-1
        # if len(letters) == 1:
        #     return False
        if left+1 == right:
            if letters[left] == letters[left+1]:
                return True
            return False
        while left < right:
            if letters[left] != letters[right]:
                return False
            left+=1
            right-=1
        return True