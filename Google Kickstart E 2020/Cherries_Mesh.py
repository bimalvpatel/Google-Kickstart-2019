class Node:

    def __init__(self,val):
        self.val = val
        self.parent = None

class UnionFind:

    def __init__(self):
        self.nodes = {}
        self.count = 0

    def insert(self,val):
        node = Node(val)
        node.parent = node
        self.nodes[val] = node
        self.count += 1

    def find(self,val):
        node = self.nodes[val]
        if node.parent == node:
            return node.parent
        node.parent = self.find(node.parent.val)
        return node.parent

    def union(self,val1,val2):
        node1 = self.find(val1)
        node2 = self.find(val2)
        if node1 == node2:
            return False
        node1.parent = node2
        self.count -= 1
        return True

    def distinctnode(self):
        return self.count

def solve():

    no_of_cherries, no_of_con = map(int,input().split())
    con = []

    for _ in range(no_of_con):
        con.append(list(map(int,input().split())))

    sugar = 0

    uf = UnionFind()

    for i in range(no_of_cherries):
        uf.insert(i+1)

    for i,j in con:
        if uf.union(i,j):
            sugar += 1

    return sugar + 2*(uf.distinctnode()-1)










if __name__ == '__main__':
    for i in range(int(input())):
        print("Case #" + str(i+1) + ": " + str(solve()))