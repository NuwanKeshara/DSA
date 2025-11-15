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









if __name__ == "__main__":
    ln3 = ListNode(3,None)
    ln2 = ListNode(2,ln3)
    ln1 = ListNode(1,ln2)
    ln0 = ListNode(0,ln1)

    s = Solution()
    x = s.reverseList(ln0)
    while x:
        print(x.val)
        x = x.next

