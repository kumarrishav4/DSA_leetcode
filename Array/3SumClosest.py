'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104

'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum =float('inf')
        count = 0
        for i in range(n-2):
            left = i+1
            right = n-1
            while left<right:
                current_total = nums[i]+nums[left]+nums[right]
                if abs(target-current_total) < abs(target-closest_sum):
                    closest_sum = current_total

                if current_total<target:
                    left+=1

                elif current_total>target:
                    right-=1

                else:
                    return closest_sum
        return closest_sum

a=Solution()
print(a.threeSumClosest([-1,2,1,-4],1))