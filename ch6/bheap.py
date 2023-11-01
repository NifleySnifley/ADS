class BHeap():
    def __init__(self):
        self.arr = []
        
    def parent(self, i):
        return (i-1) // 2
    
    def lchild(self, i):
        return i * 2 + 1
    
    def rchild(self,i):
        return i * 2 + 2
    
    def insert(self, v):
        self.arr.append(v)
        self.perc()
    
    def perc(self):
        cn = len(self.arr) - 1
        while cn >= 2:
            # Rotate up
            if (self.arr[self.parent(cn)] > self.arr[cn]):
                self.arr[cn], self.arr[self.parent(
                    cn)] = self.arr[self.parent(cn)], self.arr[cn]
            cn = self.parent(cn)
            
    def remove_min(self):
        m = self.arr[0]
        del self.arr[m]
        
        return m
        
h = BHeap()

h.arr = [5,9,11,14,18,19,21,33,17,27]

h.insert(7)

print(h.arr)