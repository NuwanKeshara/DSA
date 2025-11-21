class TreeNode:
    def __init__(self, val: int =0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.head = None
    
    def add(self, val=0):
        node = TreeNode(val=val)

        if self.head:
            curr = self.head
            while True:
                if curr.val > val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        break
        else:
            self.head = node

    
    def inOrder(self):
        ...
    
    def preOrder(self):
        ...

    def postOrder(self):
        ...

    def BFS(self):
        ...


    def __str__(self):
        print("Binary Serch Tree")