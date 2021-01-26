export class Stack {

  constructor() {
    this.data = []
    this.top = 0
  }

  push(element) {
    this.data.push(element)
    this.top++
  }

  pop() {
    if (!this.isEmpty()) {
      this.top--;
      return this.data.pop()
    }
  }

  peek() {
    return this.data[this.top - 1]
  }

  length() {
    return this.top
  }

  search(element) {
    this.data.forEach((e, i) => {
      if (e === element) return i
    })

    return -1
  }

  isEmpty() {
    return this.top === 0
  }

}