class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    #O(1)
    def insertEnd(self, val):
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    #O(n)
    def removeEnd(self):
        curr = self.head.next
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.tail = curr

    #O(1)
    def removeFront(self):
        self.head.next = self.head.next.next

    def removeIndex(self, index):
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    #O(n)
    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val)
            curr = curr.next

# test cases for linked list with assertion
def test_linked_list():
    ll = LinkedList()
    ll.insertEnd(1)
    ll.insertEnd(2)
    ll.insertEnd(3)
    ll.insertEnd(4)
    ll.insertEnd(5)

    ll.removeEnd()
    ll.removeIndex(2)
    ll.removeFront()

    assert ll.head.next.val == 2
    assert ll.tail.val == 4

    print('All test cases pass')

test_linked_list()

