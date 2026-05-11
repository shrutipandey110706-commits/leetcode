class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = {}
        #count frequency
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1

        #stores freq
        values=freq.values()

        return len(values)==len(set(values))
