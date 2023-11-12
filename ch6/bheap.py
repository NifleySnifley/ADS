# from collections import deque


class BHeap():

    def __init__(self, items=None, cap=None):
        self.arr = ([] if items is None else items)
        if (len(self.arr) > 0):
            for i in range(len(self.arr) - 1, -1, -1):
                self.heapify(i)

        self.cap = cap

    def __len__(self):
        return len(self.arr)

    def parent(self, i):
        return (i - 1) // 2

    def lchild(self, i):
        return i * 2 + 1

    def rchild(self, i):
        return i * 2 + 2

    def insert(self, v):
        self.arr.append(v)
        self.perc()
        if self.cap is not None and len(self.arr) > self.cap:
            # Only try to remove the last two nodes (final children?)
            # TODO: Prove correctness, this is just based on intuition
            if len(self.arr) >= 2:
                if (self.arr[-1] > self.arr[-2]):
                    self.arr.pop()
                else:
                    v = self.arr.pop()
                    self.arr.pop()
                    self.insert(v)
            else:
                self.arr.pop()
        # self.heapify()

    def perc(self):
        cn = len(self.arr) - 1
        while cn >= 2:
            # Rotate up
            if (self.arr[self.parent(cn)] > self.arr[cn]):
                self.arr[cn], self.arr[self.parent(cn)] = self.arr[self.parent(
                    cn)], self.arr[cn]
            cn = self.parent(cn)

    def heapify(self, i=0):
        l = self.lchild(i)
        r = self.rchild(i)
        sm = i
        if (l < len(self.arr)) and self.arr[l] < self.arr[i]:
            sm = l
        if (r < len(self.arr)) and self.arr[r] < self.arr[sm]:
            sm = r

        if (sm != i):
            self.arr[i], self.arr[sm] = self.arr[sm], self.arr[i]
            self.heapify(sm)

    def remove_min(self):
        self.arr[0], self.arr[-1] = self.arr[-1], self.arr[0]
        m = self.arr.pop()

        self.heapify(0)

        return m


# Exercises 2 #8
def heapsort(l):
    h = BHeap(l)
    return [h.remove_min() for i in range(len(h))]


h = BHeap()  #[3, 4, 5, 2, 1, 10])

h.arr = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

h.insert(7)

print(h.arr)

print(h.remove_min())
print(h.remove_min())
print(h.remove_min())
print(h.remove_min())
print(h.remove_min())
# print(h.remove_min())

print(h.arr)

print("Heapsorting")
print(heapsort([2, 1, 5, 7, 1, 2, 9, 4, 2, 6, 9]))

print("Capacity")
c = BHeap(cap=6)
c.insert(2)
c.insert(3)
c.insert(13)
c.insert(5)
c.insert(9)
c.insert(1)
c.insert(20)
c.insert(0)

print(c.arr)
