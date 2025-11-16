from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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



if __name__ == "__main__":
    # ln3 = ListNode(3,None)
    # ln2 = ListNode(2,ln3)
    # ln1 = ListNode(1,ln2)
    # ln0 = ListNode(0,ln1)

    # s = Solution()
    # x = s.reverseList(ln0)
    # while x:
    #     print(x.val)
    #     x = x.next

    ll = LinkedList()
    ll.add(1)
    # ll.add(2)
    # ll.add(3)

    print(ll)
