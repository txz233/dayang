class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        l = len(s)
        nunit = l // (2 * numRows - 2)
        x = l - nunit*(2*numRows-2)
        s1 = (2 * numRows - 2) * "X" + s + x * "X" + (2 * numRows - 2) * "X"
        nunit = len(s1) // (2 * numRows - 2)
        ans = ""
        for i in range(0, numRows):
            for j in range(0, nunit):
                if i == 0:
                    ans += s1[j * (2 * numRows - 2)]
                elif i < numRows - 1 and i >= 1:
                    ans += s1[j * (2 * numRows - 2) + i]
                    ans += s1[(j + 1) * (2 * numRows - 2) - i]
                elif i == numRows - 1:
                    ans += s1[j * (2 * numRows - 2) + i]
        ans1 = ans.replace("X", "")
        return ans1
