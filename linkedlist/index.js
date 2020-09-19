// --- Directions
// Implement classes Node and Linked Lists
// See 'directions' document

class Node {
    constructor(data, next = null){
        this.data = data;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
    }

    insertFirst(data) {
        this.insertAt(data, 0);
    }

    size(){
        let length = 0;
        let node = this.head;
        while(node){
            length++;
            node= node.next
        }
        return length;
    }

    getFirst() {
        return this.getAt(0);
    }

    getLast() {
        // if(!this.head) return null;
        // let node = this.head;
        // while(node) {
        //     if(!node.next) return node;
        //     node = node.next;
        // } 
    
        // return node;
        return this.getAt(this.size() - 1);
    }

    clear(){
        this.head = null;
    }

    removeFirst() {
     if(this.head) this.head = this.head.next;
    }

    removeLast(){
        
        if(!this.head) return;
        if(!this.head.next) {
             this.head = null;
             return;
        }

        let previous = this.head;
        let node = this.head.next;

        while(node.next) {
            previous = node;
            node = node.next;
        }

        previous.next = null;
    }

    insertLast(data){
        const last = this.getLast();

       if(last) last.next = new Node(data);
       else this.head = new Node(data);
    }

    getAt(index){
        let counter = 0;
        let node = this.head;
        while(node) {
            if(counter === index) return node;
            counter++;
            node = node.next;
        }

        return null;
    }

    removeAt(index){
        if(!this.head) return;
        if(index === 0) {
            this.head = this.head.next;
        }

        const node = this.getAt(index-1);
        if(!node || !node.next) return;
        node.next = node.next.next;
    }

    insertAt(data, index){
        if(!this.head){
            this.head = new Node(data);
            return;
        } 
        if(index === 0){
            this.head = new Node(data, this.head);
            return;
        }

        const previous = this.getAt(index-1) || this.getLast();
        previous.next = new Node(data, previous.next);

    }

    forEach(fn){
        let node = this.head;
        let counter = 0;
        while(node){
            fn(node, counter);
            node =  node.next;
            counter++
        }
    }

    *[Symbol.iterator](){
        let node = this.head;
        while(node){
            yield node;
            node = node.next;
        }
    }
}

const l  = new LinkedList();
l.insertFirst(1);
l.insertFirst(2);
l.insertLast(3);
l.getAt(3);
l.insertAt('a', 0)
console.log(l);

module.exports = { Node, LinkedList };
