"""
LeetCode (Maximum Amount with Limited Negative Skips)

You are given a grid `coins` where:
• You start at (0,0)
• You can move only RIGHT or DOWN
• Each cell adds its value to your total

Special Rule:
You are allowed to skip (ignore) up to 2 negative values.

Task:
Return the maximum amount you can collect.

------------------------------------------------

Approach (Human Thinking):

Key Idea:
This is a DP problem with an extra dimension:
→ number of skips used

------------------------------------------------

State Definition:

dp[c][k] =
Maximum amount reaching column c
using exactly k skips (k = 0,1,2)

We process row by row.

------------------------------------------------

Transitions:

1. Normal move:
Take value → dp + val

2. Skip negative:
If val < 0:
    we can skip it (do not add it)
    and increase skip count

------------------------------------------------

We take best from:
• top (previous row)
• left (same row, previous column)

------------------------------------------------

Key Insight:

This is:
Grid DP + Limited resource usage (k = 2 skips)

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:

        ROWS, COLS = len(coins), len(coins[0])

        # dp[c][k] → max value at column c using k skips
        dp = [[float('-inf')] * 3 for _ in range(COLS)]

        for r in range(ROWS):
            for c in range(COLS):

                val = coins[r][c]

                # -------------------------
                # Base case
                # -------------------------
                if r == 0 and c == 0:
                    dp[c][0] = val
                    dp[c][1] = 0 if val < 0 else float('-inf')
                    dp[c][2] = float('-inf')
                    continue

                new_dp = [float('-inf')] * 3

                # -------------------------
                # Case 1: Take value
                # -------------------------
                for k in range(3):

                    best_in = float('-inf')

                    if r > 0:
                        best_in = max(best_in, dp[c][k])

                    if c > 0:
                        best_in = max(best_in, dp[c - 1][k])

                    if best_in != float('-inf'):
                        new_dp[k] = best_in + val

                # -------------------------
                # Case 2: Skip negative
                # -------------------------
                if val < 0:
                    for k in range(1, 3):

                        best_in_prev = float('-inf')

                        if r > 0:
                            best_in_prev = max(best_in_prev, dp[c][k - 1])

                        if c > 0:
                            best_in_prev = max(best_in_prev, dp[c - 1][k - 1])

                        if best_in_prev != float('-inf'):
                            new_dp[k] = max(new_dp[k], best_in_prev)

                dp[c] = new_dp

        return max(dp[COLS - 1])


"""
Example

coins =
[
 [1, -2, 3],
 [4, -5, 6]
]

We can skip up to 2 negatives:
→ choose optimal path using skips

------------------------------------------------

Time Complexity:
O(m * n * 3)

Space Complexity:
O(n * 3)

------------------------------------------------

Key Patterns:

• Grid DP
• State expansion (k dimension)
• Resource-constrained optimization

------------------------------------------------

Important Insight:

Whenever problem says:
"at most K operations"
→ Add dimension to DP
"""
