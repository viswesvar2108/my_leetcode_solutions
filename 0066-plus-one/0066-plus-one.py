class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #converting digits to string for joining purpose
        string_digits = map(str,digits)

        #joining each char element then converting to int
        number = int(''.join(string_digits))

        #then adding one to the number
        number = number + 1
        digits = [int(digit) for digit in str(number) ]
        return digits