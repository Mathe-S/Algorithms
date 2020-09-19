// --- Directions
// Return the 'middle' node of a linked list.
// If the list has an even number of elements, return
// the node at the end of the first half of the list.
// *Do not* use a counter variable, *do not* retrieve
// the size of the list, and only iterate
// through the list one time.
// --- Example
//   const l = new LinkedList();
//   l.insertLast('a')
//   l.insertLast('b')
//   l.insertLast('c')
//   midpoint(l); // returns { data: 'b' }

// import {LinkedList} from './linkedlist';

function midpoint(list) {
    let midPoint = list.getFirst();
    let lastPoint = list.getFirst();

    while(lastPoint.next && lastPoint.next.next){
        midPoint = midPoint.next;
        lastPoint = lastPoint.next.next;
    }
    // console.log(midPoint);
    // console.log(list);
    return midPoint;
}

// const l = new LinkedList();
//     l.insertLast('a');
//     l.insertLast('b');
//     l.insertLast('c');
//     l.insertLast('d');
//     l.insertLast('e');
    
// midpoint(l);

module.exports = midpoint;
