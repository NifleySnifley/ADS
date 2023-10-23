import turtle

reduction = {"A": "DAAB", "B": "CBBA", "C": "BCCD", "D": "ADDC"}

steps = {"A": "URD", "B": "LDR", "C": "DLU", "D": "RUL"}


def step(s, length):
    turtle.setheading({"U": 90, "L": 180, "R": 0, "D": 270}[s])
    turtle.forward(length)


def hilbert(move="C", level=10):
    if (level <= 1):
        for s in steps[move]:
            step(s, 2**(level))
    else:
        red = reduction[move]
        s = steps[move]
        hilbert(red[0], level - 1)
        step(s[0], 2)
        hilbert(red[1], level - 1)
        step(s[1], 2)
        hilbert(red[2], level - 1)
        step(s[2], 2)
        hilbert(red[3], level - 1)


turtle.speed(10000)

hilbert(level=5)

turtle.Screen().mainloop()
