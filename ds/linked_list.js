class ListNode {
    constructor(val){
        this.val = val;
        this.next = null;
    }
}

class LinkedList {
    constructor(){
        this.head = new ListNode(-1);
        this.tail = this.head;
    }

    insertEnd(val){
        let newNode = new ListNode(val);
        this.tail.next = newNode;
        this.tail = this.tail.next;
    }

    removeEnd(){
        let curr = this.head.next;
        while(curr.next.next){
            curr = curr.next;
        }
        curr.next = curr.next.next;
        this.tail = curr;
    }

    removeFront(){
        this.head.next = this.head.next.next;
    }

    removeIndex(index){
        let i = 0;
        let curr = this.head;
        while(i < index && curr){
            i++;
            curr = curr.next;
        }
        if(curr && curr.next){
            if(curr.next == this.tail){
                this.tail = curr;
            }
            curr.next = curr.next.next;
        }
    }
}

function TestLinkedList(){
    const assert = require('assert');
    let linkedList = new LinkedList();
    linkedList.insertEnd(1);
    linkedList.insertEnd(2);
    linkedList.insertEnd(3);
    linkedList.insertEnd(4);
    linkedList.insertEnd(5);

    linkedList.removeEnd();
    assert(linkedList.tail.val === 4);

    linkedList.removeFront();
    assert(linkedList.head.next.val === 2);

    linkedList.removeIndex(1);
    assert(linkedList.head.next.next.val === 4);

    console.log('All test cases pass');
}

TestLinkedList();