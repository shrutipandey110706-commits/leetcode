class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2

        a=1# ek stairs ke liye shirrf ek step
        b=2 # 2 stairs ke liye hum ek ek krke bhi ja skte h or 2 karke bhi isliye two steps   

        for i in range (3,n+1) :
            current = a+b
            a=b
            b=current
        return b    
