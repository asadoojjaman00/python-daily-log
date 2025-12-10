"""
leetcode : 3583. Count Special Triplets(Medium)

You are given an integer array nums.

A special triplet is defined as a triplet of indices (i, j, k) such that:

0 <= i < j < k < n, where n = nums.length
nums[i] == nums[j] * 2
nums[k] == nums[j] * 2
Return the total number of special triplets in the array.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [6,3,6]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 1, 2), where:

nums[0] = 6, nums[1] = 3, nums[2] = 6
nums[0] = nums[1] * 2 = 3 * 2 = 6
nums[2] = nums[1] * 2 = 3 * 2 = 6
Example 2:

Input: nums = [0,1,0,0]

Output: 1

Explanation:

The only special triplet is (i, j, k) = (0, 2, 3), where:

nums[0] = 0, nums[2] = 0, nums[3] = 0
nums[0] = nums[2] * 2 = 0 * 2 = 0
nums[3] = nums[2] * 2 = 0 * 2 = 0

"""


# Count Special Triplets
class Solution(object):
    def specialTriplets(self, nums):
        MOD = 10**9 + 7
        from collections import defaultdict

        left = defaultdict(int)
        right = defaultdict(int)

        for num in nums:
            right[num] += 1

        ans = 0
        for j in range(len(nums)):
            mid = nums[j]
            double = mid * 2

            right[mid] -= 1

            count_i = left[double]
            count_k = right[double]

            ans = (ans + count_i * count_k) % MOD

            left[mid] += 1
        return ans
obj = Solution()
fn = obj.specialTriplets([8,4,2,8,4])
print(fn)