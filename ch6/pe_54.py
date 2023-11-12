from collections import Counter


def parsecard(s):
    return (int(s[0]) if s[0].isnumeric() else 'TJQKA'.index(s[0]) + 10, s[1])


def high_card(h):
    return max([c for c, s in h])


def one_pair(h):
    C = Counter()
    for c, s in h:
        C[c] += 1

    prs = [c for c, s in h if C[c] == 2]
    return max(prs) if len(prs) else None


def two_pairs(h):
    C = Counter()
    for c, s in h:
        C[c] += 1

    prs = list(set([c for c, s in h if C[c] == 2]))
    return (prs[0], prs[1]) if len(prs) >= 2 else None


def three_kind(h):
    C = Counter()
    for c, s in h:
        C[c] += 1

    prs = list(set([c for c, s in h if C[c] == 3]))
    return prs[0] if len(prs) >= 1 else None


def four_kind(h):
    C = Counter()
    for c, s in h:
        C[c] += 1

    prs = list(set([c for c, s in h if C[c] == 4]))
    return prs[0] if len(prs) >= 1 else None


def straight(h):
    svs = list([c for c, s in h])
    svs.sort()
    return svs[0] if all(
        (svs[i] == i + svs[0] for i in range(len(h)))) else None


def flush(h):
    return high_card(h) if len(set([s for c, s in h])) == 1 else None


def fullhouse(h):
    p3 = three_kind(h)
    p2 = one_pair(h)
    return None if (p3 is None or p2 is None) else (p3, p2)


def straight_flush(h):
    fsh = flush(h)
    stt = straight(h)
    return None if (fsh is None or stt is None) else stt


def royal_flush(h):
    cvs = [c for c, s in h]
    if all([e in cvs for e in [10, 11, 12, 13, 14]]):
        suit = [s for c, s in h if c == 11][0]
        if all([s == suit for c, s in h]):
            return 1

    return None


def p(s):
    return [parsecard(c) for c in s.split()]


def gt(a, b):
    # print(a, b)
    return None if (
        a is None and b is None) else (a is not None) and (b is None or a > b)


# print(royal_flush())


def a_wins_b(a, b):
    l = [
        gt(royal_flush(a), royal_flush(b)),
        gt(straight_flush(a), straight_flush(b)),
        gt(four_kind(a), four_kind(b)),
        gt(fullhouse(a), fullhouse(b)),
        gt(flush(a), flush(b)),
        gt(straight(a), straight(b)),
        gt(three_kind(a), three_kind(b)),
        gt(two_pairs(a), two_pairs(b)),
        gt(one_pair(a), one_pair(b)),
        gt(high_card(a), high_card(b))
    ]

    # print(l)

    for e in l:
        if e is not None:
            return e


hs = [p(l.strip()) for l in open("pe_54.txt").readlines()]

print(len([h for h in hs if a_wins_b(h[:5], h[5:])]))
