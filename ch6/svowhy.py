import itertools, math


# Goursat's surface
def f(x, y, z):
    a = -0.1
    b = -1.5
    c = 1
    return x**4 + y**4 + z**4 + a * (x * x + y * y + z * z)**2 + b * (
        x * x + y * y + z * z) + c


# Used this function of a sphere (r=1.0), V=1.18879 to show correctness
def g(x, y, z):
    return math.sqrt(x * x + y * y + z * z) - 1.0


def volume(fn, sth=0.05, x=-1.0, y=-1.0, z=-1.0, s=2.0):
    return (1 if fn(x + 0.5 * s, y + 0.5 * s, z + 0.5 * s) < 0 else 0) * (
        s**3) if s <= sth else sum([
            volume(fn, sth, x + xo * s, y + yo * s, z + zo * s, s / 2)
            for xo, yo, zo in itertools.product([0, 0.5], [0, 0.5], [0, 0.5])
        ])


print(f"Sphere: {volume(g)}")
print(f"Goursat: {volume(f)}")
