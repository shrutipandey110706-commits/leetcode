class Solution:
    def grayCode(self, n):
        
        # This list will store the Gray code sequence
        result = []

        # Loop from 0 to (2^n - 1)
        # (1 << n) means 2 raised to power n
        for i in range(1 << n):

            # Generate Gray code using formula:
            # gray = i XOR (i shifted right by 1)
            #
            # Example:
            # i = 5  -> 101
            # i>>1   -> 010
            # XOR    -> 111 = 7
            gray = i ^ (i >> 1)

            # Add generated value into result list
            result.append(gray)

        # Return final Gray code sequence
        return result