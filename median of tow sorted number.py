class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ans = []
        n = len(nums1)+len(nums2)
        j = 0
        k = 0
        if n==0:
            return None
        for i in range (0,n//2+2):
            if j <= len(nums1)-1 and k<= len(nums2)-1:
                if nums1[j]<=nums2[k]:
                    ans.append(nums1[j])
                    j +=1
                else: 
                    ans.append(nums2[k])
                    k +=1
            elif j>len(nums1)-1 and k<=len(nums2)-1:
                ans.append(nums2[k])
                k +=1
            elif j<=len(nums1)-1 and k>len(nums2)-1:
                ans.append(nums1[j])
                j +=1
        if n%2 ==0:
            median = (ans[len(ans)-2]+ans[len(ans)-3])/2
        else:
            median = float(ans[len(ans)-2])
        print(ans)
        return median
