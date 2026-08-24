class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # Case 1: All letters are uppercase
        if word.isupper():
            return True
        
        # Case 2: All letters are lowercase
        if word.islower():
            return True
        
        # Case 3: Only the first letter is uppercase
        if word[0].isupper() and word[1:].islower():
            return True
        
        # Otherwise, invalid capital usage
        return False
