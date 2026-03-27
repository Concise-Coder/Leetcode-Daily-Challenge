"""
LeetCode (Matrix Row Rotation Check)
Check if Matrix Rows are Similar After k Shifts

You are given a matrix mat and an integer k.

Task:
Check if shifting every row to the right by k positions
results in the SAME matrix.

------------------------------------------------

Approach (Human Thinking):

Step 1: Understand rotation
Shifting right by k means:
    new[j] = old[(j + k) % n]

So for matrix to remain same:
    mat[i][j] == mat[i][(j + k) % n]

------------------------------------------------

Step 2: Check condition

For every row:
    For every column j:
        if mismatch → return False

------------------------------------------------

Step 3: If all match → return True

------------------------------------------------

Key Insight:

Instead of actually rotating,
we simulate using modulo indexing.

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:

        n = len(mat[0])

        for row in mat:
            for j in range(n):

                if row[j] != row[(j + k) % n]:
                    return False

        return True


"""
Example

mat =
[
 [1,2,1,2]
]

k = 2

Shifted row:
[1,2,1,2] → same

→ True

------------------------------------------------

Time Complexity:
O(m * n)

Space Complexity:
O(1)

------------------------------------------------

Key Pattern:

Cyclic rotation using modulo

------------------------------------------------

Note:

No need to actually rotate the array.
"""
