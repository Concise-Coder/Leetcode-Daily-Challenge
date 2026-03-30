"""
LeetCode 2840
Check if Strings Can be Made Equal With Operations II

You are given two strings s1 and s2 of equal length.

Allowed Operation:
• Swap any two characters:
    - Both at EVEN indices
    OR
    - Both at ODD indices

Task:
Return True if s1 can be transformed into s2.

------------------------------------------------

Approach (Human Thinking):

Key Observation:

Indices are divided into 2 independent groups:
• Even indices → 0, 2, 4, ...
• Odd indices  → 1, 3, 5, ...

Within each group:
→ We can rearrange freely

------------------------------------------------

Step 1: Extract even indexed characters

s1[::2], s2[::2]

------------------------------------------------

Step 2: Extract odd indexed characters

s1[1::2], s2[1::2]

------------------------------------------------

Step 3: Compare frequency

If both even groups match AND both odd groups match:
→ return True

------------------------------------------------

Key Insight:

This is a multiset comparison problem under index constraints.

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

from collections import Counter


class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:

        # -------------------------
        # Even index characters
        # -------------------------
        even_s1 = Counter(s1[::2])
        even_s2 = Counter(s2[::2])

        # -------------------------
        # Odd index characters
        # -------------------------
        odd_s1 = Counter(s1[1::2])
        odd_s2 = Counter(s2[1::2])

        # -------------------------
        # Compare both groups
        # -------------------------
        return even_s1 == even_s2 and odd_s1 == odd_s2


"""
Example

s1 = "abcdba"
s2 = "cabdab"

Even indices:
s1 → a, c, b
s2 → c, b, a → match

Odd indices:
s1 → b, d, a
s2 → a, d, b → match

→ True

------------------------------------------------

Time Complexity:
O(n)

Space Complexity:
O(n)

------------------------------------------------

Key Pattern:

• Group-based rearrangement
• Frequency comparison (Counter)

------------------------------------------------

Important Insight:

If swaps are restricted to index parity,
→ treat even and odd indices as separate arrays
"""
