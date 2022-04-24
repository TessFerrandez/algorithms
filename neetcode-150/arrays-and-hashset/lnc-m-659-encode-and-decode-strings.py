class Solution:
    def encode(self, strs):
        estrs = [s.replace(':', '::') for s in strs]
        return ':;'.join(estrs)

    def decode(self, str):
        # write your code here
        return [s.replace('::', ':') for s in str.split(':;')]


solution = Solution()

original = ["we", "say", ":", "yes"]
encoded = solution.encode(original)
assert solution.decode(encoded) == original

original = ["lint","code","love","you"]
encoded = solution.encode(original)
assert solution.decode(encoded) == original
