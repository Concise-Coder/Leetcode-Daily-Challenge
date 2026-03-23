"""
LeetCode 1594
Maximum Non Negative Product in a Matrix

You are given a grid of integers.

You can move only:
• Right
• Down

Goal:
Find the maximum NON-NEGATIVE product from (0,0) → (m-1,n-1)

If the result is negative → return -1
Else return result % (10^9 + 7)

------------------------------------------------

Approach (Human Thinking):

Key Problem:
Multiplication with negative numbers flips sign.

So at each cell, we must track:
• Maximum product so far
• Minimum product so far

Why?
Because:
    negative × negative = positive (very important)

------------------------------------------------

Step 1: Define DP tables
max_dp[i][j] → maximum product reaching (i,j)
min_dp[i][j] → minimum product reaching (i,j)

------------------------------------------------

Step 2: Initialize base case
Start at (0,0)

------------------------------------------------

Step 3: First row and column
Only one path possible:
• first row → from left
• first column → from top

------------------------------------------------

Step 4: Transition

From:
• top (i-1, j)
• left (i, j-1)

We take:
    prev_max = max(top_max, left_max)
    prev_min = min(top_min, left_min)

If current value is NEGATIVE:
    max = prev_min * val
    min = prev_max * val

If POSITIVE:
    max = prev_max * val
    min = prev_min * val

------------------------------------------------

Step 5: Final answer

If max_dp[m-1][n-1] < 0 → return -1
Else → return modulo

------------------------------------------------

Key Insight:

Always track BOTH max and min due to sign flipping.
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        MOD = 10**9 + 7

        # DP tables
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]

        # base case
        max_dp[0][0] = min_dp[0][0] = grid[0][0]

        # first row
        for j in range(1, cols):
            max_dp[0][j] = min_dp[0][j] = (
                max_dp[0][j-1] * grid[0][j]
            )

        # first column
        for i in range(1, rows):
            max_dp[i][0] = min_dp[i][0] = (
                max_dp[i-1][0] * grid[i][0]
            )

        # fill DP
        for i in range(1, rows):
            for j in range(1, cols):

                val = grid[i][j]

                prev_max = max(
                    max_dp[i-1][j],
                    max_dp[i][j-1]
                )
                prev_min = min(
                    min_dp[i-1][j],
                    min_dp[i][j-1]
                )

                if val < 0:
                    max_dp[i][j] = prev_min * val
                    min_dp[i][j] = prev_max * val
                else:
                    max_dp[i][j] = prev_max * val
                    min_dp[i][j] = prev_min * val

        ans = max_dp[-1][-1]

        if ans < 0:
            return -1

        return ans % MOD


"""
Example

grid =
[
 [1,-2,1],
 [1,-2,1],
 [3,-4,1]
]

Best path:
1 → 1 → 3 → -4 → 1 = 12

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(m * n)

------------------------------------------------

Optimization:

Space can be reduced to O(n) using rolling arrays.

------------------------------------------------

Key Pattern:
Dynamic Programming with sign tracking
(max + min states)
"""
