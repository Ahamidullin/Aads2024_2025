class Node:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None


n = int(input())
raw = [[int(i) for i in input().split()] for _ in range(n)]
# print(raw)


def createTree(raw):
    nodes = [Node() for i in range(len(raw))]
    for i in range(len(raw)):
        nodes[i].key = raw[i][0]
        nodes[i].left = None if raw[i][1] == -1 else nodes[raw[i][1]]
        nodes[i].right = None if raw[i][2] == -1 else nodes[raw[i][2]]
    return nodes


def inOrder(node):
    if node != None:
        inOrder(node.left)
        print(node.key,end= " ")
        inOrder(node.right)

def preOrder(node):
    if node != None:
        print(node.key, end = " ")
        preOrder(node.left)
        preOrder(node.right)

def postOrder(node):
    if node != None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.key,end= " ")


nodes = createTree(raw)
# for node in nodes:
#     print(node.key, node.left.key if node.left is not None else None,
#           node.right.key if node.right is not None else None,)

inOrder(nodes[0])
print()
preOrder(nodes[0])
print()
postOrder(nodes[0])

# 10
# 0 7 2
# 10 -1 -1
# 20 -1 6
# 30 8 9
# 40 3 -1
# 50 -1 -1
# 60 1 -1
# 70 5 4
# 80 -1 -1
# 90 -1 -1

# 50 70 80 30 90 40 0 20 10 60
# 0 70 50 40 30 80 90 20 60 10
# 50 80 90 30 40 70 10 60 20 0