# from collections import deque


class BHeap():

    def __init__(self, items=None):
        self.arr = ([] if items is None else items)
        if (len(self.arr) > 0):
            for i in range(len(self.arr) - 1, -1, -1):
                self.heapify(i)

    def parent(self, i):
        return (i - 1) // 2

    def lchild(self, i):
        return i * 2 + 1

    def rchild(self, i):
        return i * 2 + 2

    def insert(self, v):
        self.arr.append(v)
        self.perc()
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
