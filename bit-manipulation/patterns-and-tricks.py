def basics(a, b):
    print(f"{a} = {bin(a)[2:]}, {b} = {bin(b)[2:]}")
    print(f"SET UNION:\t", a | b, bin(a | b)[2:])
    print(f"SET INTERSECT:\t", a & b, bin(a & b)[2:])
    print(f"SET SUBTRACT:\t", a & ~b, bin(a & ~b)[2:])
    print(f"SET NEGATE:\t", ~a, bin(~a))


basics(11, 6)
