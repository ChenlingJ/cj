import math
from typing import Iterable


class Complex:
    # initialize, self is an instance that has been constructed but not initialized
    # self is an empty Complex instance
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __neg__(self) -> "Complex":
        return Complex(-self.real, -self.imaginary)

    def __add__(self, other: "Complex") -> "Complex":
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other: "Complex") -> "Complex":
        return self + -other

    def __mul__(self, other: "Complex") -> "Complex":
        return Complex(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + self.imaginary * other.real,
        )

    def __truediv__(self, other: "Complex") -> "Complex":
        return self * other.recip()

    def mod(self) -> "Complex":
        return Complex(math.hypot(self.real, self.imaginary), 0.0)

    def conj(self) -> "Complex":
        return Complex(self.real, -self.imaginary)

    def recip(self) -> "Complex":
        denom = self.real ** 2 + self.imaginary ** 2
        return Complex(self.real / denom, -self.imaginary / denom)

    def __str__(self) -> str:
        return "{:.2f}{:+.2f}i".format(self.real, self.imaginary)


def solve(c: Iterable[float], d: Iterable[float]) -> str:
    x = Complex(*c)
    y = Complex(*d)
    return "\n".join(map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]))


if __name__ == "__main__":
    print(
        solve(
            map(float, input().split()),
            map(float, input().split()),
        )
    )
