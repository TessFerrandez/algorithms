from collections import defaultdict
from typing import List


# My TLE solution
class BookMyShow1:
    def __init__(self, n: int, m: int):
        self.lowest_seat = defaultdict(int)
        self.lowest_row = 0
        self.n = n
        self.m = m
        self.total_left = m * n

    def gather(self, k: int, maxRow: int) -> List[int]:
        if self.total_left < k:
            return []

        if self.lowest_row > maxRow:
            return []

        row = self.lowest_row
        booking = []

        while row <= maxRow:
            if self.m - self.lowest_seat[row] >= k:
                booking = [row, self.lowest_seat[row]]
                self.lowest_seat[row] += k
                self.total_left -= k
                break
            row += 1

        while self.lowest_seat[self.lowest_row] == self.m:
            self.lowest_row += 1

        return booking

    def can_scatter(self, k, maxRow):
        # check if we can scatter
        total_free = 0

        row = self.lowest_row
        while row <= maxRow:
            total_free += self.m - self.lowest_seat[row]
            if total_free >= k:
                return True
            row += 1
        return False

    def scatter(self, k: int, maxRow: int) -> bool:
        if self.total_left < k:
            return False

        if not self.can_scatter(k, maxRow):
            return False

        total_left = k
        while total_left > 0:
            row_left = self.m - self.lowest_seat[self.lowest_row]
            if row_left > total_left:
                self.lowest_seat[self.lowest_row] += total_left
                total_left = 0
            else:
                self.lowest_seat[self.lowest_row] = self.m
                total_left -= row_left
                self.lowest_row += 1

        self.total_left -= k
        return True


class SegmentTree:
    def __init__(self, left, right):
        self.val = 0
        self.mid = (left + right) // 2
        self.left = left
        self.right = right
        self.left_tree, self.right_tree = None, None
        self.max = 0
        self.sums = 0
        if left != right:
            self.left_tree = SegmentTree(left, self.mid)
            self.right_tree = SegmentTree(self.mid + 1, right)

    def update(self, left, right, val=1):
        if self.left >= left and self.right <= right:
            self.val += val
            self.max += val
            self.sums += val * (right - left + 1)
            return
        if self.left > right or self.right < left:
            return

        self.left_tree.update(left, right, val)
        self.right_tree.update(left, right, val)
        self.max = self.val + max(self.left_tree.max, self.right_tree.max)
        self.sums = self.val * (self.right - self.left + 1) + self.left_tree.sums + self.right_tree.sums

    def query(self, i):
        if self.left == self.right and self.left == i:
            return self.val
        if i < self.left or i > self.right:
            return 0
        if i <= self.mid:
            return self.val + self.left_tree.query(i)
        return self.val + self.right_tree.query(i)

    def querySum(self, left, right):
        # return sum value in range [left, right]
        if self.left >= left and self.right <= right:
            return self.sums
        if self.left > right or self.right < left:
            return 0
        return self.val * (min(right, self.right) - max(left,self.left) + 1) + self.left_tree.querySum(left, right) + self.right_tree.querySum(left, right)

    def queryLowestGreater(self, value):
        # return the smallest row with at least 'value' remaining seats
        if self.max < value:
            return -1
        if self.left == self.right:
            return -1 if self.max < value else self.left
        if self.left_tree.max >= value - self.val:
            return self.left_tree.queryLowestGreater(value - self.val)
        return self.right_tree.queryLowestGreater(value - self.val)


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.st = SegmentTree(0, n - 1)
        self.st.update(0, n - 1, m)
        self.seats_per_row = m
        self.last_good_row = 0
        self.rows = n

    def gather(self, requested: int, max_row: int):
        row = self.st.queryLowestGreater(requested)
        if row < 0 or row > max_row:
            return []
        seats = self.st.query(row)
        self.st.update(row, row, -requested)
        return [row, self.seats_per_row - seats]

    def scatter(self, requested: int, max_row: int):
        # if sum 0 - max_row greater than requested
        # it's possible to book
        if self.st.querySum(0,max_row) < requested:
            return False

        # book seats from lowest row
        while self.last_good_row < self.rows and requested > 0:
            seats = self.st.query(self.last_good_row)
            self.st.update(self.last_good_row, self.last_good_row, -min(seats, requested))
            if seats > requested:
                break
            else:
                requested -= seats
                self.last_good_row += 1
        return True


book = BookMyShow(2, 5)
assert book.gather(4, 0) == [0, 0]
assert book.gather(2, 0) == []
assert book.scatter(5, 1)
assert not book.scatter(5, 1)

book = BookMyShow(2, 8)
assert book.scatter(3, 0)
assert book.gather(8, 0) == []

book = BookMyShow(18, 48)
assert book.scatter(24, 13)
assert book.scatter(12, 5)
assert book.gather(12, 5) == [0, 36]
assert book.scatter(3, 12)
assert book.gather(36, 13) == [1, 3]
assert book.scatter(25, 6)
assert book.scatter(32, 14)
assert book.gather(29, 6) == [3, 0]
assert book.gather(3, 11) == [3, 29]
assert not book.scatter(30, 0)
assert book.gather(45, 15) == [4, 0]
assert book.gather(23, 17) == [5, 0]
assert book.gather(23, 2) == []
assert book.scatter(41, 10)
assert book.scatter(40, 6)
