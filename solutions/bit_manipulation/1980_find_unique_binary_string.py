"""
LeetCode 1980
Find Unique Binary String

Given an array nums containing n unique binary strings of length n,
return a binary string of length n that does not appear in nums.
"""


# ------------------------------------------------
# User Solution
# ------------------------------------------------

from typing import List

class SolutionUser:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        nums.sort()
        l = []

        for i in range(n):
            o = int(nums[i], 2)

            if l and l[i - 1] + 1 == o:
                l.append(o)
            else:
                if i == 0 and o == 0:
                    l.append(0)
                elif i == 0 and o != 0:
                    return "0" * n
                else:
                    return bin(l[i - 1] + 1)[2:].zfill(n)

        return bin(n)[2:].zfill(n)


# ------------------------------------------------
# Optimized Solution (Cantor's Diagonal Trick)
# ------------------------------------------------

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        result = []

        for i in range(n):
            if nums[i][i] == '0':
                result.append('1')
            else:
                result.append('0')

        return "".join(result)


"""
Optimized Approach (Diagonal Construction)

Key Idea:
Construct a binary string that differs from the i-th string
in the i-th position.

Example:
nums = ["000", "111", "001"]

Take opposite of diagonal bits:

nums[0][0] = 0 -> choose 1
nums[1][1] = 1 -> choose 0
nums[2][2] = 1 -> choose 0

Result = "100"

This guarantees the result differs from every string in nums
in at least one position.

Time Complexity: O(n)
Space Complexity: O(n)
"""
