import collections
from typing import Optional


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


    # inorder traversal
    def inOrder(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        return res
    
    def inOrder_iterative(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
    

    # preorder traversal
    def preOrder(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return res
    
    def preOrder_iterative(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        return res
    
    def preOrder_iterative2(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left

            else:
                curr = stack.pop()

        return res


    # postorder traversal
    def postOrder(self, root: Optional[TreeNode]) -> list[int]:
        res = []

        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res
    
    def postorder_iterative(self, root: Optional[TreeNode]) -> list[int]:
        stack1, stack2 = [root], []
        res = []

        while stack1:
            curr = stack1.pop()
            stack2.append(curr.val)
            if curr.left:
                stack1.append(curr.left)
            if curr.right:
                stack1.append(curr.right)

        while stack2:
            res.append(stack2.pop())
        return res


    # breadth first search traversal
    def BFS(self, root: Optional[TreeNode]) -> list[int]:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            qlen = len(queue)
            lvl = []
            for _ in range(qlen):
                curr = queue.popleft()
                lvl.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(lvl)
        return res



    def __str__(self):
        print("InOrder Traversl:", str(self.inOrder(self.head)))
        print("PreOrder Traversl:", str(self.preOrder(self.head)))
        print("PreOrder Traversl2:", str(self.preOrder_iterative2(self.head)))
        print("PostOrder Traversl:", str(self.postOrder(self.head)))
        print("PostOrder Traversl2:", str(self.postorder_iterative(self.head)))
        print("BFS Traversl:", str(self.BFS(self.head)))
        return ""


    

if __name__ == "__main__":
    bt = BinaryTree()
    bt.add(5)
    bt.add(3)
    bt.add(7)
    bt.add(1)
    bt.add(4)
    bt.add(6)

    print(bt)