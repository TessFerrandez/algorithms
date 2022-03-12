from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 5 == 0:
                result.append('Buzz')
            elif i % 3 == 0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result


solution = Solution()
assert solution.fizzBuzz(3) == ["1","2","Fizz"]
assert solution.fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
assert solution.fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
