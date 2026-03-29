"""
LeetCode 2839
Check if Strings Can be Made Equal With Operations I

You are given two strings s1 and s2 of length 4.

Allowed Operation:
• Swap characters at indices:
    (0 ↔ 2)  → even positions
    (1 ↔ 3)  → odd positions

Task:
Return True if s1 can be transformed into s2 using any number of operations.

------------------------------------------------

Approach (Human Thinking):

Key Observation:

Indices are divided into 2 independent groups:
• Even indices → [0, 2]
• Odd indices  → [1, 3]

We can rearrange within each group freely.

------------------------------------------------

Step 1: Check even positions

Possible matches:
• s1[0] == s2[0] AND s1[2] == s2[2]
OR
• s1[0] == s2[2] AND s1[2] == s2[0]

------------------------------------------------

Step 2: Check odd positions

Possible matches:
• s1[1] == s2[1] AND s1[3] == s2[3]
OR
• s1[1] == s2[3] AND s1[3] == s2[1]

------------------------------------------------

Step 3: Both must match

------------------------------------------------

Key Insight:

Independent permutation groups

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        # -------------------------
        # Check even indices (0, 2)
        # -------------------------
        can_match_evens = (
            (s1[0] == s2[0] and s1[2] == s2[2]) or
            (s1[0] == s2[2] and s1[2] == s2[0])
        )

        # -------------------------
        # Check odd indices (1, 3)
        # -------------------------
        can_match_odds = (
            (s1[1] == s2[1] and s1[3] == s2[3]) or
            (s1[1] == s2[3] and s1[3] == s2[1])
        )

        return can_match_evens and can_match_odds


"""
Example

s1 = "abcd"
s2 = "cdab"

Even indices:
[a, c] ↔ [c, a] → possible

Odd indices:
[b, d] ↔ [d, b] → possible

→ True

------------------------------------------------

Time Complexity:
O(1)

Space Complexity:
O(1)

------------------------------------------------

Key Pattern:

Group-based swapping / independent positions

------------------------------------------------

Optimization Insight:

Equivalent simpler idea:
sort(s1[0], s1[2]) == sort(s2[0], s2[2])
AND
sort(s1[1], s1[3]) == sort(s2[1], s2[3])
"""
