import math
from cmath import sqrt as csqrt

def solve_quadratic(a, b, c):
    if a == 0.0:
        if b == 0.0:
            if c == 0.0:
                return "Infinite solutions."
            return "No solution."
        return f"Linear root: {-c / b:.4f}"

    d = b*b - 4*a*c
    if d > 0:
        r1 = (-b + math.sqrt(d)) / (2*a)
        r2 = (-b - math.sqrt(d)) / (2*a)
        return f"Two real roots: {r1:.4f} and {r2:.4f}"

    if d == 0:
        r = -b / (2*a)
        return f"One real root: {r:.4f}"

    r1 = (-b + csqrt(d)) / (2*a)
    r2 = (-b - csqrt(d)) / (2*a)
    return (
        f"Complex roots: {r1.real:.4f} {'+' if r1.imag >= 0 else '-'} {abs(r1.imag):.4f}i "
        f"and {r2.real:.4f} {'+' if r2.imag >= 0 else '-'} {abs(r2.imag):.4f}i"
    )

def main():
    a, b, c = 1, -5, 6   # Example coefficients
    print(f"Solving: {a}x^2 + ({b})x + ({c}) = 0")
    print(solve_quadratic(a, b, c))

if __name__ == "__main__":
    main()
