"""
LeetCode 3212
Count Submatrices With Equal Frequency of X and Y

You are given a grid containing:
'X', 'Y', and '.'

A submatrix is valid if:
• It has equal number of 'X' and 'Y'
• It contains at least one 'X'

------------------------------------------------

Approach (Your Idea - Top Left Fixed Optimization):

Observation:
We only consider submatrices starting from (0, 0).

We maintain prefix counts for each column:
• ps_x[c] → total X count from (0,0) to (r,c)
• ps_y[c] → total Y count from (0,0) to (r,c)

For each row:
    we accumulate counts horizontally
    then update column prefix sums

At each cell (r, c):
    if:
        ps_x[c] > 0   (at least one X)
        AND
        ps_x[c] == ps_y[c]
    then:
        valid submatrix found

------------------------------------------------

Key Insight:

Instead of checking all submatrices,
we reduce the problem to checking only
prefix rectangles from (0,0).

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        # prefix sums for columns
        ps_x = [0] * cols
        ps_y = [0] * cols

        ans = 0

        for r in range(rows):

            curr_x = 0
            curr_y = 0

            for c in range(cols):

                # update row-wise counts
                if grid[r][c] == 'X':
                    curr_x += 1
                elif grid[r][c] == 'Y':
                    curr_y += 1

                # update column prefix
                ps_x[c] += curr_x
                ps_y[c] += curr_y

                # check condition
                if ps_x[c] > 0 and ps_x[c] == ps_y[c]:
                    ans += 1

        return ans


"""
Example

grid =
[
 ['X','Y','.'],
 ['Y','.','.']
]

We track prefix counts for X and Y.

At each cell (r, c), we check:
• Equal count of X and Y
• At least one X

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(n)

------------------------------------------------

Note:

This solution works ONLY for submatrices
starting from (0,0).

For full problem (any submatrix),
we need 2D prefix + hashmap approach.
"""
