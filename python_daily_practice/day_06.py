"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):

        if not strs:
            return ""

        first_val = strs[0]
        last_val = strs[-1]

        if not first_val or not last_val:
            return ""

        i = 0
        y_compare = ""

        if first_val[0] == last_val[0]:
            while i < len(first_val) and i < len(last_val) and first_val[i] == last_val[i]: 
                y_compare += first_val[i]
                i+=1       
        else : 
            return y_compare
        

        for td in strs:
            x_compare = td[:i]
            if x_compare != y_compare:
                while not td.startswith(y_compare):
                    y_compare = y_compare[:-1]
                    if y_compare == "":
                        return y_compare
        return y_compare

obj = Solution()
print(obj.longestCommonPrefix(["aaa","aa","aaa"]))