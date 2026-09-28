class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        bits = num.bit_length() #1 << 3= 1000

        mask = (1<<bits)-1 # Create a number having all 1s of the same length
        return num ^ mask



        
