"""
LeetCode (Biweekly/Weekly Contest)
Minimum Absolute Difference in k x k Submatrix

You are given a 2D grid and an integer k.

For every k x k submatrix, compute:
• The minimum absolute difference between any two DISTINCT values

Return a matrix where:
ans[i][j] = result for submatrix starting at (i, j)

------------------------------------------------

Approach (Brute Force - Human Thinking):

Step 1: Iterate over all k x k submatrices
    Top-left corner (r, c)

Step 2: Collect all DISTINCT elements
    Use a set to avoid duplicates

Step 3: Edge case
    If only one unique value → answer = 0

Step 4: Sort values
    Minimum difference will be between adjacent elements

Step 5: Compute minimum difference

------------------------------------------------

Key Insight:

Sorting reduces:
O(n² comparisons) → O(n log n) + linear scan

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Brute Force Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        # result matrix
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for r in range(m - k + 1):
            for c in range(n - k + 1):

                # collect distinct values
                distinct_vals = set()

                for i in range(r, r + k):
                    for j in range(c, c + k):
                        distinct_vals.add(grid[i][j])

                # if only one value
                if len(distinct_vals) <= 1:
                    ans[r][c] = 0
                    continue

                # sort values
                sorted_vals = sorted(distinct_vals)

                # find minimum difference
                min_diff = float('inf')

                for i in range(1, len(sorted_vals)):
                    min_diff = min(
                        min_diff,
                        sorted_vals[i] - sorted_vals[i - 1]
                    )

                ans[r][c] = min_diff

        return ans


"""
Example

grid =
[
 [1,3,6],
 [7,2,9],
 [4,5,8]
]

k = 2

Submatrices:
[1,3;7,2] → values = {1,2,3,7} → min diff = 1
[3,6;2,9] → {2,3,6,9} → min diff = 1
...

------------------------------------------------

Time Complexity:
O((m*n*k²) + sort)

Worst case:
O(m * n * k² log k²)

------------------------------------------------

Space Complexity:
O(k²)

------------------------------------------------

Note:

This is a brute-force solution.
Can be optimized using:
• Sliding window
• Balanced BST / Sorted structure
• Frequency arrays (if constraints small)
"""
