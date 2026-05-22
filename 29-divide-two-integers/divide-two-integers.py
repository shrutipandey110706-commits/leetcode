class Solution:
    def divide(self, dividend, divisor):

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Check sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Divide using subtraction + bit shift
        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Double temp value
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient