values = [
    17,
    45,
    96,
]


def div2rem(n):
    stack = []
    while n != 0:
        stack.append(n % 2)
        n //= 2

    s = ""
    while (len(stack)):
        s+=str(stack.pop())
    return s


print(div2rem(0xAA))
print(bin(0xAA))
