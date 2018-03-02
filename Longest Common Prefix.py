class Solution:
#divde and conquer
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs) == 1:
            return strs[0]
        leftpart = strs[:(len(strs)//2)]
        rightpart = strs[(len(strs)//2):]
        leftpart=self.longestCommonPrefix(leftpart)
        rightpart=self.longestCommonPrefix(rightpart)
        minlen = min(len(leftpart),len(rightpart))

        for i in range (0,minlen):
            if leftpart[i] != rightpart[i]:
                return leftpart[:i]
        return leftpart[:minlen]
