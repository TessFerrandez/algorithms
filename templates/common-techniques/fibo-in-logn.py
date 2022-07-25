MOD = 1000000007

def fib(n):
    a = [[1, 1], [1, 0]]
    x = [[0, 0], [0, 0]]

    def multiply(a, b):
        c = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    c[i][k] = (c[i][k] + ((a[i][j] % MOD) * (b[j][k] % MOD)) % MOD) % MOD

        x[0][0] = c[0][0]
        x[0][1] = c[0][1]
        x[1][0] = c[1][0]
        x[1][1] = c[1][1]

    def helper(n):
        if n == 0:
            x[0][0] = 1
            x[0][1] = 0
            x[1][0] = 0
            x[1][1] = 1
            return

        helper(n // 2)
        multiply(x, x)
        if n & 1:
            multiply(x, a)

    if n == 0:
        return 0

    helper(n - 1)
    return x[0][0]


assert fib(1) == 1
assert fib(2) == 1
assert fib(3) == 2
assert fib(4) == 3
assert fib(5) == 5
assert fib(6) == 8
