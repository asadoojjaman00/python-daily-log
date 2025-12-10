import math
class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        for i in range(1, len(complexity)):
            if complexity[i] <= complexity[0]:
                return 0
        
        MOD = 10**9+7
        
        return math.factorial(len(complexity) - 1) % MOD
obj = Solution()
n = obj.countPermutations([0,1,2,3,4,5,6,4,3,2,1,2,3])
print(n)