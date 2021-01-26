export class Queue {

  constructor() {
    this.data = []
  }

  enqueue(element) {
    this.data.push(element)
  }

  dequeue() {
    if (!this.isEmpty()) {
      return this.data.shift()
    }
  }

  front() {
    if (!this.isEmpty()) {
      return this.data[0]
    } else {
      return []
    }
  }

  isEmpty() {
    return this.data.length === 0
  }

}