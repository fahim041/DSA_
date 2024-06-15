class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insertFront(self, val):
        newNode = ListNode(val)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def insertEnd(self, val):
        newNode = ListNode(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def removeFront(self):
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def removeEnd(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

    def print(self):
        curr = self.head.next
        while curr != self.tail:
            print(curr.val)
            curr = curr.next

# test cases
def test_linked_list():
    ll = LinkedList()
    ll.insertEnd(1)
    ll.insertFront(13)
    ll.insertFront(2)
    ll.insertEnd(20)

    ll.removeEnd()
    ll.removeFront()

    assert ll.head.next.val == 13
    assert ll.tail.prev.val == 1

    print('All test cases pass')

test_linked_list()