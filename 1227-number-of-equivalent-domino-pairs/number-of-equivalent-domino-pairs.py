class Solution(object):
    def numEquivDominoPairs(self, dominoes):

        count = {}   # stores frequency of dominoes
        ans = 0

        for a, b in dominoes:

            # Make fixed form
            key = (min(a, b), max(a, b))

            # Add previous occurrences
            ans += count.get(key, 0)

            # Increase frequency
            count[key] = count.get(key, 0) + 1

        return ans