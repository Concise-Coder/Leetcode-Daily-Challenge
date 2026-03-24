"""
LeetCode 2906
Construct Product Matrix

You are given a matrix grid.

For each cell (i, j), compute:
Product of ALL elements in the matrix EXCEPT grid[i][j]

Return the resulting matrix modulo 12345.

------------------------------------------------

Approach (Human Thinking):

Key Idea:
Instead of recomputing product for every cell (O(n²*m²)),
we use prefix and suffix product trick.

------------------------------------------------

Step 1: Flatten traversal (row-wise)

We simulate 1D traversal over matrix.

------------------------------------------------

Step 2: Prefix pass

For each cell:
    ans[i][j] = product of all elements BEFORE it

------------------------------------------------

Step 3: Suffix pass

Traverse from end:
    multiply ans[i][j] with product of all elements AFTER it

------------------------------------------------

Step 4: Combine

Final:
    ans[i][j] = prefix * suffix % MOD

------------------------------------------------

Key Insight:

This is extension of:
"Product of Array Except Self"

Applied to 2D matrix.

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def constructProductMatrix(
        self,
        grid: List[List[int]]
    ) -> List[List[int]]:

        n, m = len(grid), len(grid[0])
        MOD = 12345

        # result matrix
        ans = [[0] * m for _ in range(n)]

        # -------------------------
        # Prefix pass
        # -------------------------
        pref = 1

        for i in range(n):
            for j in range(m):

                ans[i][j] = pref
                pref = (pref * grid[i][j]) % MOD

        # -------------------------
        # Suffix pass
        # -------------------------
        suff = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                ans[i][j] = (ans[i][j] * suff) % MOD
                suff = (suff * grid[i][j]) % MOD

        return ans


"""
Example

grid =
[
 [1,2],
 [3,4]
]

Total product = 24

Output:
[
 [24/1, 24/2],
 [24/3, 24/4]
]
=
[
 [24,12],
 [8,6]
] % 12345

------------------------------------------------

Time Complexity:
O(n * m)

Space Complexity:
O(1) extra (excluding output)

------------------------------------------------

Key Pattern:

Prefix + Suffix Product Trick

------------------------------------------------

Related:
• Product of Array Except Self (1D version)
"""
