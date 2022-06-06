class Solution:
    def totalNQueens(self, n: int) -> int:
        def get_candidates(state, n):
            if not state:
                return range(n)

            current_row = len(state)
            candidates = set(range(n))

            for row, col in enumerate(state):
                candidates.discard(col)     # candidate and q in same col

                # discard diagonals
                distance = current_row - row
                candidates.discard(col + distance)
                candidates.discard(col - distance)

            return candidates

        def is_valid_state(state, n):
            return len(state) == n

        def search(state, solutions, n):
            if is_valid_state(state, n):
                solutions.append(state.copy())
                return

            for candidate in get_candidates(state, n):
                state.append(candidate)
                search(state, solutions, n)
                state.pop()

        state, solutions = [], []
        search(state, solutions, n)
        return len(solutions)


solution = Solution()
assert solution.totalNQueens(4) == 2
assert solution.totalNQueens(1) == 1
