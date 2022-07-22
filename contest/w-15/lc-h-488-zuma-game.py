from collections import deque


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def play_board(board, i):
            ''' Remove any 3+ continuous balls on board'''
            if i < 0:
                return board

            left = right = i
            while left > 0 and board[left - 1] == board[i]:
                left -= 1

            while right + 1 < len(board) and board[right + 1] == board[i]:
                right += 1

            continuous = right - left + 1
            if continuous >= 3:
                new_board = board[:left] + board[right + 1:]
                return play_board(new_board, left - 1)
            else:
                return board

        hand = "".join(sorted(hand))

        todo = deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while todo:
            current_board, current_hand, step = todo.popleft()

            for i in range(len(current_board) + 1):
                for j in range(len(current_hand)):

                    # skip any duplicate balls (same color)
                    if j > 0 and current_hand[j] == current_hand[j - 1]:
                        continue

                    # only insert at the start of a continuous set of balls
                    # [R]RR is the same as R[R]R and RR[R]
                    if i > 0 and current_board[i - 1] == current_hand[j]:
                        continue

                    pick = False

                    # pick the ball from hand[j] and place it at board[i] IF
                    # the balls [i] and [j] match
                    if i < len(current_board) and current_board[i] == current_hand[j]:
                        pick = True

                    # [i - 1] and [i] are the same but [j] is different
                    if 0 < i < len(current_board) and current_board[i - 1] == current_board[i] and current_board[i] != current_hand[j]:
                        pick = True

                    if pick:
                        new_board = play_board(current_board[:i] + current_hand[j] + current_board[i:], i)
                        new_hand = current_hand[:j] + current_hand[j + 1:]

                        if new_board == '':
                            return step + 1

                        if (new_board, new_hand) not in visited:
                            todo.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))

        return -1


solution = Solution()
assert solution.findMinStep('WRRBBW', 'RB') == -1
assert solution.findMinStep('WWRRBBWW', 'WRBRW') == 2
assert solution.findMinStep('G', 'GGGGG') == 2
