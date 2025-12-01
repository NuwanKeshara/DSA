
# a = ["a", 2]
# b = ["a", 2]

# if a == b:
#     print('yes')
# else:
#     print("no")


# # immutable object
# a = b = 0

# # mutable object
# a = b = {}

# print(id(a))
# print(id(b))

# a[1] = 1

# print(id(a))
# print(id(b))


# print({'a':1, 'b':2} == {'b':2, 'a':12})
# dict = {}
# a = {'a':1}
# dict[str(a)] = 1
# print(dict.get())

# print(sorted("jgrjfuy"))

# s = ""
# print(s[4:4])

import collections


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, val: int) -> None:
        node = TreeNode(val)
        curr = self.head

        if not curr:
            self.head = node
        else:
            while curr:
                if curr.val > val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = node
                        return
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = node
                        return
    
    def inorder_recursive(self) -> list[int]:
        if not self.head:
            return []
        
        stack = []
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)

        inorder(self.head)
        return stack


    def inorder_iterative(self) -> list[int]:
        if not self.head:
            return []
        
        stack, res = [], []
        curr = self.head
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


    def preorder_recursive(self) -> list[int]:
        if not self.head:
            return []
        
        stack = []
        def preorder(root):
            if not root:
                return
            stack.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(self.head)
        return stack
    

    def preorder_iterative(self) -> list[int]:
        if not self.head:
            return []
        
        res, stack = [], []
        curr = self.head
        while curr or stack:
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            
            curr = stack.pop()
            curr = curr.right

        return res


    def preorder_iterative2(self) -> list[int]:
        if not self.head:
            return []
        
        curr = self.head
        stack, res = [], []
        while curr or stack:
            if curr:
                stack.append(curr.right)
                res.append(curr.val)
                curr = curr.left 
            else:
                curr = stack.pop()
        return res
    

    def postorder_recursive(self) -> list[int]:
        stack = []
        
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            stack.append(root.val)

        postorder(self.head)
        return stack


    def postorder_iterative(self) -> list[int]:
        stack1, stack2 = [self.head], []
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


    def BFS(self) -> list[list[int]]:
        res = []
        queue = collections.deque()
        queue.append(self.head)

        while queue:
            qlen = len(queue)
            lvl = []
            for _ in range(qlen):
                node = queue.popleft()
                lvl.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(lvl)
        return res
