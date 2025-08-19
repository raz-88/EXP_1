import math

with open("input_multiple.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        a, b, c = map(float, line.strip().split())
        D = b**2 - 4*a*c

        print(f"\nSet {line_num} (a={a}, b={b}, c={c}):")
        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            print(f"  Two real roots: {x1}, {x2}")
        elif D == 0:
            x = -b / (2*a)
            print(f"  One real root: {x}")
        else:
            print("  No real roots")
