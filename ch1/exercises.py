def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        assert(isinstance(top, int))
        assert(isinstance(bottom, int))
        g = gcd(top, bottom)
        self.num = top // g
        self.den = bottom // g

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        if isinstance(other_fraction, Fraction):
            new_num = self.num * other_fraction.den \
                + self.den * other_fraction.num
            new_den = self.den * other_fraction.den
            return Fraction(new_num, new_den)
        else:
            return Fraction(int(other_fraction * 1000000000),
                            1000000000) + self

    def __mul__(self, other_fraction):
        new_den = self.den * other_fraction.den
        new_num = self.num * other_fraction.num
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        return self + Fraction(-other_fraction.num, other_fraction.den)

    def __lt__(self, other_fraction):
        return (self.num / self.den) < (other_fraction.num /
                                        other_fraction.den)

    def __gt__(self, other_fraction):
        return (self.num / self.den) > (other_fraction.num /
                                        other_fraction.den)

    def __iadd__(self, other):
        self = self + other
        return self

    def __repr__(self):
        return f"Fraction({self.num}/{self.den})"

    def __radd__(self, other):
        return self + other

    def recip(self):
        return Fraction(self.den, self.num)

    def __truediv__(self, other_fraction):
        return self * other_fraction.recip()

    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))


x = Fraction(1, 2)
y = Fraction(2, 3)
print("__radd__ functionality:")
print(1.5 + y)
print()

print("__iadd__ functionality:")
y += Fraction(2, 3)
print(y)