class Node:
    def __init__(self):
        Node.key = None
        Node.left = None
        Node.right= None


def insert(root,new_node):
    if root is None:
        return new_node
    if root.key < new_node.key:
        if root.right == None:
            root.right = new_node
        else:
            insert(root.right,new_node)
    else:
        if root.left == None:
            root.left = new_node.key
        else:
            insert(root.left,new_node)


f = open("input.txt")
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)






