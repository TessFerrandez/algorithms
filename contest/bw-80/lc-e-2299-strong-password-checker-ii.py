class Solution:
    # my solution
    def strongPasswordCheckerII1(self, password: str) -> bool:
        def has_upper(password):
            for ch in password:
                if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                    return True
            return False

        def has_lower(password):
            for ch in password:
                if ch in "abcdefghijklmnopqrstuvwxyz":
                    return True
            return False

        def has_digit(password):
            for ch in password:
                if ch in "0123456789":
                    return True
            return False

        def has_special(password):
            for ch in password:
                if ch in "!@#$%^&*()-+":
                    return True
            return False

        def has_double(password):
            for i in range(len(password) - 1):
                if password[i] == password[i + 1]:
                    return True
            return False

        if len(password) < 8:
            return False
        if not has_upper(password):
            return False
        if not has_lower(password):
            return False
        if not has_digit(password):
            return False
        if not has_special(password):
            return False
        if has_double(password):
            return False
        return True

    # cleaner
    def strongPasswordCheckerII(self, password: str) -> bool:
        seen = set()

        for i, ch in enumerate(password):
            if i > 0 and ch == password[i - 1]:
                return False
            if ch in '!@#$%^&*()-+':
                seen.add('special')
            elif ch.isupper():
                seen.add('upper')
            elif ch.islower():
                seen.add('lower')
            elif ch.isnumeric():
                seen.add('numeric')

        return len(password) > 7 and len(seen) == 4


solution = Solution()
assert not solution.strongPasswordCheckerII("aab1!A")
assert solution.strongPasswordCheckerII("IloveLe3tcode!")
assert not solution.strongPasswordCheckerII("Me+You--IsMyDream")
assert not solution.strongPasswordCheckerII("1aB!")
