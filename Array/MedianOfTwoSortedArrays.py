'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 =len(nums1)
        len2 = len(nums2)
        i=0
        j=0
        k=0
        
        arr3 = [0 for _ in range(len1+len2)]
        while(i<len1):
            arr3[k] =nums1[i]
            k +=1
            i +=1
        while(j<len2):
            arr3[k] =nums2[j]
            k +=1
            j +=1
        arr3.sort()
        len3 = len(arr3)
        if len3%2 ==0:
            z=len3//2
            a1= float(arr3[z])
            a2= float(arr3[z-1])
            return float((a1+a2)/2)
        else:
            z = len3//2 
            return float(arr3[z])

            
