class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        uniqeType= len(set(candyType))
        can_eat = len(candyType)//2

        return min(uniqeType, can_eat)