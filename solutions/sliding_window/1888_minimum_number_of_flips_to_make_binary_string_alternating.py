"""
LeetCode 1888
Minimum Number of Flips to Make the Binary String Alternating

Given a binary string s, we can:
1. Rotate the string (move first character to the end).
2. Flip any character (0 -> 1 or 1 -> 0).

Return the minimum number of flips needed to make the string alternating.
"""


# ------------------------------------------------
# User Solution
# ------------------------------------------------

class SolutionUser:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        a1, a2 = "", ""
        for i in range(len(s)):
            a1 += "0" if i % 2 == 0 else "1"
            a2 += "1" if i % 2 == 0 else "0"

        res = len(s)
        d1, d2 = 0, 0
        l = 0

        for j in range(len(s)):
            if s[j] != a1[j]:
                d1 += 1
            if s[j] != a2[j]:
                d2 += 1

            if (j - l + 1) > n:
                if s[l] != a1[l]:
                    d1 -= 1
                if s[l] != a2[l]:
                    d2 -= 1
                l += 1

            if (j - l + 1) == n:
                res = min(res, d1, d2)

        return res


# ------------------------------------------------
# Optimized Solution (Constant Extra Memory)
# ------------------------------------------------

class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s

        res = n
        diff1 = diff2 = 0
        left = 0

        for right in range(len(s)):

            # expected characters for alternating patterns
            expected1 = '0' if right % 2 == 0 else '1'
            expected2 = '1' if right % 2 == 0 else '0'

            if s[right] != expected1:
                diff1 += 1
            if s[right] != expected2:
                diff2 += 1

            # maintain sliding window size n
            if right - left + 1 > n:
                left_expected1 = '0' if left % 2 == 0 else '1'
                left_expected2 = '1' if left % 2 == 0 else '0'

                if s[left] != left_expected1:
                    diff1 -= 1
                if s[left] != left_expected2:
                    diff2 -= 1

                left += 1

            if right - left + 1 == n:
                res = min(res, diff1, diff2)

        return res


"""
Approach (Optimized)

1. Rotations are simulated by doubling the string:
       s = s + s

2. Two alternating patterns exist:
       010101...
       101010...

3. Instead of building pattern strings, compute expected
   characters using index parity.

4. Use a sliding window of size n to evaluate every rotation.

5. Track mismatches with both patterns and take the minimum.

Time Complexity: O(n)
Space Complexity: O(1) extra
"""
