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

    def __getitem__(self, key):
        return self.find(key)

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

        # Either the sibling or the
        print(parent.key, n.key)

        print(f"successor is left? {isl}")

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
            # Two children oh no
            #TODO do the thing
            pass


bst = BTN(70)
bst[14] = "hi"
bst[91] = None
bst[95] = None
bst[93] = None
bst[92] = None
bst[94] = None

bst[100] = "max!"

print(bst[14])

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
