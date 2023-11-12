lnames = {
    i: v
    for i, v in enumerate([
        "", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
    ])
}
lnames[30] = 'thirty'
lnames[40] = 'forty'
lnames[50] = 'fifty'
lnames[60] = 'sixty'
lnames[70] = 'seventy'
lnames[80] = 'eighty'
lnames[90] = 'ninety'

# llens = [len(s) for s in lnames]


def nstr(n):
    if n in lnames:
        return lnames[n]
    else:
        tens = (n % 100) // 10
        thousands = n // 1000
        hundreds = (n % 1000) // 100
        ones = n % 10

        ns = ''
        if (thousands > 0):
            ns += f"{lnames[thousands]} thousand"
        if (hundreds > 0):
            ns += (' and' if len(ns) else '') + f"{lnames[hundreds]} hundred"
        if tens > 1:
            ns += (' and' if len(ns) else '') + f" {lnames[tens*10]}"
        if 0 < ones + tens * 10 < 20:
            ns += (' and' if len(ns) else '') + f" {lnames[ones + tens*10]}"
        elif tens > 0 and ones > 0:
            ns += f" {lnames[ones]}"
        return ns


print(sum([len(nstr(e).replace(' ', '')) for e in range(1, 1000 + 1)]))
