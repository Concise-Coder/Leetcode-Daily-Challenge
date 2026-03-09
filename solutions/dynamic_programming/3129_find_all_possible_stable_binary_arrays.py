"""
LeetCode 3129
Find All Possible Stable Binary Arrays I

A binary array is called stable if it does not contain more than 'limit'
consecutive 0s or 1s.

Given:
zero  -> number of zeros
one   -> number of ones
limit -> maximum allowed consecutive identical bits

Return the number of stable arrays that can be formed.

Note:
I was able to solve this problem independently.
"""


from functools import lru_cache

MOD = 10**9 + 7


# ------------------------------------------------
# User Achievement
# ------------------------------------------------
"""
This problem was solved by me independently.
The logic involves counting valid binary arrays while
respecting the constraint on consecutive 0s and 1s.
"""


# ------------------------------------------------
# Optimized Dynamic Programming Solution
# ------------------------------------------------

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        @lru_cache(None)
        def dp(z, o, last, count):
            """
            z -> remaining zeros
            o -> remaining ones
            last -> last placed element (0 or 1)
            count -> current consecutive count
            """

            if z == 0 and o == 0:
                return 1

            ans = 0

            # place 0
            if z > 0:
                if last == 0:
                    if count < limit:
                        ans += dp(z-1, o, 0, count+1)
                else:
                    ans += dp(z-1, o, 0, 1)

            # place 1
            if o > 0:
                if last == 1:
                    if count < limit:
                        ans += dp(z, o-1, 1, count+1)
                else:
                    ans += dp(z, o-1, 1, 1)

            return ans % MOD

        ans = 0

        if zero > 0:
            ans += dp(zero-1, one, 0, 1)

        if one > 0:
            ans += dp(zero, one-1, 1, 1)

        return ans % MOD


"""
Approach

This is solved using Dynamic Programming with memoization.

State:
dp(z, o, last, count)

z      -> remaining zeros
o      -> remaining ones
last   -> last placed bit
count  -> number of consecutive identical bits

Transitions:
• Add 0 if zeros remain and consecutive limit allows.
• Add 1 if ones remain and consecutive limit allows.

Memoization ensures each state is computed once.

Time Complexity:
O(zero * one * limit)

Space Complexity:
O(zero * one * limit)
"""
