class Solution:
    def numberOfWays(self, corridor: str) -> int:
        nchairs = 0
        last_chair = -1

        pots = []

        for pos, item in enumerate(corridor):
            if item == "S":
                if nchairs == 0:
                    if last_chair != -1:
                        pots.append(pos - last_chair)
                    nchairs += 1
                elif nchairs == 1:
                    nchairs = 0
                    last_chair = pos

        if nchairs != 0 or last_chair == -1:
            return 0
        if not pots:
            return 1

        total = 1
        for p in pots:
            total *= p
        return total % (10 ** 9 + 7)


solution = Solution()
assert solution.numberOfWays("PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS") == 919999993
assert solution.numberOfWays("SSPPSPS") == 3
assert solution.numberOfWays("PPSPSP") == 1
assert solution.numberOfWays("S") == 0
assert solution.numberOfWays("P") == 0
