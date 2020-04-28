#https://leetcode.com/problems/maximum-subarray/
nums=[-2,1,-3,4,-1,2,1,-5,4]

#DP O(n) with constant space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        output=nums[0]
        cur=nums[0]
        for i in range(1,len(nums)):
            cur=max(cur+nums[i],nums[i])
            if cur>output:
                output=cur
        return output
