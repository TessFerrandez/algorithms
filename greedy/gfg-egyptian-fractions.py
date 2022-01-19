'''
Represent a fraction as a sum of 1/n+1/m...

Ex. 2/3 = 1/2 + 1/6

Greedy algo

1. Find ceil(3/2) = 2 => 1/2
2. Calculate rest = 2/3 - 1/2 = 4/6 - 3/6 = 1/6
3. GOTO #1
'''
def print_egyptian(nr: int, dr: int):
    # if numerator or denominator is 0
    if dr == 0 or nr == 0:
        return

    # if numerator divides denominator
    # then we have a simple divisior
    if dr % nr == 0:
        print(f"1/{dr // nr}", end="")
        return

    # if denominator divides numerator,
    # the gien number is not a fraction
    if nr % dr == 0:
        print(nr // dr, end="")
        return

    # if numerator is more than denominator
    if nr > dr:
        print(nr // dr, "+ ", end="")
        print_egyptian(nr % dr, dr)
        return

    # dr > nr and dr % nr is non-zero
    # find ceiling of dr / nr and print it as first fraction
    n = dr // nr + 1
    print(f"1/{n} + ", end="")
    print_egyptian(nr * n - dr, dr * n)


nr = 6
dr = 14

print(f"{nr}/{dr} = ", end="")
print_egyptian(nr, dr)
