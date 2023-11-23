from operator import or_, add
from functools import reduce


class BitsetGen():

    def __init__(self, keys=None, frozen=True):
        self.keys = {}
        self.keys_rev = []
        self.len = 0
        self.frozen = frozen

        if (keys is not None):
            keys.sort()
            for k in keys:
                self.addkey(k)

    def addkey(self, key):
        if key in self.keys:
            return
        else:
            self.keys_rev.append(key)
            self.keys[key] = 1 << (self.len)
            self.len += 1

    def __len__(self):
        return self.len

    def values(self):
        return self.keys_rev.__iter__()

    def iter(self, s: int):
        for i in range(self.len):
            if (s & (1 << i)):
                yield self.dec_val(s & (1 << i))

    def enc(self, value):
        if isinstance(value, set) or isinstance(value, list):
            s = 0
            for v in value:
                s |= self.enc(v)
            return s
        elif value in self.keys:
            return self.keys[value]
        else:
            if self.frozen:
                print("Error, key not found in set, aborting!")
                raise KeyError()
            else:
                print("Warning, key not found in set, adding!")
                self.addkey(value)
                return self.keys[value]

    def dec_val(self, value: int):
        if value.bit_count() > 1:
            print("Error decoding value, more than one value in set!")
        else:
            if value == 0:
                return None
            else:
                bi = (value.bit_length() - 1)
                if 0 <= bi < len(self.keys_rev):
                    return self.keys_rev[bi]
                else:
                    raise IndexError()

    def dec_set(self, value: int):
        return set(self.iter(value))

    def tostr(self, bset: int):
        return "b{" + ', '.join([str(v) for v in self.iter(bset)]) + "}"


def flatten(arr):
    try:
        return [] if len(arr) == 0 else reduce(add, map(flatten, arr))
    except Exception:
        return [arr]


if __name__ == "__main__":
    b = BitsetGen(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

    s1 = b.enc(list('abcfaaba'))
    print(bin(s1))
    print(b.tostr(s1))

    print(flatten(['a', [], 'b', ['c', ['d']]]))
