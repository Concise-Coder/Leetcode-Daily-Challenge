"""
LeetCode (Lexicographically Smallest String Construction with Constraints)

You are given:
• str1 → pattern of 'T' and 'F'
• str2 → target substring

Goal:
Construct the lexicographically smallest string `ans` such that:

For every index i:
• If str1[i] == 'T' → substring starting at i MUST equal str2
• If str1[i] == 'F' → substring starting at i MUST NOT equal str2

If impossible → return ""

------------------------------------------------

Approach (Human Thinking):

Step 1: Initialize answer with '?'

Length = n + m - 1

------------------------------------------------

Step 2: Enforce 'T' constraints

For each i where str1[i] == 'T':
    force ans[i + j] = str2[j]

If conflict occurs → return ""

------------------------------------------------

Step 3: Prepare tracking for 'F'

For each i where str1[i] == 'F':
• Count how many '?' positions exist
• Count mismatches already present

If:
    no '?' AND no mismatch → invalid → return ""

------------------------------------------------

Step 4: Fill remaining '?' greedily

For each '?':
• Try smallest possible character ('a' → 'z')
• Avoid choices that would violate an 'F' constraint

We maintain:
• forbidden characters list
• update counts dynamically

------------------------------------------------

Step 5: Return result

------------------------------------------------

Key Insight:

This is:
• Greedy construction
• Constraint satisfaction
• Sliding window reasoning

------------------------------------------------
"""


# ------------------------------------------------
# User Solution (Clean Version)
# ------------------------------------------------

class Solution:
    def lexicographicallySmallest(self, str1: str, str2: str) -> str:

        n, m = len(str1), len(str2)
        length = n + m - 1

        ans = ['?'] * length

        # -------------------------
        # Step 1: Apply 'T' constraints
        # -------------------------
        for i in range(n):

            if str1[i] == 'T':

                for j in range(m):

                    if ans[i + j] == '?':
                        ans[i + j] = str2[j]

                    elif ans[i + j] != str2[j]:
                        return ""

        # -------------------------
        # Step 2: Track 'F' constraints
        # -------------------------
        q_count = [0] * n
        mismatch_count = [0] * n

        for i in range(n):

            if str1[i] == 'F':

                for j in range(m):

                    if ans[i + j] == '?':
                        q_count[i] += 1

                    elif ans[i + j] != str2[j]:
                        mismatch_count[i] += 1

                if q_count[i] == 0 and mismatch_count[i] == 0:
                    return ""

        # -------------------------
        # Step 3: Fill remaining '?'
        # -------------------------
        for k in range(length):

            if ans[k] == '?':

                forbidden = [False] * 26

                start_i = max(0, k - m + 1)
                end_i = min(n - 1, k)

                for i in range(start_i, end_i + 1):

                    if str1[i] == 'F':

                        if q_count[i] == 1 and mismatch_count[i] == 0:
                            forbidden[ord(str2[k - i]) - ord('a')] = True

                chosen = '?'

                for c in range(26):
                    if not forbidden[c]:
                        chosen = chr(ord('a') + c)
                        break

                if chosen == '?':
                    return ""

                ans[k] = chosen

                # update tracking
                for i in range(start_i, end_i + 1):

                    if str1[i] == 'F':

                        q_count[i] -= 1

                        if chosen != str2[k - i]:
                            mismatch_count[i] += 1

        return "".join(ans)


"""
Example (Conceptual)

str1 = "TFT"
str2 = "ab"

We enforce:
• index 0 → "ab"
• index 2 → "ab"

Fill remaining positions while ensuring 'F' condition is respected.

------------------------------------------------

Time Complexity:
O(n * m)

Space Complexity:
O(n)

------------------------------------------------

Key Patterns:

• Greedy + Constraints
• Sliding window validation
• Character restriction (forbidden set)

------------------------------------------------

Important Insight:

"Fill '?' with smallest valid choice"
→ Classic lexicographically smallest construction
"""
