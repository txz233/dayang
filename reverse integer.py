class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x//(10**5)) != 0:
            ans1 = 0
        if x >=0:
            neg = False
        else:
            neg = True
            x = -x
        bitnum = 0
        ans = 0
        for i in range (0,5):
            if x//(10**i)>=1:
                bitnum +=1
            elif x//(10**i) ==0:
                break
        for i in range (0,bitnum):
            bit = (x%(10**(i+1))-x%(10**(i)))/(10**(i))
            ans += bit*(10**(bitnum-i-1))
        ans1 =int(ans)
        if neg:
            ans1 = -ans1
        return ans1
