from bst import BTN


class AVLN(BTN):

    def __init__(self, key=None, value=None):
        self.value = value
        self.key = key
        self.parent: AVLN | None = None
        self.lchild: AVLN | None = None
        self.rchild: AVLN | None = None
        self.balfac: int = 0

    def print(self, d=0):
        print("\t" * d, self.key, "->", self.value, f"({self.balfac})")
        if (self.lchild is not None):
            self.lchild.print(d + 1)
        else:
            print("\t" * (d + 1), "NONE")

        if (self.rchild is not None):
            self.rchild.print(d + 1)
        else:
            print("\t" * (d + 1), "NONE")


class AVLTree():

    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        self.set(self.root, key, value)

    def set(self, node, key, value):
        if (self.root is None):
            self.root = AVLN(key, value)
            return

        if (key == node.key):
            node.value = value
        elif (key > node.key):
            if (node.rchild is None):
                node.rchild = AVLN(key, value)
                node.rchild.parent = node
                self.set_balances(node.rchild)
            else:
                self.set(node.rchild, key, value)
        else:
            if (node.lchild is None):
                node.lchild = AVLN(key, value)
                node.lchild.parent = node
                self.set_balances(node.lchild)
            else:
                self.set(node.lchild, key, value)

    def set_balances(self, node):
        if node.balfac > 1 or node.balfac < -1:
            self.rebalance(node)
            return
        if (node.parent is not None):
            if (node.parent.lchild == node):
                node.parent.balfac += 1
            elif (node.parent.rchild == node):
                node.parent.balfac -= 1
            if (node.parent.balfac != 0):
                self.set_balances(node.parent)

    def rebalance(self, node):
        print(f"Rebalancing node {node.key}")
        if (node.balfac < 0):
            if (node.rchild.balfac > 0):
                self.rot_r(node.rchild)
                self.rot_l(node)
            else:
                self.rot_l(node)
        else:
            if (node.lchild.balfac < 0):
                self.rot_l(node.lchild)
                self.rot_r(node)
            else:
                self.rot_r(node)

    def __delitem__(self, key):
        # TODO: Delete using a copy of the BTN method but find which node needs to be rebalanced and correctly edit balfac-s
        # Maybe abstract the delete method a bit more (successor method, etc.)

    def print(self):
        if self.root is not None:
            self.root.print()

    def rot_l(self, node: AVLN):
        newroot = node.rchild
        node.rchild = newroot.lchild
        if (newroot.lchild is not None):
            newroot.lchild.parent = newroot
        newroot.parent = node.parent
        if (newroot.parent is None):
            self.root = newroot
        else:
            if (node.parent.lchild == node):
                node.parent.lchild = newroot
            else:
                node.parent.rchild = newroot

        newroot.lchild = node
        node.parent = newroot
        node.balfac = (node.balfac + 1 - min(newroot.balfac, 0))
        newroot.balfac = (newroot.balfac + 1 + max(node.balfac, 0))

    def rot_r(self, node: AVLN):
        newroot = node.lchild
        node.lchild = newroot.rchild
        if (newroot.rchild is not None):
            newroot.rchild.parent = newroot

        newroot.parent = node.parent
        if (newroot.parent is None):
            self.root = newroot
        else:
            if (node.parent.lchild == node):
                node.parent.lchild = newroot
            else:
                node.parent.rchild = newroot

        newroot.rchild = node
        node.parent = newroot
        node.balfac = (node.balfac - 1 - max(newroot.balfac, 0))
        newroot.balfac = (newroot.balfac - 1 - min(node.balfac, 0))

    def __getitem__(self, key):
        return None if (self.root is None) else self.root[key]


t = AVLTree()
t['a'] = None
t['b'] = None
t['c'] = None
t['d'] = None
t['e'] = None
t['f'] = None
t['g'] = None

t.print()
