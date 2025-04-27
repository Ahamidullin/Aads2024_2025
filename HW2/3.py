class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None

n = int(input())
raw = [[int(i) for i in input().split()] for _ in range(n)]

def createTree(raw):
    nodes = [Node() for i in range(len(raw))]
    for i in range(len(raw)):
        nodes[i].key = raw[i][0]
        if 0 <= raw[i][1] < len(nodes):
            nodes[i].left = nodes[raw[i][1]]
        else:
            nodes[i].left = None

        if 0 <= raw[i][2] < len(nodes):
            nodes[i].right = nodes[raw[i][2]]
        else:
            nodes[i].right = None
    return nodes

x = []
def check(node, parent=None, isLeft=False):
    if node is not None:
        check(node.left, parent=node.key, isLeft=True)

        if isLeft:
            if parent and node.key >= parent:
                x.append(None)
            else:
                x.append(node.key)
        else:
            if parent and node.key < parent:
                x.append(None)
            else:
                x.append(node.key)

        check(node.right, parent=node.key, isLeft=False)

nodes = createTree(raw)

if n:
    check(nodes[0])
    print(x)
    if None in x:
        print("INCORRECT")
    else:
        print("CORRECT" if sorted(x) == x else "INCORRECT")
else:
    print("CORRECT")





# 3
# 2 1 2
# 1 -1 -1
# 1 -1 -1