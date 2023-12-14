class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null; // "this" points to its parent which is LinkedList class.
  }

  addFirst(data) {
    const newNode = new Node(data);
    newNode.next = this.head;
    this.head = newNode;
  }
  addLast(data) {
    const newNode = new Node(data);
    if (!this.head) {
      this.head = newNode;
      return;
    }
    let current = this.head;
    while (current.next) {
      current = current.next;
    }
    current.next = newNode;
  }
  size() {
    let l = 0;
    let current = this.head;
    while (current.next) {
      current = current.next;
      l += 1;
    }
    return l;
  }
  addAt(index, data) {
    const newNode = new Node(data);
    if (index == 0 || index > this.size()) {
      console.log("Invalid Index");
      return;
    }
    if (!this.head) {
      this.head = newNode;
      return;
    }
    let current = this.head;
    for (let i = 0; i < index - 1; i++) {
      current = current.next;
    }
    newNode.next = current.next; // 16
    current.next = newNode; //  26
  }

  removeFirst() {
    if (!this.head) {
      return;
    }
    this.head = this.head.next;
  }

  removeLast() {
    //own
    if (!this.head) {
      console.log("Empty!");
    }
    let current = this.head;
    for (let i = 0; i < this.size() - 1; i++) {
      current = current.next;
    }
    current.next = null;
  }
  removeAt(index) {
    //own
    if (index == 0 || index > this.size()) {
      console.log("Invalid Index");
      return;
    }
    let current = this.head;
    for (let i = 0; i < index - 1; i++) {
      current = current.next;
    }
    current.next = current.next.next;
  }
  print() {
    let current = this.head;
    while (current) {
      process.stdout.write(`${current.data} --> `);
      current = current.next;
    }
  }
}

const linkedList = new LinkedList();
linkedList.addFirst(5);
linkedList.addFirst(10);
linkedList.addFirst(13);
linkedList.addAt(2, 16);
linkedList.addAt(1, 26);
linkedList.removeFirst();
linkedList.removeLast();
linkedList.removeAt(1);
console.log("Size of LinkedList ", linkedList.size());
linkedList.print();
