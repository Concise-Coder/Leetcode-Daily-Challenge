"""
LeetCode 3070
Count Submatrices with Top-Left Element and Sum Less Than k

You are given a matrix grid and an integer k.

A submatrix is valid if:
• It starts at (0, 0) (top-left corner)
• Its sum is ≤ k

Return the number of such submatrices.

------------------------------------------------

Approach (Human Thinking):

Step 1: Fix the top-left corner
All submatrices must start from (0,0).
So each submatrix is defined by choosing a bottom-right corner (i, j).

So the problem reduces to:
For every (i, j), compute sum of rectangle (0,0) → (i,j)

------------------------------------------------

Step 2: Use Prefix Sum

We build a prefix sum matrix where:

prefix[i][j] = sum of all elements from (0,0) to (i,j)

Transition:

prefix[i][j] =
    grid[i][j]
    + prefix[i-1][j]
    + prefix[i][j-1]
    - prefix[i-1][j-1]

------------------------------------------------

Step 3: Count valid submatrices

For each (i, j):
    if prefix[i][j] ≤ k → count it

------------------------------------------------

Key Insight:

Since all submatrices start from (0,0),
we don't need complex submatrix enumeration.

Each cell itself represents one submatrix.

------------------------------------------------
"""


# ------------------------------------------------
# Human Thinking Solution
# ------------------------------------------------

from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])

        prefix = [[0]*n for _ in range(m)]
        count = 0

        for i in range(m):
            for j in range(n):

                prefix[i][j] = grid[i][j]

                if i > 0:
                    prefix[i][j] += prefix[i-1][j]

                if j > 0:
                    prefix[i][j] += prefix[i][j-1]

                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i-1][j-1]

                if prefix[i][j] <= k:
                    count += 1

        return count


"""
Example

grid =
[
 [7,6,3],
 [6,6,1]
]

k = 18

Prefix matrix:
[7,13,16]
[13,25,29]

Valid cells (≤ 18):
7, 13, 16, 13 → total = 4

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(m * n)
"""
