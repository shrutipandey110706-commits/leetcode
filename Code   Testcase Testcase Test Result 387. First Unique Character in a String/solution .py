class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        frequency={}
        for ch in s:
            frequency [ch] = frequency.get(ch, 0) + 1 """frequency.get(ch, 0) + 1 = Look for ch in the dictionary. If it exists, give me its value. If it doesn't exist, give me 0"""


        for i in range (len(s)):
            if frequency[s[i]]==1:
                return i   

        return -1         
            
