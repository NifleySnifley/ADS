class DLL_Node():

    def __init__(self, value):
        self.value = value
        self.next: DLL_Node | None = None
        self.prev: DLL_Node | None = None

    def setnext(self, next):
        self.next = next

    def setprev(self, next):
        self.prev = next

    def chain(self, b):
        self.setnext(b)
        b.setprev(self)


class DLL_Iter():

    def __init__(self, dll, rev):
        self.list = dll
        self.rev = rev
        self.cur = dll.tail if rev else dll.head

    def __iter__(self):
        self.cur = self.list.tail if self.rev else self.list.head
        return self

    def __next__(self):
        if (self.cur is None):
            raise StopIteration
        else:
            c = self.cur
            self.cur = self.cur.prev if self.rev else self.cur.next
            return c.value


class DLL():

    def __init__(self):
        self.head: DLL_Node | None = None
        self.tail: DLL_Node | None = None
        self.length = 0

    def __iter__(self):
        return DLL_Iter(self, False)

    def __len__(self):
        return self.length

    def backwards(self):
        return DLL_Iter(self, True)

    def add_front(self, value):
        n = DLL_Node(value)
        self.length += 1

        if (self.length == 1):
            self.head = n
            self.tail = n
            return
        ph = self.head
        n.chain(ph)
        self.head = n

    def add_back(self, value):
        n = DLL_Node(value)
        self.length += 1
        if (self.length == 1):
            self.head = n
            self.tail = n
            return

        self.tail.chain(n)
        self.tail = n

    def as_list(self):
        cur = self.head
        l = []
        while (cur is not None):
            l.append(cur.value)
            cur = cur.next
        return l

    def as_list_rev(self):
        cur = self.tail
        l = []
        while (cur is not None):
            l.append(cur.value)
            cur = cur.prev
        return l

    def pop_front(self):
        if (self.head is None):
            raise IndexError("Pop from empty DLL")
        else:
            n = self.head
            self.head = self.head.next
            if (self.head is not None): self.head.setprev(None)
            self.length -= 1
            if (self.length == 0):
                self.tail = self.head = None
            return n.value

    def pop_back(self):
        if (self.tail is None):
            raise IndexError("Pop from empty DLL")
        else:
            n = self.tail
            self.tail = self.tail.prev
            if (self.tail is not None): self.tail.setnext(None)
            self.length -= 1
            if (self.length == 0):
                self.tail = self.head = None
            return n.value

    def node_at(self, index):
        if (index < 0 or index >= len(self)):
            return None
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur

    def insert(self, index, value):
        if index < 0 or index > len(self):
            raise IndexError
        before = self.node_at(index - 1)
        after = self.node_at(index)
        n = DLL_Node(value)
        if (before is not None):
            before.chain(n)
        if (after is not None):
            n.chain(after)

        if (index == 0):
            self.head = n
        if (index == len(self) - 1):
            self.tail = n

        self.length += 1

    def __contains__(self, value):
        return any(item == value for item in self)


ll = DLL()

ll.add_back("b")
ll.add_back("c")
ll.add_back("d")
ll.add_front("a")
print(ll.as_list())
print(ll.as_list_rev())

ll.insert(4, "0")
for i in ll:
    print(i)

print("0" in ll)
