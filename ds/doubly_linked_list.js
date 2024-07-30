class ListNode {
    constructor(val){
        this.val = val;
        this.next = null;
        this.prev = null;
    }
}

class LinkedList {
    constructor(){
        this.head = new ListNode(-1);
        this.tail = new ListNode(-1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    insertFront(val){
        let newNode = new ListNode(val);
        newNode.next = this.head.next;
        newNode.prev = this.head;
        this.head.next.prev = newNode;
        this.head.next = newNode;
    }

    insertEnd(val){
        let newNode = new ListNode(val);
        newNode.next = this.tail;
        newNode.prev = this.tail.prev;

        this.tail.prev.next = newNode;
        this.tail.prev = newNode;
    }

    removeFront(){
        this.head.next.next.prev = this.head;
        this.head.next = this.head.next.next;
    }

    removeEnd(){
        let node = this.tail.prev;
        node.prev.next = this.tail;
        this.tail.prev = node.prev;
    }
}

function testLinkedList(){
    const assert = require('assert');

    let linkedList = new LinkedList();
    linkedList.insertEnd(1);
    linkedList.insertEnd(2);
    linkedList.insertEnd(3);
    linkedList.insertEnd(4);
    linkedList.insertEnd(5);

    linkedList.removeEnd();
    assert(linkedList.tail.prev.val === 4);

    linkedList.removeFront();
    assert(linkedList.head.next.val === 2);

    linkedList.insertFront(0);
    assert(linkedList.head.next.val === 0);

    linkedList.removeFront();
    assert(linkedList.head.next.val === 2);

    linkedList.removeEnd();
    assert(linkedList.tail.prev.val === 3);

    console.log('All test cases pass');
}

testLinkedList();