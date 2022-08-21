class MyCalendar:
    def __init__(self):
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.bookings:
            if s < end and start < e:
                return False
        self.bookings.append((start, end))
        return True


cal = MyCalendar()
assert cal.book(10, 20)
assert not cal.book(15, 25)
assert cal.book(20, 30)
