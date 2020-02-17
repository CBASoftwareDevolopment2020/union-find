# UnionFind


class QuickFind:
    def __init__(self, n):
        self.id = [x for x in range(n)]

    def union(self, p, q):
        # self.id = [self.id[q] if x is self.id[p] else x for x in self.id]
        p = self.id[p]
        q = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] is p:
                self.id[i] = q

    def find(self, p):
        return self.id[p]

    def count(self):
        return len(set(self.id))


class QuickUnion:
    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root != q_root:
            self.id[p_root] = q_root
            self.count -= 1


class WeightedQuickUnion:
    def __init__(self, n):
        self.count = n
        self.id = [x for x in range(n)]
        self.size = [1 for x in range(n)]

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root != q_root:
            if self.size[p_root] < self.size[q_root]:
                self.id[p_root] = q_root
                self.size[q_root] += self.size[p_root]
            else:
                self.id[q_root] = p_root
                self.size[p_root] += self.size[q_root]
            self.count -= 1
