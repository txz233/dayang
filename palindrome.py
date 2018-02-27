class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sample = 0
        bit = 0
        last = 0
        while sample < x:
            last =sample
            sample = 10 * sample + (x % 10)
            x = (x - (x % 10)) // 10
            bit += 1
            print(sample)
            print(last)
            print(x)
            print(bit)
        if bit % 2 == 0:
            if sample == last:
                return True
            else:
                return False
        else:
            if x == sample:
                return True
            else:
                return False
