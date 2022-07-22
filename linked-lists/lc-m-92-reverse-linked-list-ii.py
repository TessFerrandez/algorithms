from ListNode import ListNode, ll_from_array, array_from_ll


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int):
        if not head:
            return None

        left, right = head, head
        stop = False

        def recurse_and_reverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurse_and_reverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurse_and_reverse(right, m, n)
        return head


solution = Solution()
print(array_from_ll(solution.reverseBetween(ll_from_array([1, 2, 3, 4, 5]), 2, 4)))
print(array_from_ll(solution.reverseBetween(ll_from_array([5]), 1, 1)))
