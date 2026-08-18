class Solution:
    def subarraySum(self, nums, k):

        # Stores prefix sum and how many times it has occurred
        prefix_sum = {0: 1}

        # Stores the current prefix sum
        sum = 0

        # Stores the total number of valid subarrays
        count = 0

        for num in nums:

            # Add the current number to the prefix sum
            sum += num

            # We need to find a previous prefix sum equal to sum - k
            required_sum = sum - k

            # If required_sum exists, we found one or more
            # subarrays whose sum is equal to k
            if required_sum in prefix_sum:
                count += prefix_sum[required_sum]

            # Store the current prefix sum in the dictionary
            # If it already exists, increase its frequency by 1
            prefix_sum[sum] = prefix_sum.get(sum, 0) + 1

        # Return the total number of subarrays with sum equal to k
        return count
