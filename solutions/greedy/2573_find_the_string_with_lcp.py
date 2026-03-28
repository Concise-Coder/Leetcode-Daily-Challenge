"""
LeetCode 2573
Find the String with LCP

You are given an LCP matrix where:
lcp[i][j] = length of longest common prefix of suffixes starting at i and j.

Task:
Construct the lexicographically smallest string that satisfies the LCP matrix.
If impossible → return "".

------------------------------------------------

Approach (Human Thinking):

Step 1: Greedy Construction

We assign characters from left to right.

Idea:
If lcp[i][j] > 0 → characters at i and j must be SAME.

So:
• Start assigning smallest character ('a', 'b', ...)
• For each i:
    assign same character to all j where lcp[i][j] > 0

------------------------------------------------

Step 2: Build string

Convert numeric labels → characters

------------------------------------------------

Step 3: Verification (VERY IMPORTANT)

We must verify correctness using DP:

If:
res[i] == res[j]
→ lcp[i][j] = 1 + lcp[i+1][j+1]

Else:
→ lcp[i][j] = 0

If mismatch → return ""

------------------------------------------------

Key Insight:

Construction alone is not enough.
Verification ensures correctness.

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:

        n = len(lcp)

        word = [0] * n
        c = 1  # 1 -> 'a', 2 -> 'b', ...

        # -------------------------
        # Step 1: Greedy assignment
        # -------------------------
        for i in range(n):

            if word[i] != 0:
                continue

            if c > 26:
                return ""

            for j in range(i, n):
                if lcp[i][j] > 0:
                    word[j] = c

            c += 1

        # -------------------------
        # Step 2: Build string
        # -------------------------
        res = "".join(chr(ord('a') + x - 1) for x in word)

        # -------------------------
        # Step 3: Verify using DP
        # -------------------------
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                expected = 0

                if res[i] == res[j]:
                    expected = 1 + (
                        lcp[i + 1][j + 1]
                        if i + 1 < n and j + 1 < n
                        else 0
                    )

                if lcp[i][j] != expected:
                    return ""

        return res


"""
Example

lcp =
[
 [3,0,1],
 [0,2,0],
 [1,0,1]
]

Output:
"aba"

------------------------------------------------

Time Complexity:
O(n^2)

Space Complexity:
O(n)

------------------------------------------------

Key Patterns:

• Greedy construction
• Matrix constraints
• DP verification

------------------------------------------------

Important Insight:

"Construct + Verify" is a powerful technique
for problems with strict constraints.
"""
