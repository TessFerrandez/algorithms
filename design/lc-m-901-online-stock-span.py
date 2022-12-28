class StockSpanner:
    def __init__(self):
        self.spans = []

    def next(self, price: int) -> int:
        span = 1
        while self.spans and self.spans[-1][0] <= price:
            _, old_span = self.spans.pop()
            span += old_span
        self.spans.append((price, span))
        return span


spanner = StockSpanner()
assert spanner.next(100) == 1
assert spanner.next(80) == 1
assert spanner.next(60) == 1
assert spanner.next(70) == 2
assert spanner.next(60) == 1
assert spanner.next(75) == 4
assert spanner.next(85) == 6
