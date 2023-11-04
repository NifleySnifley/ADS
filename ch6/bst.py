class BTN():

    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.lchild = None
        self.rchild = None

    def print(self, d=0):
        print("\t" * d, self.key, "->", self.value)
        if (self.lchild is not None):
            self.lchild.print(d + 1)
        if (self.rchild is not None):
            self.rchild.print(d + 1)

    def insert(self, node):
        val = node.key
        if (val == self.key):
            self.value = node.value
        elif (val > self.key):
            if (self.rchild is None):
                self.rchild = node
            else:
                self.rchild.insert(node)
        else:
            if (self.lchild is None):
                self.lchild = node
            else:
                self.lchild.insert(node)

    def find_node(self, key):
        # print(f"I am {self.key}, value is {self.value}")
        if (self.key == key):
            return self
        else:
            if (key < self.key and self.lchild is not None):
                return self.lchild.find_node(key)
            elif (self.rchild is not None):
                return self.rchild.find_node(key)
        return None

    def find(self, key):
        n = self.find_node(key)
        return n.value if (n is not None) else None

    def items(self):
        if (self.lchild is not None):
            for k in self.lchild.items():
                yield k
        yield (self.key, self.value)
        if (self.rchild is not None):
            for k in self.rchild.items():
                yield k

    def values(self):
        return (v for k, v in self.items())

    def keys(self):
        return (k for k, v in self.items())

    def __contains__(self, key):
        if (self.key == key):
            return True
        else:
            if (key < self.key and self.lchild is not None):
                return key in self.lchild
            elif (self.rchild is not None):
                return key in self.rchild
        return False

    def __setitem__(self, key, value):
        node = BTN(key, value)
        self.insert(node)

    def max(self):
        if (self.rchild is None):
            return self.value
        else:
            return self.rchild.max()

    def min(self):
        if (self.lchild is None):
            return self.value
        else:
            return self.lchild.min()

    def min_node(self):
        if (self.lchild is None):
            return self
        else:
            return self.lchild.min_node()

    def __getitem__(self, key):
        return self.find(key)

    # Transplant replace subtree U with subtree V
    # p is
    def transplant(self, u, v, up, vp):
        if (up.lchild is not None) and u.key == up.lchild.key:
            up.lchild = v
        else:
            up.rchild = v
        if v is not None:
            vp = up

    def __delitem__(self, key):
        parent = self
        n = None
        isl = False
        while True:
            if (parent.lchild is not None and parent.lchild.key == key):
                n = parent.lchild
                isl = True
                break
            elif (parent.rchild is not None and parent.rchild.key == key):
                n = parent.rchild
                break
            else:
                if (key > parent.key and parent.rchild is not None):
                    parent = parent.rchild
                elif (parent.lchild is not None):
                    parent = parent.lchild
                else:
                    return  # Value no exist

        if (n.lchild is None):
            if (isl):
                parent.lchild = n.rchild
            else:
                parent.rchild = n.rchild
        elif (n.rchild is None):
            if (isl):
                parent.lchild = n.lchild
            else:
                parent.rchild = n.lchild
        else:
            # Successor
            y = n.rchild
            yp = n
            while (y.lchild is not None):
                yp = y
                y = yp.lchild

            # n is not y's parent
            if y.key not in [n.lchild.key, n.rchild.key]:
                self.transplant(y, y.rchild, yp, y)
                y.rchild = n.rchild

            self.transplant(n, y, parent, yp)
            y.lchild = n.lchild


bst = BTN(70)
bst[14] = "hi"
bst[91] = None
bst[95] = None
bst[93] = None
bst[92] = 'aa'
bst[94] = None

bst[100] = "max!"

print(bst[14])
print(bst[92])

bst[14] = "bye"
bst.print()

print(bst[14])
print(list(bst.keys()))
print(list(bst.values()))
print(73 in bst)
print(20 in bst)

print(bst.max())

del bst[95]
bst.print()

# bst = BTN(17)
# # bst[25] = None
# bst[35] = None
# bst[29] = None
# bst[38] = None
# bst[5] = None
# bst[2] = None
# bst[11] = None
# bst[9] = None
# bst[7] = None
# bst[8] = None
# bst[16] = None

# del bst[5]

# bst.print()
