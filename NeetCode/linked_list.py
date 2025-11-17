from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Node:
    def __init__(self, val: int = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    # def __init__(self):
    #     self.head = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left, right = None, head

        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp
        
        return left


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            if list1.val <= list2.val:
                head, tail = list1, list1
                curr1 = list1.next
                curr2 = list2
            else:
                head, tail = list2, list2
                curr2 = list2.next
                curr1 = list1
            
            while curr1 and curr2:

                if curr1.val <= curr2.val:
                    tail.next = curr1
                    curr1 = curr1.next
                else:
                    tail.next = curr2
                    curr2 = curr2.next
                tail = tail.next
            
            if curr1:
                tail.next = curr1
            elif curr2:
                tail.next = curr2
            
            return head
        

    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
            
        return False


    def hasCycle2(slef, head: Optional[ListNode]) -> bool:
        hashSet = set()

        while head:
            if head in hashSet:
                return True
            else:
                hashSet.add(head)
            head = head.next
        return False

    def reorderList(self, head: Optional[ListNode]) -> ListNode:
        hashMap = {}
        index = 0

        while head:
            hashMap[index] = head
            head = head.next
            index += 1
        # print(hashMap)

        dummy = ListNode()
        head = dummy
        while hashMap:
            minNode = hashMap[min(hashMap)]
            dummy.next = minNode
            dummy = dummy.next
            hashMap.pop(min(hashMap))

            if hashMap:
                maxNode = hashMap[max(hashMap)]
                dummy.next = maxNode
                dummy = dummy.next
                hashMap.pop(max(hashMap))
            
        dummy.next = None
        self.head = head.next


    def reorderList2(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = slow
        slow = slow.next
        prev = temp.next = None

        # first - head, second - slow

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        first, second = head, prev
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        hashMap = {}
        curr = head
        index = 0

        while curr:
            hashMap[index] = curr
            curr = curr.next
            index += 1
        
        next = None 
        nth_index = index - n    
        for i in range(index-1, -1, -1):
            if i == nth_index:
                continue
            hashMap[i].next = next
            next = hashMap[i]
            
        return next
    


    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        index = 0
        while curr:
            curr = curr.next
            index += 1

        nth_index = index - n
        prev = ListNode(next=head)
        new = prev 
        next = head

        for i in range(nth_index + 1):
            if i == nth_index:
                prev.next = next.next

            prev = next
            next = next.next
        return new.next
    


    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            prev = prev.next
            right = right.next

        prev.next = prev.next.next
        return dummy.next


    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        hashMap = {head:None}
        node = head

        while node:
            new = Node(node.val)
            hashMap[node] = new
            node = node.next

        node = head

        while node:
            if node.next:
                hashMap[node].next = hashMap[node.next]
            if node.random:
                hashMap[node].random = hashMap[node.random]
            
            node = node.next
        return hashMap[head]



class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val) -> Node:
        curr = Node(val)

        if not self.head:
            self.head = curr
            self.tail = curr
        else: 
            self.tail.next = curr
            self.tail = curr
        return self.head
    
    # def __repr__(self):
    #     return f"{self.head}"
    
    def __str__(self):
        vals = []
        curr = self.head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        return str(vals)
    




class Nodex:
    def __init__(self, val=0, key=0, next=None, prev=None):
        self.val = val
        self.key = key
        self. next = next
        self.prev = prev


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.mru = self.lru = None

    # remove node from anywhere in the doubly linkedlist
    def remove(self, node: Node) -> None:
        prev_node, next_node = node.prev, node.next
        node.next = node.prev = None

        if prev_node and next_node:
            prev_node.next, next_node.prev = next_node, prev_node
        elif prev_node is None and next_node:
            self.lru, next_node.prev = next_node, None
        elif prev_node and next_node is None:
            self.mru, prev_node.next = prev_node, None
        else:
            self.lru = self.mru = None
            
    # insert far right into the doubly linkedList
    def insert(self, node: Node) -> None:
        if self.mru and self.lru:
            node.prev = self.mru
            node.next = None
            self.mru.next = node
            self.mru = node
        else:
            self.lru = self.mru = node
            node.next = node.prev = None
    

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    # add a new node to far right in the doubly linkedlist
    def put(self, key: int, value: int) -> None:
        new_node = Nodex(val=value, key=key)

        if key in self.cache:
            self.remove(self.cache[key])
        elif self.capacity == len(self.cache):
            lru_key = self.lru.key
            self.remove(self.cache[lru_key])
            del self.cache[lru_key]
        self.cache[key] = new_node
        self.insert(new_node)




if __name__ == "__main__":
    # ln3 = ListNode(3,None)
    # ln2 = ListNode(2,ln3)
    # ln1 = ListNode(1,ln2)
    # ln0 = ListNode(0,ln1)

    s = Solution()
    # x = s.reverseList(ln0)
    # while x:
    #     print(x.val)
    #     x = x.next

    # ll = LinkedList()
    # ll.add(1)
    # ll.add(2)
    # head = ll.add(3)

    # print(ll)

    # s.reorderList(head)
    # print(s)

    # s = {0:10, 1:20}
    # s.pop(0)
    # print(s)

    lc = LRUCache(10)
    print(lc.put(10, 13))
    print(lc.put(3, 17))
    print(lc.put(6, 11))
    print(lc.put(10, 5))
    print(lc.put(9, 10))
    print(lc.get(13))
    print(lc.put(2, 19))
    print(lc.get(2))
    print(lc.get(3))
    print(lc.put(5, 25))
    print(lc.get(8))
    print(lc.put(9, 22))
    print(lc.put(5, 5))
    print(lc.put(1, 30))
    print(lc.get(11))
    print(lc.put(9, 12))
    print(lc.get(7))
    print(lc.get(5))
    print(lc.get(8))
    print(lc.get(9))
    print(lc.put(4, 30))
    print(lc.put(9, 3))
    print(lc.get(9))
    print(lc.get(10))
    print(lc.get(10))
    print(lc.put(6, 14))
    print(lc.put(3, 1))
    print(lc.get(3))
    print(lc.put(10, 11))
    print(lc.get(8))
    print(lc.put(2, 14))
    print(lc.get(1))
    print(lc.get(5))
    print(lc.get(4))
    print(lc.put(11, 4))
    print(lc.put(12, 24))
    print(lc.put(5, 18))
    print(lc.get(13))
    print(lc.put(7, 23))
    print(lc.put(8, 27))
    print(lc.put(12, 12))
    print(lc.get(3))
    print(lc.put(3, 21))
    print(lc.put(10, 10))
    print(lc.get(8))
    print(lc.get(11))
    print(lc.get(7))
    print(lc.put(7, 10))
    print(lc.put(9, 2))
    print(lc.put(5, 8))
    print(lc.get(11))
    print(lc.put(8, 2))
    print(lc.put(11, 1))
    print(lc.put(5, 5))
    print(lc.get(5))
    print(lc.put(4, 9))
    print(lc.get(4))
    print(lc.get(10))
    print(lc.put(6, 18))
    print(lc.put(4, 7))
    print(lc.put(8, 12))
    print(lc.get(7))
    print(lc.get(5))
    print(lc.get(4))
    print(lc.get(5))
    print(lc.put(7, 23))
    print(lc.get(3))
    print(lc.put(7, 3))
    print(lc.put(4, 4))
    print(lc.put(10, 6))
    print(lc.get(6))
    print(lc.put(3, 9))
    print(lc.get(3))
    print(lc.get(4))
    print(lc.put(11, 11))
    print(lc.put(1, 12))
    print(lc.get(3))
    print(lc.put(1, 2))
    print(lc.put(5, 6))
    print(lc.get(5))
    print(lc.put(1, 11))
    print(lc.put(8, 12))
    print(lc.get(2))
    print(lc.get(5))
    print(lc.get(9))
    print(lc.put(10, 1))
    print(lc.put(1, 3))
    print(lc.get(10))
    print(lc.put(10, 2))
    print(lc.put(1, 11))
    print(lc.put(5, 5))
    print(lc.put(7, 5))
    print(lc.put(10, 10))
    print(lc.get(9))
    print(lc.get(4))
    print(lc.get(4))
    print(lc.get(6))
    print(lc.get(11))
    print(lc.put(7, 13))
    print(lc.put(2, 7))
    print(lc.put(10, 13))
    print(lc.put(8, 5))
    print(lc.put(9, 10))
    print(lc.get(6))
    print(lc.get(10))
    print(lc.put(3, 5))
    print(lc.put(10, 12))
    print(lc.put(5, 12))
    print(lc.get(8))
    print(lc.get(3))
    print(lc.put(3, 1))
    print(lc.put(4, 6))
    print(lc.put(10, 4))
    print(lc.put(8, 10))
    print(lc.put(4, 9))
    print(lc.put(2, 13))
    print(lc.put(10, 8))
    print(lc.put(1, 8))
    print(lc.put(1, 2))
    print(lc.put(4, 6))
    print(lc.put(4, 2))
    print(lc.put(10, 10))
    print(lc.put(9, 12))
    print(lc.get(4))
    print(lc.get(10))
    print(lc.get(10))
    print(lc.get(9))
    print(lc.put(8, 7))
    print(lc.get(5))
    print(lc.put(3, 8))
    print(lc.get(10))
    print(lc.put(5, 11))
    print(lc.put(5, 2))
    print(lc.get(8))
    print(lc.put(1, 3))
    print(lc.put(7, 8))
    print(lc.get(1))
    print(lc.put(6, 5))
    print(lc.get(9))
    print(lc.put(7, 12))
    print(lc.get(5))
    print(lc.get(8))
    print(lc.put(10, 4))
    print(lc.put(1, 9))
    print(lc.put(2, 4))
    print(lc.put(2, 5))
    print(lc.put(10, 10))
    print(lc.get(5))
    print(lc.get(9))
    print(lc.get(10))
    print(lc.put(8, 3))
    print(lc.put(1, 7))
    print(lc.put(10, 7))
    print(lc.put(4, 8))
    print(lc.put(2, 11))
    print(lc.put(8, 2))
    print(lc.get(1))
    print(lc.get(9))
    print(lc.get(2))
    print(lc.put(2, 5))
    print(lc.put(3, 8))
    print(lc.put(1, 8))
    print(lc.put(2, 7))
    print(lc.get(10))
    print(lc.get(3))
    print(lc.put(1, 4))
    print(lc.put(10, 5))
    print(lc.get(8))
    print(lc.get(2))
    print(lc.get(2))
    print(lc.get(1))
    print(lc.put(9, 2))
    print(lc.get(5))
    print(lc.get(7))
    print(lc.put(10, 3))
    print(lc.put(5, 5))
    print(lc.put(1, 10))
    print(lc.put(2, 10))
    print(lc.get(4))
    print(lc.get(3))
    print(lc.get(1))
    print(lc.get(1))
    print(lc.put(3, 7))
    print(lc.get(9))
    print(lc.put(10, 2))
    print(lc.get(3))
    print(lc.get(4))
    print(lc.put(6, 4))
    print(lc.get(6))
    print(lc.put(7, 11))
    print(lc.get(8))
    print(lc.get(6))
    print(lc.put(2, 2))
    print(lc.get(2))
    print(lc.put(7, 9))
    print(lc.put(8, 6))
    print(lc.put(2, 4))
    print(lc.get(8))
    print(lc.get(1))
    print(lc.put(7, 5))
    print(lc.put(4, 1))
    print(lc.get(10))
    print(lc.put(6, 3))
    print(lc.get(6))
    print(lc.put(4, 6))
    print(lc.put(1, 8))
    print(lc.put(6, 7))
    print(lc.put(3, 4))
    print(lc.put(4, 3))
    print(lc.get(10))
    print(lc.get(3))
    print(lc.get(7))
    print(lc.put(4, 3))
    print(lc.get(8))
    print(lc.put(3, 7))
    print(lc.get(4))
    print(lc.get(10))
    print(lc.put(6, 4))
    print(lc.put(5, 10))
    print(lc.put(2, 4))
    print(lc.put(5, 6))
    print(lc.put(10, 9))
    print(lc.put(5, 8))
    print(lc.put(1, 3))
    print(lc.put(7, 5))
    print(lc.put(8, 10))
    print(lc.get(3))
    print(lc.put(6, 4))
    print(lc.get(5))
    print(lc.put(8, 2))
    print(lc.put(8, 7))
    print(lc.put(6, 4))
    print(lc.get(10))
    print(lc.put(9, 3))
    print(lc.put(4, 7))
    print(lc.get(6))
    print(lc.put(5, 10))
    print(lc.get(10))
    print(lc.get(10))
    print(lc.put(8, 5))
    print(lc.get(4))
    print(lc.put(5, 9))
    print(lc.put(9, 9))
    print(lc.put(5, 2))
    print(lc.put(6, 4))
    print(lc.put(3, 8))
    print(lc.put(8, 8))
    print(lc.put(10, 2))
    print(lc.put(2, 7))
    print(lc.put(1, 7))
    print(lc.put(10, 9))
    print(lc.get(4))
    print(lc.get(1))
    print(lc.get(7))
    print(lc.put(8, 10))
    print(lc.get(6))
    print(lc.put(4, 5))
    print(lc.get(7))
    print(lc.put(3, 9))
    print(lc.get(4))
    print(lc.get(1))
    print(lc.put(6, 9))
    print(lc.put(10, 10))
    print(lc.put(9, 1))
    print(lc.put(4, 6))
    print(lc.put(1, 10))
    print(lc.get(8))
    print(lc.put(7, 10))
    print(lc.get(9))
    print(lc.put(5, 5))
    print(lc.put(1, 3))
    print(lc.get(8))
    print(lc.put(2, 7))
    print(lc.get(9))
    print(lc.put(6, 4))
    print(lc.get(7))
    print(lc.put(2, 9))
    print(lc.get(10))
    print(lc.get(6))


