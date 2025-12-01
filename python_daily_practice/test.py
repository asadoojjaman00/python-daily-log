"""
Q1. Concatenation of Array
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums of length n, you want to create an array
 ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
"""



# class Solution(object):
#     def getConcatenation(self, nums):
#         ans = []
#         n2 = len(nums) *2
        
#         while 0 < n2:
#             i =0
#             for i in nums:
#                 ans.append(nums[i])
#                 n2-=1
#         return ans
    
# l = [1,2,1]
# obj = Solution()
# print(obj.getConcatenation(l))
class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        n = len(nums)
        for i in range(n):
            ans.append(nums[i])
        for i in range(n):
            ans.append(nums[i])
        return ans
    
obj = Solution()
print(obj.getConcatenation([1,2,1]))