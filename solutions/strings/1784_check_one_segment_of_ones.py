"""
LeetCode 1784: Check if Binary String Has at Most One Segment of Ones

Problem:
Given a binary string s, return True if the string contains at most one
contiguous segment of '1's, otherwise return False.
"""

# ---------------------------
# Your Solution
# ---------------------------

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if "0" in s:
            n = s.index("0")
            if "1" in s[n:]:
                return False
            else:
                return True
        else:
            return True


# ---------------------------
# Alternative Solution
# ---------------------------

class SolutionOptimized:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s


"""
Explanation of Alternative Approach:
If the substring "01" appears in the string, it means that after a segment
of '1's ended, another '1' appeared later, creating multiple segments.
Therefore, a valid string with at most one segment of ones must NOT contain "01".

Time Complexity: O(n)
Space Complexity: O(1)
"""
