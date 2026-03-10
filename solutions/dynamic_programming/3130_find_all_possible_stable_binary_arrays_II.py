"""
LeetCode 3130
Find All Possible Stable Binary Arrays II

A binary array is called stable if it does not contain more than 'limit'
consecutive 0s or 1s.

Given:
zero  -> number of zeros
one   -> number of ones
limit -> maximum allowed consecutive identical bits

Return the number of possible stable arrays.

The answer should be returned modulo 1e9 + 7.
"""

MOD = 10**9 + 7


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:

        # dp0[i][j] -> arrays ending with 0
        # dp1[i][j] -> arrays ending with 1

        dp0 = [[0]*(one+1) for _ in range(zero+1)]
        dp1 = [[0]*(one+1) for _ in range(zero+1)]

        dp0[1][0] = 1
        dp1[0][1] = 1

        for z in range(zero+1):
            for o in range(one+1):

                # ending with 0
                if z > 0:
                    for k in range(1, limit+1):
                        if z-k >= 0:
                            dp0[z][o] = (dp0[z][o] + dp1[z-k][o]) % MOD
                        else:
                            break

                # ending with 1
                if o > 0:
                    for k in range(1, limit+1):
                        if o-k >= 0:
                            dp1[z][o] = (dp1[z][o] + dp0[z][o-k]) % MOD
                        else:
                            break

        return (dp0[zero][one] + dp1[zero][one]) % MOD


"""
Approach

Dynamic Programming.

Two DP states are maintained:

dp0[z][o] -> number of valid arrays with z zeros and o ones
             ending with 0

dp1[z][o] -> number of valid arrays with z zeros and o ones
             ending with 1

Transition:

To end with 0:
    append up to 'limit' zeros after a sequence ending with 1

To end with 1:
    append up to 'limit' ones after a sequence ending with 0

This guarantees that no segment exceeds the allowed limit.

Time Complexity:
O(zero * one * limit)

Space Complexity:
O(zero * one)
"""
