class Node:
    def __init__(self, val1, val2):
        self.key1 = val1
        self.key2 = val2
        self.left = None
        self.right = None


# def createbintree(data, ind=None):  # строит бинарное дерево по первому ключу (массив отсортирован)
#     if data:
#         mid = ind if ind else len(data) // 2
#         node = Node(*data[mid])
#         if len(data) > 1:
#             node.left = createbintree(data[:mid])
#             node.right = createbintree(data[mid + 1:])
#         return node


def create_bin_tree(data):
    root = None
    for elem in data:
        current = root
        parent = None
        dir = None
        while current:
            if current.key1 > elem[0]:
                parent = current
                current = current.left
                dir = "left"
            elif current.key1 < elem[0]:
                parent = current
                current = current.right
                dir = "right"
        node = Node(*elem)
        if parent:
            if dir == "left":
                parent.left = node
            elif dir == "right":
                parent.right = node
        else:
            root = node
    return root



def in_order(node):
    if node is not None:
        in_order(node.left)
        print(f"({node.key1}, {node.key2})")
        in_order(node.right)


# max heap: корень - макс; дети - меньше относительно родителя
def check_maxheap(node):
    if node:
        left = False if node.left and node.left.key2 >= node.key2 else check_maxheap(node.left)
        right = False if node.right and node.right.key2 >= node.key2 else check_maxheap(node.right)
        return left and right
    else:
        return True

def check_minheap(node):
    if node:
        left = False if node.left and node.left.key2 <= node.key2 else check_minheap(node.left)
        right = False if node.right and node.right.key2 <= node.key2 else check_minheap(node.right)
        return left and right
    else:
        return True


data = [[int(i) for i in input().split()] for _ in range(int(input()))]
for i in range(len(data)):
    root = create_bin_tree(data, i)
    # in_order(root)
    print(check_maxheap(root) or check_minheap(root))








