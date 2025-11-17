from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


    
    # def __str__(self):
    #     vals = []
    #     curr = self.head
    #     while curr is not None:
    #         vals.append(curr.val)
    #         curr = curr.next
    #     return str(vals)


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

    s = Solution()
    # x = s.reverseList(ln0)
    # while x:
    #     print(x.val)
    #     x = x.next

    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    head = ll.add(3)

    print(ll)

    s.reorderList(head)
    print(s)

    # s = {0:10, 1:20}
    # s.pop(0)
    # print(s)
