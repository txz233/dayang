def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        start =0
        sign = 1
        ans =0
        maxint=(1<<31)-1
        if str =="":
            return 0
        if str[0]=="+":
            start +=1
        elif str[0]=="-":
            start +=1
            sign = -1
        for i in range (start,len(str)):
            if str[i]<"0" or str[i]>"9":
                break
            else:
                ans=ans*10+int(str[i])
        ans=ans*sign
        if ans > maxint:
            return 2147483647
        if ans < (-1-maxint):
            return -2147483648
        return ans
